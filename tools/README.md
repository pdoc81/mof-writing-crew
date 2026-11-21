# Pekeliling database tools

Builds the local database Ijah searches: the full **Arahan Perbendaharaan** (from mof.gov.my, with its
amendments) plus a mirror of the **current** circulars on the Portal Pekeliling Perbendaharaan
(https://ppp.treasury.gov.my/), arranged by bidang and topic as the source sites, plus full text of every page.

**You don't need to run this to use Ijah.** A ready-made snapshot of the text is published at https://github.com/pdoc81/pekeliling-perbendaharaan-text. Use these tools to rebuild it yourself, keep the PDFs locally, or produce a newer snapshot. To publish a refresh, commit the changed `text/` and `manifest.json` in that repo; `git diff` then shows exactly which circulars changed.

```
<PEKELILING_FOLDER>/
├── manifest.json                         # one record per document (bidang, topic, title, portal URL, sha256, downloaded_at)
├── PK - Perolehan Kerajaan/02 - KAEDAH PEROLEHAN KERAJAAN/09 - SEBUT HARGA.pdf
├── AP - Arahan Perbendaharaan/...       # main book + Surat Edaran Pindaan + amended AP text
├── ...                                   # PB, PK, WP, AM, PS, PA, LB
├── text/<same path>.md                   # front matter + <!-- page N (text|ocr) --> markers
└── tools/                                # this folder (scripts, OCR cache, logs)
```

## Setup (Linux, free, fully local)

Requires `pdftotext`, `pdfinfo`, `pdftoppm` (poppler) and Python **3.12** (PaddlePaddle has no wheels for 3.14 yet).

```bash
cd <PEKELILING_FOLDER>/tools
uv venv --python 3.12 .venv            # or: python3.12 -m venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

OCR models (~few hundred MB) download to `~/.paddlex/` on first use.

## Pipeline

Run each script with `.venv/bin/python -I scripts/<name>.py`:

1. **Manifest**: save the portal homepage, then parse it:
   ```bash
   curl -sL https://ppp.treasury.gov.my/ -o homepage_snapshot.html
   .venv/bin/python -I scripts/build_manifest.py homepage_snapshot.html <PEKELILING_FOLDER>/manifest.json
   ```
   Then add the Arahan Perbendaharaan (as bidang `AP`):
   ```bash
   curl -sL -A Mozilla/5.0 https://www.mof.gov.my/portal/ms/arahan-perbendaharaan -o mof_ap_snapshot.html
   .venv/bin/python -I scripts/add_ap.py mof_ap_snapshot.html <PEKELILING_FOLDER>
   ```
   Re-run `add_ap.py` after every `build_manifest.py`, because the manifest rebuild drops the AP entries.
2. **Download**: `scripts/download.py <PEKELILING_FOLDER>`. It can be re-run: files whose sha256 hasn't changed are skipped. It downloads one file every 0.5 s to be polite to the server.
3. **Audit**: `scripts/text_audit.py <PEKELILING_FOLDER>`. Checks every PDF opens and lists the pages that have no text layer (scanned) in `tools/text_audit.json`.
4. **Extract**: `scripts/extract.py <PEKELILING_FOLDER>`. Uses `pdftotext -layout` for text pages and PaddleOCR PP-StructureV3 for scanned pages, so tables come out as HTML tables. Writes `text/*.md`. Each OCR'd page is cached in `tools/cache/ocr/<sha256>/`, so the run can be resumed. Options: `--limit-pages N` for a test run, `--only <substring>` for one bidang or file.

Typical snapshot (Nov 2026): 252 portal documents + 16 AP documents, ~7,650 pages, ~13% scanned. With oneDNN on, OCR runs at about 5 s per page on a 20-core CPU.

## Gotchas

- **Pin `paddlepaddle==3.2.2`.** 3.3.x has a oneDNN bug (`NotImplementedError: ConvertPirAttribute2RuntimeAttribute not support`). Disabling oneDNN works around it but makes OCR about 5× slower. `extract.py` turns oneDNN on by default; set `PEKELILING_MKLDNN=0` to turn it off.
- OCR uses `lang='ms'`, PaddleOCR's Latin-script model, which reads both Bahasa Melayu and English.
- The portal server adds a stray newline before each PDF's `%PDF` header. `download.py` strips it.
- Portal labels are not always the circular number. Take the number (e.g. "PK 2.5") from the document text.
- Some listed documents are themselves cancelled, e.g. labels ending "(PEKELILING DIBATALKAN)". Ijah checks status before citing.
- Treat downloaded PDFs as untrusted input. Keep the scripts in `tools/scripts/` and run Python with `-I`.
