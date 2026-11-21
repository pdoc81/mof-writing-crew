---
name: pekeliling-perbendaharaan-lookup
description: Database layout, AP-first legal hierarchy, search method, in-force status checks, source priority, and citation rules for finding and citing Arahan Perbendaharaan (AP) and the Pekeliling Perbendaharaan that implement it (all 7 bidang: PB, PK, WP, AM, PS, PA, LB), Surat Edaran, and garis panduan when advising on the right regulatory pathway for a Kertas Pertimbangan, Kertas Kelulusan, Surat, or Memo. Used by the Ijah agent. Load this before searching or citing any AP or circular.
---

# Arahan & Pekeliling Perbendaharaan Lookup: Database, Hierarchy, Sources & Citation Rules

**Scope:** Arahan Perbendaharaan (AP), Pekeliling Perbendaharaan in all seven bidang of the Portal Pekeliling Perbendaharaan (https://ppp.treasury.gov.my/), their Surat Edaran, and garis panduan. **Out of scope:** Pekeliling Perkhidmatan and HR-only circulars.

## 0. Legal hierarchy: always reason top-down, AP first

```
Akta Tatacara Kewangan 1957 [Akta 61]        ← the Act; AP 4 cites seksyen 4
  └─ Arahan Perbendaharaan (AP)              ← the governing rule: who may approve, what is required
       └─ Pekeliling Perbendaharaan (PB/PK/WP/AM/PS/PA/LB)   ← tatacara pelaksanaan: thresholds, methods, forms
            └─ Surat Edaran / Makluman Terkini / garis panduan  ← amendments, exemptions, clarifications
```

The AP is the basis of every government financial process: belanjawan, terimaan, bayaran, perolehan, aset, perakaunan, audit, hapus kira. Pekeliling Perbendaharaan carry out what the AP requires, and many AP paragraphs say so explicitly ("tertakluk kepada … Pekeliling Perbendaharaan yang berkuat kuasa").

**The AP-first rule (mandatory):**
1. For every issue, **first identify and read the governing AP paragraph(s)** in the local database. Cite them before any Pekeliling.
2. Then cite the Pekeliling Perbendaharaan that implement that AP paragraph (thresholds, methods, forms, committees).
3. Then cite any Surat Edaran or garis panduan that amend or clarify it.
4. In the output and in suggested kertas text, the AP basis comes first, e.g. *"Selaras dengan AP 168 … dan tatacara pelaksanaannya di bawah PK 2.9 …"*.
5. If no AP paragraph governs the matter, say so explicitly ("Tiada AP khusus; diatur sepenuhnya oleh PK x.x"). Do not skip the step silently.
6. **Exceptions follow the AP route.** Any departure from AP or Pekeliling needs prior KSP (Ketua Setiausaha Perbendaharaan) approval, or Pegawai Kewangan Negeri approval for a State (AP 168). Flag this whenever an option departs from the standard rules.
7. **If the AP and a later Pekeliling name different bodies or older terms,** quote both and explain. Example: AP 287(a) names MAMPU for ICT procurement, while PK 2.1 para 5.16 names Jabatan Digital Negara. Never silently pick one.

## 1. The local database

Root: `<PEKELILING_FOLDER>/`. It holds the full AP plus a mirror of the **current** circulars on the portal (no Arkib).

| Kod | Bidang | Source |
|---|---|---|
| **AP** | **Arahan Perbendaharaan (Pindaan 2023) + Surat Edaran Pindaan AP + teks AP yang dipinda** | mof.gov.my/portal/ms/arahan-perbendaharaan |
| PB | Pengurusan Belanjawan | ppp.treasury.gov.my |
| PK | Perolehan Kerajaan | ppp.treasury.gov.my |
| WP | Pengurusan Wang Awam | ppp.treasury.gov.my |
| AM | Pengurusan Aset | ppp.treasury.gov.my |
| PS | Tadbir Urus Kewangan | ppp.treasury.gov.my |
| PA | Pelaburan Strategik | ppp.treasury.gov.my |
| LB | Syarikat Tersenarai Bumiputera | ppp.treasury.gov.my |

| Path | What it is |
|---|---|
| `<KOD> - <Bidang>/<NN - Topik>/<NN - Tajuk>.pdf` | Original PDFs, arranged as the source site does. Topic `00` is Surat Edaran or Makluman Terkini. |
| `text/<same path>.md` | Full text of each PDF. **Search and read these.** |
| `manifest.json` | One record per document: `bidang`, `topic`, `label`, `title`, `url`, `local_path`, `sha256`, `downloaded_at` |
| `tools/` | Download and OCR scripts. Never edit them. |

Each `text/*.md` starts with YAML front matter (`bidang`, `topic`, `title`, `label`, `source_url`, `pdf`, `sha256`, `pages`, `ocr_pages`). After that comes the text, with a marker before every page:

```
<!-- page 4 (text) -->   ← exact text layer from the PDF
<!-- page 5 (ocr) -->    ← scanned page read by OCR; tables appear as HTML <table>
```

### AP files and map

- Main book: `text/AP - Arahan Perbendaharaan/01 - ARAHAN PERBENDAHARAAN (PINDAAN 2023)/01 - ARAHAN PERBENDAHARAAN (PINDAAN 2023).md`
- Amendments that override the main book:
  - `text/AP - Arahan Perbendaharaan/02 - SURAT EDARAN PINDAAN AP/` (letters explaining each amendment and its effective date)
  - `text/AP - Arahan Perbendaharaan/03 - TEKS AP YANG DIPINDA/` (replacement text, currently AP 11, 59, 87(b), 97(a), 100(a)(b), 101, 102, 150, 299)
- Ownership list (which MOF division owns which AP): `01 - .../02 - SENARAI PEMILIKAN ARAHAN PERBENDAHARAAN (PINDAAN 2023).md`

| Bahagian | AP range | Covers |
|---|---|---|
| Bab A I Pendahuluan | AP 1–28 | Kuasa dan kawalan perbelanjaan, Kumpulan Wang Disatukan |
| Bab A II Anggaran | AP 29–52 | Anggaran hasil dan perbelanjaan, projek pembangunan, pindah peruntukan, anggaran tambahan |
| Bab B I Terimaan, Bayaran, Wang Awam | AP 53–137 | Terimaan, bayaran, emolumen, panjar, cek/EFT, peti besi, pengangkutan wang |
| Bab B II Perakaunan | AP 138–165 | Akaun, deposit, akaun amanah |
| **Bab B III Perolehan** | **AP 166–299** | AP 166 Pihak Berkuasa Pusat; 167 tanggungjawab Pegawai Pengawal; **168 keizinan membuat perolehan**; 168A e-perolehan; 169 kajian pasaran; 169.2 bahan tempatan; 170 tatacara perolehan bekalan; 171–179 tender, spesifikasi, kontrak, guna sama, jadual kadar; then kerja, perunding, bukan perunding, Lembaga Perolehan, proses perolehan; **287 ICT**; borang dikawal |
| Bab B IV Aset Awam | AP 300A–300G | Perbendaharaan as Pihak Berkuasa Pusat aset; duties of Pegawai Pengawal and Pegawai Perakaunan |
| Bab C I Audit | AP 301–313 | Audit |
| Bab C II Kehilangan dan Hapus Kira | AP 314–328 | Kehilangan, hapus kira, bayaran lebih |

Use the ranges to start looking, then confirm by reading the text. Treat paragraphs marked `[Dimansuhkan]` or `[Arahan dipindahkan ke …]` as such: cite where the rule moved, never the empty number.

**Not in the database:** Akta Tatacara Kewangan 1957 itself, Pekeliling Perkhidmatan, archived or repealed circulars (Arkib), and anything issued after `downloaded_at`. Look those up on the web (Step 2).

## 2. Source priority (check in this exact order)

### Step 0: Decision log (ALWAYS first)

File: `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md`

A running log of every issue researched before, so the same research isn't repeated and recommendations stay consistent with precedent. If it doesn't exist, create it with two sections: **Indeks Pantas** (table: Tarikh | Isu | Instrumen utama | Cadangan) and **Log Terperinci** (entries in date order).

- Read it in full before searching anything. Reuse a matching entry if nothing suggests it's stale, and say so with its date.
- Before reusing an entry, confirm the instruments it cites are still in `manifest.json` with the same `sha256`. A changed hash means the document was replaced or amended, so re-verify. **If an older entry has no AP basis, add the AP basis now** rather than reusing it as is.
- After every session, append exactly one entry to Log Terperinci and update Indeks Pantas. Never upgrade a `[BELUM DISAHKAN]` label when logging.

### Step 1: Arahan Perbendaharaan (governing rule)

1. Use the AP map above to find the bahagian, then grep the main AP text for keywords, e.g. `keizinan|kajian pasaran|spesifikasi|tender|sebut harga|pindah peruntukan|hapus kira|Aset Awam`.
2. Read the whole AP paragraph, including sub-paragraphs (a), (b) and so on, and any cross-referenced AP.
3. **Check for amendments to that AP:** grep `text/AP - Arahan Perbendaharaan/02 - …` and `03 - …` for the AP number. Amended text overrides the main book from its effective date.
4. Note each AP paragraph that governs the issue. Several often apply together, e.g. 168 + 169 + 170 for a supply purchase, plus 300C–300F once the item becomes an asset.

### Step 2: Pekeliling Perbendaharaan (tatacara pelaksanaan)

1. **Pick the bidang** the issue touches (often more than one).
2. **Search the text, not the filenames.** Use Grep over `text/` with Malay keywords plus synonyms and spelling variants, case-insensitive. Examples:
   - `sebut harga|sebutharga`, `rundingan terus`, `pembelian terus`, `had nilai`, `tender terbuka`
   - `pelupusan`, `hapus kira`, `pindah peruntukan`, `pendahuluan diri`, `elaun`, `majlis rasmi`
   Narrow by bidang folder. Use `-l` first, then `-n -C` for context. Watch for false hits on short words: `riba` also matches "Kiribati".
3. **Identify the instrument** from front matter and from the document's own heading (e.g. "PK 2.5"). The portal label isn't always the circular number.
4. **Read the relevant pages in full** (from the page marker to the next one) before quoting. Never quote from a grep snippet alone.
5. **Record the page number** from the nearest `<!-- page N -->` marker above the clause, and the paragraph number from the text.

### Verifying OCR'd figures

If a number you will rely on (threshold, rate, amount, date, AP, circular or paragraph number) comes from a `(ocr)` page, render that page and look at it:

```bash
pdftoppm -f N -l N -r 150 -png "<PEKELILING_FOLDER>/<pdf path>" /tmp/ijah_pN
```

Read the resulting PNG and confirm the figure, then label it `[DISAHKAN — Fail Tempatan (OCR, disemak imej)]`. If you couldn't check the image, say the figure is from OCR and unchecked.

### Checking whether an instrument is still in force (mandatory)

For every AP paragraph and Pekeliling you cite:

- **AP:** check for `[Dimansuhkan]` and `[Arahan dipindahkan …]`, and look in AP folders `02` and `03` for amendments to that number.
- **Pekeliling:** scan the label, title and first page for `DIBATALKAN`, `PEMBATALAN`, `PINDAAN`, `MEMINDA`, `MENGGANTIKAN`, `BERKUAT KUASA`, `TARIKH KUAT KUASA`. Some PB labels end "(PEKELILING DIBATALKAN)".
- Grep the whole `text/` tree for the instrument number (e.g. `PK 2\.5|PK2\.5`, `AP 168\b`) to find **later** Surat Edaran or pindaan that amend, exempt or cancel particular paragraphs.
- If several versions exist, cite the one with the latest effective date and say what it replaced.
- State the status: *Berkuat kuasa sejak …* / *Dipinda oleh … (tarikh)* / *Perenggan X dibatalkan oleh …* / *Dibatalkan*.

**Freshness rule.** Check `downloaded_at` in `manifest.json`. If the snapshot is more than 30 days old, **or** the issue depends on a threshold or rate, check the portal's "Makluman Terkini" (https://ppp.treasury.gov.my/) and the MOF AP page for anything newer before finalising. Tell the user the snapshot date either way.

### Step 3: Official web sources (gaps and freshness)

1. https://ppp.treasury.gov.my/ (Pekeliling) and https://www.mof.gov.my/portal/ms/arahan-perbendaharaan (AP and its amendments).
2. ePerolehan (eP), for procurement system procedures.
3. Jabatan Akauntan Negara Malaysia (JANM), where it is the issuing authority.
4. The Attorney General's Chambers (lom.agc.gov.my), for the text of Akta Tatacara Kewangan 1957 when you need to quote the Act.
5. Only then a general web search, and only to find a link back to an official domain. Never cite a repost or blog.

## 3. Citation format and confidence labels

- **AP:** *AP 168 (Keizinan Membuat Perolehan), Arahan Perbendaharaan (Pindaan 2023), ms PDF 84*. If an amendment applies, add *"sebagaimana dipinda oleh Surat Edaran … bertarikh …"*.
- **Pekeliling:** *PK 2.9 Sebut Harga, perenggan 2.1(iii), ms 5*.
- Always give the `text/` path, PDF path and `source_url` in Rujukan. Page numbers are PDF page markers. The AP's printed page numbers differ (PDF page 84 is printed page 75), so say "ms PDF".

Every instrument cited MUST carry one label:

- **[DISAHKAN — Fail Tempatan]**: quoted directly from a `(text)` page of the local database.
- **[DISAHKAN — Fail Tempatan (OCR, disemak imej)]**: quoted from an `(ocr)` page, with key figures checked against the rendered image.
- **[DISAHKAN — Sumber Rasmi]**: read directly from an official web source. Cite the URL.
- **[BELUM DISAHKAN]**: from general knowledge, or an OCR figure not checked against the image. Flag it explicitly and tell the user to confirm it before citing in a signed paper. **Never present it with the same confidence as a DISAHKAN item.**

If nothing relevant can be found or verified, say so plainly. Never invent an AP number, circular number, paragraph or threshold to fill a gap.

## 4. What "suitable pathway" analysis looks like

1. **Isu/Keperluan**: a one-line restatement, plus the bidang involved.
2. **Asas Arahan Perbendaharaan**: the governing AP paragraph(s), each quoted, with status and label. This always comes first.
3. **Pekeliling dan tatacara pelaksanaan**: the Pekeliling, Surat Edaran and garis panduan that implement the AP, each with status, quoted clause, page and label.
4. **Pilihan laluan (2–4)**: genuinely distinct pathways, each with Kelebihan, Kekurangan/Risiko, the relevant cited threshold, and, where it departs from the rules, the AP 168 exception route (prior KSP approval).
5. **Cadangan**: the most defensible pathway and why, or an honest toss-up.
6. **Cadangan teks (optional)**: a ready-to-paste DASAR SEMASA or justification paragraph in house style (see `mof-house-style`). **Open with the AP basis, then the Pekeliling.**
7. **Rujukan**: every source checked, plus the database snapshot date.

This slots straight into the **DASAR SEMASA** and **ULASAN** sections of `kertas-pertimbangan-mof`, or the justification paragraph of `surat-mof` / `memo-mof`. The final delivery format is the user's call.

## 5. Files this workflow writes

Only `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md` (append-only), plus throwaway page images under `/tmp`. Never modify the PDFs, `text/`, `manifest.json`, or `tools/`.
