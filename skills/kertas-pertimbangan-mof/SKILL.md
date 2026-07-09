---
name: kertas-pertimbangan-mof
description: Draft or review a Kertas Pertimbangan (consideration paper) for MOF/Perbendaharaan Malaysia — policy-level, ministerial, or reputationally sensitive proposals (new programmes, policy changes, initiatives, extending facilities to new grades). Always load mof-house-style alongside this.
---

# Kertas Pertimbangan MOF (Policy Consideration Paper)

Load `mof-house-style` first. Structurally near-identical to `kertas-kelulusan-mof` (same memo-with-PARA/PERKARA-table architecture), but used for matters that need **policy justification** and often go to the most senior officer or a Minister rather than a routine approver. Loads more argumentation weight into Dasar Semasa and Ulasan.

## When Pertimbangan vs Kelulusan
- Use **Pertimbangan** when: the matter is a new policy/programme, extends an existing facility to a new group, involves ministerial-level approval, or is reputationally sensitive (e.g. optics of spending, precedent-setting).
- Use **Kelulusan** when: the matter is routine/precedented spend or participation, decided at division/club level with no new policy created.
- The document header is plain `MEMO` either way — the genre lives in the title line and content, not a special header.

## Page architecture (same shell as Kertas Kelulusan)

1. Letterhead (centered bold): `MEMO` / unit / `PERBENDAHARAAN MALAYSIA` (or a programme-specific unit name for special initiatives).
2. File ref + month/year, blank serial `(    )`.
3. Addressee ladder: `YBhg. Datuk KSP,` — `Melalui` — `YBhg. Datuk TKSP(M)`; OR for ministerial matters: `YB [Menteri]` → `Melalui,` → `YBhg. Datuk KSP,`.
4. Title, UPPERCASE bold: `PERMOHONAN PERTIMBANGAN ...`
5. **PARA | PERKARA table** — the mature 6-para skeleton (below).
6. Submission sentence, `Sekian, terima kasih.`, `"BERKHIDMAT UNTUK NEGARA"`.
7. Preparer signature block.
8. Decision pages per approver (DISOKONG → DILULUSKAN/DIPERSETUJUI chain).
9. QC strip (Disediakan/Disemak/Diperaku, with `Tel:` in the newest template).
10. Lampiran A/B/C.

## The mature 6-para skeleton (canonical heading names, UPPERCASE bold, sometimes underlined)

1. **TUJUAN**
2. **LATAR BELAKANG**
3. **DASAR SEMASA** — the section that distinguishes this from Kelulusan: state the existing policy/precedent baseline before proposing a change.
4. **ULASAN** (or "ULASAN [UNIT]") — the justification-building section, heaviest argumentation.
5. **IMPLIKASI KEWANGAN**
6. **SYOR** (or "SYOR PERBENDAHARAAN")

Order of 3–5 is flexible — lead with whichever (policy baseline vs cost) is the crux. Add ad-hoc sections when needed: `KONSEP DAN TEMA MAJLIS`, `KEPERLUAN PENUBUHAN PASUKAN`, `CADANGAN KEANGGOTAAN PASUKAN`, `SKOP PERMOHONAN`. For AI-assisted drafts, richer working sections are acceptable pre-review: `RISIKO DAN MITIGASI`, `PERKARA YANG PERLU DISAHKAN` — trim these back to the lean 6-para skeleton before final signed docx.

## Section-by-section drafting guide

**TUJUAN** — one sentence, front-loaded:
> *"Kertas ini disediakan bertujuan untuk memohon pertimbangan dan kelulusan YBhg. Datuk KSP bagi [tindakan] ... dengan menggunakan peruntukan sebanyak RM[jumlah]."*
Append a compliance clause where relevant, e.g.: *"... selaras dengan [Arahan/Pekeliling Perbendaharaan yang releven — verify with the pekeliling-perbendaharaan-lookup skill], tertakluk kepada peruntukan yang diluluskan serta tatacara perolehan Kerajaan yang berkuat kuasa."*

**LATAR BELAKANG** — trigger (policy launch/inviting letter/tradition) → prior decisions with exact file ref and date → event/programme particulars → pivot with `Sehubungan itu, ...`.

**DASAR SEMASA** — state the current rule/precedent verbatim, with citation to the actual instrument (do not guess a circular number — use `pekeliling-perbendaharaan-lookup` to find and verify it), or a named prior memo (`Merujuk kepada kelulusan terdahulu melalui memo: MOF.XXX-X/X/X bertarikh [tarikh] (Lampiran A)`).

