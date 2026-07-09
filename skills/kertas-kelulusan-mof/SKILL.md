---
name: kertas-kelulusan-mof
description: Draft or review a Kertas Kelulusan (approval paper) for MOF/Perbendaharaan Malaysia or Kelab Perbendaharaan — routine/precedented approval requests (sports contingent participation, event costs, incentive policy, procurement approvals). Always load mof-house-style alongside this.
---

# Kertas Kelulusan MOF (Approval Paper)

Load `mof-house-style` first. A Kertas Kelulusan is a **memo whose body is a PARA | PERKARA table**, ending in a multi-tier sign-off chain culminating in a DILULUSKAN/TIDAK DILULUSKAN decision. Use for routine or precedented matters (vs `kertas-pertimbangan-mof` for policy-level/contested matters — see that skill for the distinction).

## Page architecture

1. Letterhead block (centered bold): `MEMO` / issuing unit, OR `MEMO KELULUSAN` for club-level approvals.
2. File reference + month/year line, blank serial `(    )`.
3. Addressee ladder: `YBhg. [Tan Sri/Datuk/Dato'] [Approver],` then `Melalui` if routed through an intermediate.
4. Title, full UPPERCASE bold: `PERMOHONAN KELULUSAN ...`
5. **The PARA | PERKARA table** — this is the entire substance (see below).
6. Submission sentence + `Sekian, terima kasih.` + `"BERKHIDMAT UNTUK NEGARA"` (bold, centered).
7. Preparer signature block: dotted line, `( NAMA BOLD )`, post, `Tarikh :`.
8. **One decision page per approver in the chain** (page-break separated) — see Decision Block below.
9. QC strip: `Disediakan oleh / Disemak oleh / Diperaku(kan) oleh` table, dotted lines, `Nama:`, `Jawatan:`, `Tarikh:`.
10. Lampiran (A, B, C...) for cost detail, name lists, terms of reference.

## The PARA | PERKARA table

Two columns. Left = paragraph number (`1.`, `2.` ...). Right = bold section heading + numbered content (Word multilevel: `2.1` → `(a)(b)(c)` → `i.ii.iii.`).

Canonical section order (Kelab/routine variant):
1. **Tujuan**
2. **Latar Belakang**
3. **Ulasan** *(optional — omit for very routine items)*
4. **Implikasi Kewangan** *(or "Implikasi Kos")*
5. **Ulasan dan Syor** / **Syor**

## Section-by-section drafting guide

**Tujuan** — one sentence, front-load everything: decision-maker + action + amount + date + funding vehicle.
> *"Kertas ini disediakan bertujuan untuk memohon pertimbangan dan kelulusan YBhg. Dato' YDP Kelab Perbendaharaan Putrajaya bagi menganjurkan [Nama Program/Majlis] pada [tarikh] dengan menggunakan peruntukan sebanyak RM[jumlah]."*

**Latar Belakang** — narrative escalation: (i) context/trigger, (ii) prior decisions/precedent with file ref, (iii) event particulars as a bold `Tarikh:/Masa:/Lokasi:` mini-block, (iv) exhaustive enumerated lists (agencies, eligible officers, items), (v) pivot with `Sehubungan itu, ...`.

**Ulasan** (if present) — `[Unit] berpandangan permohonan ini boleh dipertimbangkan berdasarkan justifikasi berikut:` then enumerate. Techniques: market-testing (`telah menjalankan kajian pasaran... tiga (3) [pembekal/penganjur]... sebut harga seperti di Lampiran A, B dan C`), benchmarking, welfare framing (`sebagai tanda sokongan, motivasi dan galakan semangat`).

**Implikasi Kewangan** — headline figure repeated; detail pushed to Lampiran (`dengan pecahan kos seperti di Lampiran C`); name the funding source explicitly (e.g. `peruntukan Kelab Perbendaharaan`, `Akaun Amanah Sumber Khas`). Use the financial table patterns below.

**Syor** — mirrors Tujuan, decision-ready:
> *"Berdasarkan kepada ulasan di para [n], adalah disyorkan supaya [Approver] menimbang dan meluluskan perkara-perkara berikut:"* then lettered items each ending `..., diluluskan.`

## Financial table patterns (verbatim column headers)

- Event costing: `BIL | ITEM | KOS/UNIT | KUANTITI | HARI | JUMLAH`
- Alt: `BIL | PERKARA | KUANTITI | HARGA/UNIT | JUMLAH`
- Incentives: `BIL | ACARA SUKAN | BIL ATLET* | KOS INSENTIF (RM)` with footnotes `* kelayakan... ** andaian...`
- **Totals row always present**, bold, `JUMLAH` or `JUMLAH KESELURUHAN`.
- RM format: `RM175,000.00` in prose; `(RM)` in header + bare `175,000.00` in cells.

## Decision block (repeat per approver, page-break separated)

```
MOF.100-XX/X/X JLDx (    )                              <Bulan Tahun>     ← ref repeated, 9-10.5pt
<TITLE REPEATED, bold caps>
Syor di para [n] DISOKONG / TIDAK DISOKONG                                ← intermediate approver
Ulasan:
______________________________________________________

                                        ....................
                                        ( NAMA BOLD )
                                                 <Post>
                                        Tarikh :          / <tahun>
```

- Intermediate tier verbs: `DISOKONG/TIDAK DISOKONG` (senior-officer level) or `DIPERAKU/TIDAK DIPERAKU` / `DIPERAKUKAN/TIDAK DIPERAKUKAN` (club route) or `BERSETUJU/TIDAK BERSETUJU`.
- Final tier: `DILULUSKAN / TIDAK DILULUSKAN` (top approver).
- For genuinely contested items, offer a **numbered decision menu** instead of a binary:
  > `Keputusan:` `1. DILULUSKAN pemberian insentif kemenangan RM[jumlah] ...` `2. TIDAK DILULUSKAN ...`
- Old/club-only alternative: centered `Kelulusan Yang Dipertua Kelab Perbendaharaan:` / `LULUS / TIDAK LULUS`.

## Checklist before finalizing
- [ ] Body is a PARA|PERKARA (or BIL|PERKARA) table, not running prose
- [ ] Tujuan sentence contains decision-maker, action, amount, date, funding source
- [ ] Financial table has a bold totals row and named funding source
- [ ] Every approver in the chain has their own decision page with correct verb tier
- [ ] Submission line: `Dikemukakan syor [Unit] di para [n] untuk pertimbangan dan persetujuan [Approver] jua.`
- [ ] QC strip (Disediakan/Disemak/Diperaku) present
- [ ] Detail tables offloaded to Lampiran, referenced `(Lampiran A)`
- [ ] "BERKHIDMAT UNTUK NEGARA" before signature
