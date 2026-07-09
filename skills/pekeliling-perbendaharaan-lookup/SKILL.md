---
name: pekeliling-perbendaharaan-lookup
description: Reference and verification rules for finding and citing Pekeliling Perbendaharaan (perolehan / wang awam-kewangan), Arahan Perbendaharaan (AP), and garis panduan when advising on the right regulatory pathway for a Kertas Pertimbangan, Kertas Kelulusan, Surat, or Memo. Used by the Ijah agent — load this before searching or citing any circular.
---

# Pekeliling Perbendaharaan Lookup — Sources & Citation Rules

**Scope covered:** Pekeliling Perbendaharaan (Perolehan), Pekeliling Perbendaharaan (Wang Awam/Kewangan), Arahan Perbendaharaan (AP), and internal garis panduan held locally. **Out of scope (do not cite):** Pekeliling Perkhidmatan / HR-only circulars — those belong to a separate skill, not this one.

**Setup required:** this skill assumes you (or the Ijah agent using it) have a local folder of saved Pekeliling/AP/garis panduan reference files, referred to below as `<PEKELILING_FOLDER>`. Replace that placeholder with your actual folder path wherever it appears. If you don't have such a folder yet, create one — start with whatever circulars you already reference most often in your own papers.

## 1. Source priority (check in this exact order)

### Step 0 — The decision log (ALWAYS check this first, before any PDF/web search)

File: `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md`

This is a running log of every issue previously researched — instruments found, pathways considered, and what was recommended/decided. It exists so the same research is never repeated from scratch and so recommendations stay consistent with precedent across papers over time. If this file doesn't exist yet, create it with two sections: an "Indeks Pantas" (quick-index) summary table and a "Log Terperinci" (detailed chronological log).

- **Read this file in full before touching any PDF or doing a web search.** Check the quick-index table and the detailed log for an entry matching or closely resembling the current issue.
- If a matching entry exists and nothing suggests it's stale (no newer superseding circular has since surfaced), reuse it — state explicitly that this answer comes from a prior logged session and cite the entry's date, rather than re-deriving it as if new.
- If the entry looks potentially outdated (e.g. it's more than a year old and the issue is procurement-threshold-sensitive, which changes periodically), do a quick re-verification pass before trusting it fully.
- If no matching entry exists, proceed to Step 1 and Step 2 as normal.
- **After finishing a research session** (whether reused-from-log or freshly researched), append exactly one new entry to the detailed log (never overwrite or reorder existing entries) and update the quick-index table. Keep the citation-confidence labels identical to what was given to the user — do not upgrade a `[BELUM DISAHKAN]` to `[DISAHKAN]` when logging it.

### Step 1 — Local repository (fastest, zero hallucination risk when found)

Primary folder: `<PEKELILING_FOLDER>/`

Re-index this folder with `ls`/`find` every session — don't assume the contents from a previous run are still complete, it will grow over time. A typical folder like this might hold: programme-specific garis panduan (PDFs from the issuing agency), ministerial letters clarifying financial procedures for a specific initiative, and internal guideline documents your own office has produced. Note honestly what's actually there — many personal Pekeliling folders are narrow (e.g. only covering one programme's guidance) and do NOT contain the full general Pekeliling Perbendaharaan / Arahan Perbendaharaan series. Don't assume coverage beyond what a `find`/`grep` actually returns.

Also worth checking (secondary, often scattered but real files sometimes exist):
- Any internal "garis panduan" or "senarai pekeliling" documents in your broader working-directory tree, even outside the dedicated reference folder.
- Individual project/procurement folders sometimes carry a cited circular as a Lampiran attachment to a specific past Kertas — search by keyword (`grep`/`find -iname`) across your wider working tree when the issue matches a domain you've handled before (procurement threshold, sponsorship, asset purchase).

**How to extract text for citation:** for PDFs, use `pdftotext` (via Bash) or the `pdf` skill; for .docx, use python-docx (python3 has it installed). Always quote the actual clause text you find — never paraphrase from memory and present it as a direct quote.

### Step 2 — Web search (for anything not found locally, or to check for a newer/superseding version)

Search official sources first, in this preference order:
1. The relevant national treasury/finance ministry's official portal and its Pekeliling Perbendaharaan / Arahan Perbendaharaan repository pages (for Malaysia: treasury.gov.my).
2. The national e-procurement portal for procurement-specific circulars and thresholds (for Malaysia: ePerolehan/eP).
3. The national accountant-general's department for wang awam/kewangan-related circulars where they are the issuing authority (for Malaysia: Jabatan Akauntan Negara Malaysia / JANM).
4. Only after the above: general web search, and only to locate a link back to an official source — never rely on a secondary blog/PDF-repost site as the citation itself without cross-checking against an official domain.

Treasury circulars are frequently renumbered/superseded — when found via web search, note the circular's **date and whether it says it supersedes/amends an earlier one**, and flag this to the user.

## 2. Citation confidence — mandatory labeling

Every circular/instrument cited MUST carry one of these labels:

- **[DISAHKAN — Fail Tempatan]** — text was directly read/quoted from a specific local file. Cite the file path.
- **[DISAHKAN — Sumber Rasmi]** — text was directly read/quoted from an official web source. Cite the URL and access context.
- **[BELUM DISAHKAN]** — recalled from general knowledge but NOT verified against an actual document this session. Must be explicitly flagged as such, with a recommendation that the user confirm the exact clause/number before citing it in a signed paper. **Never present a [BELUM DISAHKAN] item with the same confidence as a DISAHKAN one.**

If nothing relevant can be found or verified at all, say so plainly — do not invent a circular number to fill the gap. A missing citation is far less damaging than a wrong one in an official government paper.

## 3. What "suitable pathway" analysis looks like

For a given issue/problem/procurement strategy, structure the output as:

1. **Isu/Keperluan** — one-line restatement of what the user is trying to do.
2. **Instrumen berkaitan** — the circular(s)/AP/garis panduan that govern this, each with its citation-confidence label.
3. **Pilihan laluan (2–4 options)** — each a genuine distinct pathway (e.g. sebutharga vs rundingan terus vs perjanjian panel sedia ada), with:
   - **Kelebihan (Pros)**
   - **Kekurangan/Risiko (Cons)**
   - Threshold/nilai had yang releven, if known
4. **Cadangan (Recommendation)** — which pathway is most defensible given the instruments found, and why. If two are close, say so rather than forcing false confidence.
5. **Rujukan** — full list of sources checked (including local paths/URLs), so the user can independently verify.

This structure is designed to slot straight into the **DASAR SEMASA** and **ULASAN** sections of a `kertas-pertimbangan-mof` document, or into the justification paragraph of a `surat-mof`/`memo-mof` — but the analysis itself does not decide the final delivery format; that's a decision the user makes when invoking it.

## 4. The log file is the ONE file this workflow maintains directly

This workflow does not produce final deliverables (docx/HTML/PDF/PNG) on its own — that format decision belongs to whoever invoked it. The single exception is `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md`, which is read at the start and appended to at the end of every session, per Step 0 above. Do not write to any other file unless explicitly instructed.