**ULASAN** — this is where the case gets built. Common techniques:
- Benchmarking table (e.g. comparing practice across other ministries/agencies).
- Market-testing (`telah menjalankan kajian pasaran... sebut harga seperti di Lampiran A, B dan C`).
- Leadership-aspiration framing (`menyambut amanat YB Menteri Kewangan semasa pembentangan Bajet [tahun]`, `Menjunjung aspirasi YAB Perdana Menteri`).
- Welfare/motivation framing.
- **Arguing against the proposal is legitimate** when warranted — invoke fiscal prudence, optics, and value-for-money, then still present a neutral decision menu in SYOR rather than unilaterally killing it:
  > *"[Unit] berpandangan bahawa [cadangan] adalah kurang bersesuaian jika dilihat dari sudut fungsi dan peranan [agensi]... kurang selaras dengan prinsip perbelanjaan berhemat."*

**IMPLIKASI KEWANGAN** — headline figure; funding source named precisely (e.g. `Peruntukan Belanja B11 – [nama program], Butiran/Aktiviti [kod]`, `Maksud B10 – [nama] melalui OS yang bersesuaian`). For ceiling-based asks, use `anggaran kos siling` with the caveat: *"nilai sebenar tertakluk kepada ... kelulusan Pihak Berkuasa Melulus."* Include a budget-balance table when relevant (see below).

**SYOR** — mirror of Tujuan, decision-ready:
> *"Berdasarkan kepada ulasan di para 5, adalah disyorkan supaya YBhg. Datuk KSP menimbang dan meluluskan perkara-perkara berikut:"* — itemized (a)/(b)/(c), each ending in a performative clause, final item ending `..., diluluskan.`

## Financial table patterns

- Project costing (multi-line items): `BIL | PROJEK/PROGRAM | KERJA-KERJA TERLIBAT | PECAHAN KOS (RM) | KOS (RM)` — vertically merge project rows, aggregate `KOS`, itemize `PECAHAN KOS`.
- Ceiling/scope: `Bil. | Perkara | Anggaran Kos Siling (RM) | Catatan`.
- Budget-balance proof: `Peruntukan Asal | Peruntukan Semasa Sehingga [tarikh] (RM) | Peruntukan Yang Diperlukan (RM) | Baki (RM)`.
- Authority matrix: `Bil. | Had Nilai | Pihak Berkuasa Melulus`.
- Bold totals row always.

## Decision block — same mechanics as Kertas Kelulusan, but with escalation to Minister possible

- Intermediate: `Syor di para 6 DISOKONG / TIDAK DISOKONG` (senior deputy level).
- KSP-as-intermediate-to-Minister: `Syor di para 6 DIPERSETUJUI / TIDAK DIPERSETUJUI`.
- Final (KSP or Minister): `Syor di para 6 DILULUSKAN / TIDAK DILULUSKAN`.
- **For genuinely contested/ministerial items, use a structured decision menu with checkboxes:**
  ```
  Syor di para 6 DILULUSKAN / TIDAK DILULUSKAN seperti pilihan berikut:-

  ☐  ... ditolak dan dimaklumkan kepada [pihak berkenaan]; atau
  ☐  ... dipersetujui dan dimaklumkan kepada [pihak berkenaan].
  ```
  Lay this out as a 3-column table so the Minister/approver can tick a box — this is the preferred device when presenting a genuine either/or to a senior decision-maker.

## Drafting-process note

Drafting in Markdown first — mirroring the exact PARA/PERKARA structure and phrase inventory, with working-draft metadata (`Status: Draf kerja untuk semakan dalaman... tertakluk kepada pengesahan...`), explicit placeholders (`[NAMA KSP]`, `[Diisi oleh Bahagian Kewangan]`), source-file audit trails per Lampiran, and double-counting controls (`direkodkan untuk makluman tetapi tidak dicampur... bagi mengelakkan pertindihan angka`) — before converting to the lean signed .docx works well in practice. When asked to draft a Kertas Pertimbangan, producing this richer Markdown draft FIRST (with placeholders flagged) is a good default.

## Checklist before finalizing
- [ ] DASAR SEMASA section states the policy baseline with a verified citation (not guessed)
- [ ] ULASAN carries the real argumentative weight (benchmarking/market-testing/aspiration framing)
- [ ] IMPLIKASI KEWANGAN names the exact vot/funding code and includes a budget-balance table if relevant
- [ ] SYOR is itemized and decision-ready; use a checkbox decision menu for contested/ministerial items
- [ ] Decision-page verb tier matches approver level (DISOKONG → DIPERSETUJUI/DILULUSKAN)
- [ ] Placeholders (`[...]`) flagged clearly if this is a working draft
- [ ] Compliance boilerplate included where the matter involves procurement/spend, with the underlying circular actually verified (see `pekeliling-perbendaharaan-lookup`)
