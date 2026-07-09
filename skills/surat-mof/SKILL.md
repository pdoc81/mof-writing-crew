---
name: surat-mof
description: Draft or review an official MOF/Perbendaharaan Malaysia letter (surat rasmi) to external parties, Ministers, Tan Sri/Datuk-level recipients, vendors, or other agencies — jemputan, pelepasan, lantikan, permohonan/sumbangan, pemakluman, arahan. Always load mof-house-style alongside this.
---

# Surat Rasmi MOF (Official External/Formal Letter)

Load `mof-house-style` first for fonts, honorifics, numbering, and fixed phrases. This skill covers the surat-specific skeleton — the key differences from a memo are the letterhead/address block, "Melalui" routing, and stricter honorific grading.

## Skeleton

```
[Letterhead zone — pre-printed letterhead OR inline crest image; leave top margin blank if pre-printed]

                                          MOF.100-XX/X/X (    )    [Bulan Tahun]   ← right-aligned, day may be blank in drafts

<RECIPIENT NAME/OFFICE — bold first line>
<address lines — plain>
<POSTCODE CITY — bold + underlined>

[(u.p.: <named attention, numbered if multiple>)]

[Melalui,
<Bold Name>
<Title>;
dan
<Bold Name>
<Title>.]

<Salutation matched to rank>,

TAJUK PENUH HURUF BESAR (bold, justified, no "PER:" prefix, no trailing full stop)

<Opening formula — graded by deference>          ← unnumbered para 1

2.  <news / latar belakang>              ← "Sukacita dimaklumkan..." / "Seperti tuan sedia maklum..."
3.  <the ask>                            ← "Sehubungan itu, ..."
[n.] <appreciation>

Sekian. / Sekian, terima kasih.

"MALAYSIA MADANI"                        ← adapt to current slogans; drop if not applicable
"BERKHIDMAT UNTUK NEGARA"

Saya yang menjalankan amanah,            ← "Yang benar," only for peer-level letters

(NAMA PENUH DALAM HURUF BESAR)
b.p. Ketua Setiausaha Perbendaharaan
<Bahagian>
Kementerian Kewangan Malaysia

Tel.: [no.]
E-mel: [nama@agensi.gov.my]

s.k.:
<abbreviations / named officers>
Fail
```

## Rules specific to surat

1. **Reference line has no "Ruj. Kami/Ruj. Tuan" labels** — bare file reference right-aligned, date on same or next line. Empty parentheses `(    )` for the serial. Classified letters append `(S)`.
2. **Recipient block**: first line bold (name or company), body plain, final postcode+city line **bold AND underlined**. Company recipients: company name in caps bold.
3. **Circulars**: replace the address block with `Semua Ketua Jabatan/Ketua Bahagian` (bold) or `SENARAI EDARAN SEPERTI DI LAMPIRAN A.` (bold caps), with the real list as a Lampiran headed `SENARAI EDARAN`.
4. **"Melalui,"** is used when routing upward through intermediate officers (e.g., writing to a Minister through club/committee officials) — bold each intermediate name, join multiple with `;` + `dan`.
5. **Salutation** must match the honorific ladder exactly (see `mof-house-style` §5) — never generic "Dear Sir".
6. **Opening formula** — pick by recipient rank:
   - Minister (YB): `Dengan segala hormat dan takzimnya saya merujuk kepada perkara di atas.`
   - Tan Sri/Dato': `Dengan segala hormatnya saya merujuk kepada perkara di atas.`
   - Standard: `Dengan hormatnya saya merujuk kepada perkara di atas.`
   - Senior officer to subordinate: `Saya merujuk kepada perkara di atas.`
7. **Numbering**: para 1 never numbered; `2.` onward manual tab or auto-list. Sub-items `(i)/(ii)` or `(a)/(b)`, left indent ~28–43pt.
8. **Sign-off**: `Saya yang menjalankan amanah,` for any b.p./on-behalf signature (this REPLACES the archaic "Saya yang menurut perintah" — avoid the old form unless your office specifically still uses it). Peer-level senior-to-senior letters use `Yang benar,` instead.
9. **Dual-hat signature titles** chain with `merangkap`: e.g. `Setiausaha Bahagian ... merangkap [jawatan kedua], b.p. Ketua Setiausaha Perbendaharaan`.
10. Lampiran sections get `LAMPIRAN A/B/C` in the Word page header, right-aligned; body events/costs go there, not in the letter body.

## Subtype fingerprints

- **Jemputan**: title starts `JEMPUTAN ...`; `Sukacita dimaklumkan... menjemput YB untuk merasmikan...`; aturcara/logistics block; hope-clause (`berharap dengan kesudian YB... akan memeriahkan lagi...`).
- **Pelepasan waktu bekerja**: addressed to `Semua Ketua Jabatan/Ketua Bahagian`; roster in Lampiran; bold the operative dates.
- **Lantikan**: `SENARAI EDARAN SEPERTI DI LAMPIRAN A.`; performative para: `...telah dinamakan dan dilantik sebagai...`.
- **Permohonan/sumbangan**: names an exact sum; policy-hook justification; heavy Lampiran (photos/quotes/costs); use `Melalui,` when routed to a Minister.
- **Pemakluman (vendor)**: cites the prior letter in the opener; payment table in-body; assurance close.
- **Arahan (from a senior officer)**: curt opener `Saya merujuk...`; first-person directive `saya mengarahkan...`; no honorific inflation.

## Checklist before finalizing
- [ ] Postcode+city line bold AND underlined
- [ ] Salutation matches recipient's exact honorific tier
- [ ] Opening formula matches deference level
- [ ] "Melalui," used correctly if routed through intermediaries
- [ ] Sekian rule respected
- [ ] "Saya yang menjalankan amanah," (not the archaic form) unless peer-to-peer
- [ ] s.k. ends with `Fail`
- [ ] Arial 12pt, A4, justified body, bold-underlined section headings where applicable
