---
name: memo-mof
description: Draft or review an internal MOF/Perbendaharaan Malaysia memo (running-letter style, e.g. memo kelulusan, pemakluman, jemputan, permohonan). Use when the user asks for a "memo" to KSP/TKSP/SBDSP/KS or similar internal addressee. Always load mof-house-style alongside this.
---

# Memo MOF (Internal Running-Letter Memo)

Load `mof-house-style` first for fonts, honorifics, numbering, and fixed phrases shared across all MOF documents. This skill covers the memo-specific skeleton.

## When to use a running memo vs a Kertas
A plain memo is for routine, low-friction items resolved in one paragraph flow: pemakluman, jemputan, small permohonan, single-tier kelulusan. If the matter needs multi-tier sign-off, cost tables, or policy justification, use `kertas-kelulusan-mof` or `kertas-pertimbangan-mof` instead.

## Skeleton

```
                    MEMO
              SEKSYEN PENTADBIRAN
       BAHAGIAN DASAR SARAAN DAN PENGURUSAN
            PERBENDAHARAAN MALAYSIA

MOF.100-XX/X/X JLDx (    )                    <Bulan Tahun>

<ADDRESSEE ABBREVIATION>              e.g. KS(PP) / TKSP(M) / Senarai edaran seperti di Lampiran A

Tuan,/Puan,/YBhg. Datin/Tuan/Puan,

TAJUK PENUH DALAM HURUF BESAR (bold)

Dengan hormatnya saya merujuk kepada perkara di atas.        ← never numbered

2.  <makluman / latar belakang>
3.  <butiran / isu / justifikasi>
4.  <permohonan / tindakan>              ← "Sehubungan itu, ..."
[n.] <penghargaan>

Sekian. / Sekian, terima kasih.

["BERKHIDMAT UNTUK NEGARA"]              ← bold, only for broadcast/formal memos
[Saya yang menjalankan amanah,]          ← only when b.p.

(NAMA PENUH DALAM HURUF BESAR)
KS(P) / post abbreviation

☎ : [no.]
✉ : [nama@agensi.gov.my]

s.k.:
<abbreviations>
Fail
```

## Rules specific to memos

1. **No "Daripada:" line** — sender identity appears only in the signature block.
2. **Salutation line is optional** for quick internal memos between equal-rank sections; keep it for anything going up to KS(Kew)/SBDSP/TKSP/KSP.
3. Numbering: para 1 unnumbered; `2.` onward, either manual `2.<tab>` or Word auto-list `start=2`. Sub-items `(a)(b)(c)` bold run-in, or `i. ii. iii.` roman auto-list.
4. Kelulusan-type memos (routine, single-tier) may embed a small `BIL | PERKARA` table body instead of running prose — see `kertas-kelulusan-mof` if it grows past one approver.
5. Choose the opener and closer from the fixed phrase inventory in `mof-house-style` — match register to the addressee's seniority.
6. Contact block Arial 8pt; s.k. Arial 8–10pt, `Fail` last.
7. A4, margins 2.54 cm (bottom margin may be trimmed to fit one page — this is an accepted house habit, not an error).

## Subtype fingerprints

- **Kelulusan**: closes with `pertimbangan dan kelulusan pihak puan dipohon bagi perkara seperti yang dinyatakan di perenggan [n].`
- **Pemakluman/edaran**: header may say `NOTA PEMAKLUMAN`; addressee is `Senarai edaran seperti di Lampiran A`; sign `b.p Ketua Setiausaha Perbendaharaan` + `Saya yang menjalankan amanah,` + slogan.
- **Jemputan**: `Sukacita dimaklumkan ...`; indented `Tarikh/Masa/Lokasi` block; `adalah dijemput hadir atau menghantar wakil`; contact-person paragraph.
- **Permohonan/pengecualian**: justification list (roman numerals); `memohon jasa baik dan pertimbangan`.

## Checklist before finalizing
- [ ] Reference line has blank `(    )` for registry serial number
- [ ] Para 1 unnumbered, numbering starts at 2
- [ ] Sekian rule respected (no double "terima kasih")
- [ ] Signature name bold in parentheses, ALL CAPS
- [ ] s.k. ends with `Fail`
- [ ] Arial throughout, justified body, A4
- [ ] No imperative requests — passive/hedged phrasing only
