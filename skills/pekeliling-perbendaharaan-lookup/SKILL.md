---
name: pekeliling-perbendaharaan-lookup
description: Database layout, search method, in-force status checks, source priority, and citation rules for finding and citing Pekeliling Perbendaharaan (all 7 bidang — PB, PK, WP, AM, PS, PA, LB), Surat Edaran, Arahan Perbendaharaan (AP), and garis panduan when advising on the right regulatory pathway for a Kertas Pertimbangan, Kertas Kelulusan, Surat, or Memo. Used by the Ijah agent — load this before searching or citing any circular.
---

# Pekeliling Perbendaharaan Lookup — Database, Sources & Citation Rules

**Scope:** Pekeliling Perbendaharaan in all seven bidang of the Portal Pekeliling Perbendaharaan (https://ppp.treasury.gov.my/), their Surat Edaran, Arahan Perbendaharaan (AP), and garis panduan. **Out of scope:** Pekeliling Perkhidmatan / HR-only circulars.

| Kod | Bidang |
|---|---|
| PB | Pengurusan Belanjawan |
| PK | Perolehan Kerajaan |
| WP | Pengurusan Wang Awam |
| AM | Pengurusan Aset |
| PS | Tadbir Urus Kewangan |
| PA | Pelaburan Strategik |
| LB | Syarikat Tersenarai Bumiputera |

## 0. The local database

Root: `<PEKELILING_FOLDER>/` — a mirror of the **current** circulars on the portal (no Arkib).

| Path | What it is |
|---|---|
| `<KOD> - <Bidang>/<NN - Topik>/<NN - Tajuk>.pdf` | Original PDFs, arranged exactly as the portal (topic `00` = Surat Edaran / Makluman Terkini) |
| `text/<same path>.md` | Full text of each PDF. **Search and read these.** |
| `manifest.json` | One record per document: `bidang`, `topic`, `label`, `title`, `url` (portal link), `local_path`, `sha256`, `downloaded_at` |
| `tools/` | Download/OCR scripts — never edit |

Each `text/*.md` starts with YAML front matter (`bidang`, `topic`, `title`, `label`, `source_url`, `pdf`, `sha256`, `pages`, `ocr_pages`), then the text with a marker before every page:

```
<!-- page 4 (text) -->   ← exact text layer from the PDF
<!-- page 5 (ocr) -->    ← scanned page, read by OCR; tables appear as HTML <table>
```

Scanned-page tables are kept as HTML `<table>` rows — read them cell by cell.

**Not in the database:** Arahan Perbendaharaan (AP) itself, archived/repealed circulars (Arkib), and anything issued after `downloaded_at`. Treat those as web lookups (Step 2).

## 1. Source priority (check in this exact order)

### Step 0 — Decision log (ALWAYS first)

File: `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md`

A running log of every issue previously researched, so research isn't repeated and recommendations stay consistent with precedent. If it doesn't exist, create it with two sections: **Indeks Pantas** (table: Tarikh | Isu | Instrumen utama | Cadangan) and **Log Terperinci** (chronological entries).

- Read it in full before searching anything. Reuse a matching entry if nothing suggests it's stale, and say so with its date.
- Before reusing, confirm the instruments it cites are still in `manifest.json` with the same `sha256`. A changed hash means the circular was replaced or amended: re-verify.
- After every session, append exactly one entry to Log Terperinci and update Indeks Pantas. Never upgrade a `[BELUM DISAHKAN]` label when logging.

### Step 1 — Local database (primary source)

1. **Pick the bidang** the issue touches (often more than one).
2. **Search the text, not the filenames.** Use Grep over `text/` with Malay keywords plus synonyms and spelling variants, case-insensitive. Examples:
   - `sebut harga|sebutharga`, `rundingan terus`, `pembelian terus`, `had nilai`, `tender terbuka`
   - `pelupusan`, `hapus kira`, `pindah peruntukan`, `pendahuluan diri`, `elaun`, `majlis rasmi`
   Narrow by bidang folder (e.g. `text/PK - Perolehan Kerajaan/`). Use `-l` first to list files, then `-n -C` to see context.
3. **Identify the instrument** from front matter (`title`, `label`, `topic`) and from the document's own heading (e.g. "PK 2.5"). The portal label is not always the circular number; take the number from the document text.
4. **Read the relevant pages in full** (from the page marker to the next marker) before quoting. Never quote from a grep snippet alone.
5. **Record the page number** from the nearest `<!-- page N -->` marker above the clause, and the paragraph number from the text itself.

**Verifying OCR'd figures.** If a number you will rely on (threshold, rate, amount, date, circular or paragraph number) comes from a `(ocr)` page, render the page and look at it:

```bash
pdftoppm -f N -l N -r 150 -png "<PEKELILING_FOLDER>/<pdf path>" /tmp/ijah_pN
```

Then Read the resulting PNG and confirm the figure. Label it `[DISAHKAN — Fail Tempatan (OCR, disemak imej)]`. If you could not check the image, say the figure is from OCR and unchecked.

### Checking whether a circular is still in force (mandatory)

The portal lists only current topics, but some listed documents are themselves cancelled or partly amended. For every instrument you cite:

- Scan the label/title and first page for: `DIBATALKAN`, `PEMBATALAN`, `PINDAAN`, `MEMINDA`, `MENGGANTIKAN`, `BERKUAT KUASA`, `TARIKH KUAT KUASA`. Example: some PB labels end "(PEKELILING DIBATALKAN)".
- Grep the whole `text/` tree for the circular's number (e.g. `PK 2\.5|PK2\.5`) to find **later** Surat Edaran or pindaan that amend, exempt, or cancel particular paragraphs. Topic `00` (Surat Edaran) folders are the usual place.
- If several versions are present, cite the one with the latest effective date and state what it replaced.
- State status in the output: *Berkuat kuasa sejak <tarikh>* / *Dipinda oleh <instrumen, tarikh>* / *Perenggan X dibatalkan oleh <instrumen>* / *Dibatalkan*.

**Freshness rule.** Check `downloaded_at` in `manifest.json`. If the snapshot is more than 30 days old, **or** the issue depends on a threshold or rate, check the portal's "Makluman Terkini" (https://ppp.treasury.gov.my/) for anything newer on that topic before finalising. Tell the user the snapshot date either way.

### Step 2 — Official web sources (gaps, AP, freshness)

1. https://ppp.treasury.gov.my/ (Portal Pekeliling Perbendaharaan) and treasury.gov.my, including Arahan Perbendaharaan.
2. ePerolehan (eP), for procurement system procedures.
3. Jabatan Akauntan Negara Malaysia (JANM), where it is the issuing authority.
4. Only then a general web search, and only to find a link back to an official domain. Never cite a repost or blog.

Note each web-found circular's date and whether it says it supersedes or amends an earlier one.

## 2. Citation format and confidence labels

Cite as: **<Kod + nombor> <Tajuk>, perenggan <x>, ms <n>**. For example: *PK 2.5 Kontrak Pusat, perenggan 4.2, ms 6*. Give the `text/` path, PDF path and `source_url` in Rujukan.

Every instrument cited MUST carry one label:

- **[DISAHKAN — Fail Tempatan]**: quoted directly from a `(text)` page of the local database.
- **[DISAHKAN — Fail Tempatan (OCR, disemak imej)]**: quoted from an `(ocr)` page, with key figures checked against the rendered page image.
- **[DISAHKAN — Sumber Rasmi]**: read directly from an official web source. Cite the URL.
- **[BELUM DISAHKAN]**: from general knowledge, or an OCR figure not checked against the image. Not verified this session. Flag it explicitly and tell the user to confirm it before citing in a signed paper. **Never present it with the same confidence as a DISAHKAN item.**

If nothing relevant can be found or verified, say so plainly. Never invent a circular number, paragraph or threshold to fill a gap.

## 3. What "suitable pathway" analysis looks like

1. **Isu/Keperluan**: a one-line restatement, plus the bidang involved.
2. **Instrumen berkaitan**: each instrument with its status, quoted clause, page, and label.
3. **Pilihan laluan (2–4)**: genuinely distinct pathways, each with Kelebihan, Kekurangan/Risiko, and the relevant cited threshold.
4. **Cadangan**: the most defensible pathway and why, or an honest toss-up.
5. **Cadangan teks (optional)**: a ready-to-paste DASAR SEMASA or justification sentence in house style (see `mof-house-style`).
6. **Rujukan**: every source checked, plus the database snapshot date.

This slots straight into the **DASAR SEMASA** and **ULASAN** sections of `kertas-pertimbangan-mof`, or the justification paragraph of `surat-mof` / `memo-mof`. The final delivery format is the user's call.

## 4. Files this workflow writes

Only `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md` (append-only), plus throwaway page images under `/tmp`. Never modify the PDFs, `text/`, `manifest.json`, or `tools/`.
