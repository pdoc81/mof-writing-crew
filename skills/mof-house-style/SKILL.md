---
name: mof-house-style
description: Shared house style for official Perbendaharaan Malaysia (MOF) documents — fonts, spacing, honorifics, fixed Malay phrases, numbering, RM formatting, signature blocks, s.k., Lampiran conventions. Load this whenever drafting or reviewing any memo, surat rasmi, kertas kelulusan, kertas pertimbangan, minit, or laporan for a Malaysian government office.
---

# MOF/BDSP House Style (Gaya Rumah Perbendaharaan)

Reverse-engineered from real internal Malaysian government correspondence (2018–2026), originally from Seksyen Pentadbiran, Bahagian Dasar Saraan dan Pengurusan (BDSP), Perbendaharaan Malaysia. These conventions are broadly representative of formal Bahasa Melayu government correspondence style — treat them as strong defaults, and adjust for your own office's specific template where it differs.

## 1. Page & typography

| Property | Value |
|---|---|
| Paper | A4 portrait (21.0 × 29.7 cm) — never US Letter |
| Margins | 2.54 cm all round (letters on pre-printed letterhead: top 4.05 cm) |
| Font | **Arial everywhere**, body **12 pt** (even if the Word style says Times New Roman — override every run) |
| Contact/s.k. blocks | Arial 8–10 pt |
| Alignment | Body **justified**; letterhead & titles centered; ref/date right or tabbed right |
| Line spacing | Single or 1.15; space before/after 0 — use **blank paragraphs** as separators, not space-after |
| Emphasis | **Bold** for: tajuk, section headings, names, verdict words, operative dates & RM amounts mid-sentence. Underline sparingly (postcode-city line, routing sentences). *Italics* ONLY for foreign terms (*value for money*, *event organizer*). |

## 2. Reference line & date

- Format: `MOF.100-XX/X/X JLDx (        )` + tab(s) + `April 2026` on ONE line — file ref left, date right.
- **Serial number in parentheses is ALWAYS left blank** — the registry fills it by hand.
- **In drafts, omit the day**: write `  April 2026` not `21 April 2026` — the day is written by hand at signing. Malay month names always (Januari … Disember).
- Never type the labels "Rujukan:" or "Tarikh:". Incoming letters are cited in-body: `surat KK.XXX-X/X/X (XX) bertarikh [tarikh]`.

## 3. Numbering

- **Paragraph 1 (the opener) is NEVER numbered. Numbering starts at `2.`** typed as `2.` + tab (or Word auto-list with start=2, hanging indent ~0.64 cm).
- Sub-items: `2.1, 2.2` → `(a) (b) (c)` → `i. ii. iii.` Sub-heading letters may carry bold run-in headings.
- Cross-reference paragraphs as `di perenggan 3` or `di para 6`; attachments as `seperti di **Lampiran A**`.

## 4. Numbers, money, dates

- Quantities doubled: `dua (2) orang pegawai`, `tiga (3) fasa`, `seratus empat (104) unit`.
- Money: `RM175,000.00` (RM prefix, thousands commas, 2 decimals, no space). In tables, move RM to the header `(RM)` and cells hold `50,000.00`. Totals row bold: `JUMLAH KESELURUHAN`. Qualifiers: `(tidak termasuk SST)`.
- Event particulars as an indented label block (~2.5 cm left indent), NOT a table:
  ```
  Tarikh  : 15 Januari 2026 (Khamis)
  Masa    : 9.00 pagi
  Lokasi  : [Lokasi]
  ```

## 5. Honorifics (never "anda" — always third-person honorific)

Ladder: `YAB` > `YB` (Menteri; spell full style in address: `YB Senator Tengku Datuk Seri Utama …`) > `YBhg. Tan Sri` > `YBhg. Datuk Seri / Dato' Seri` > `YBhg. Datuk / Dato' / Datin` > `YBrs.` (senior officers without titles) > `Tuan / Puan / Encik / Cik`.

- In-body second person: `pihak puan`, `tuan/puan`, `YBhg. Datuk Seri` — repeat the honorific instead of pronouns.
- Circular cascade, verbatim every time: `YBhg. Tan Sri/Datuk/Dato'/Datin/Dr./Tuan/Puan` (drop the Tan Sri tier if none in audience).

### Post abbreviations (MOF-internal — adapt to your own office's structure)
| Abbrev | Post |
|---|---|
| KSP | Ketua Setiausaha Perbendaharaan (`YBhg. Datuk Seri KSP`) |
| TKSP(M)/(D)/(I)/(P) | Timbalan KSP (Pengurusan/Dasar/Antarabangsa/…) |
| SBDSP | Setiausaha Bahagian, Bahagian Dasar Saraan dan Pengurusan |
| TSBDSP(O)/(M) | Timbalan Setiausaha BDSP |
| KS(P), KS(Kew), KS(PSM), KS(PP), KS(S) | Ketua Seksyen (Pentadbiran / Kewangan / Pengurusan Sumber Manusia / …) |
| PSU(P) | Penolong Setiausaha (Pentadbiran) |
| SBSKK, SBPK, SBFE, SBPA … | Setiausaha Bahagian of other divisions |
| YBMK / YB MKII | YB Menteri Kewangan / Menteri Kewangan II |

## 6. Fixed phrase inventory (use verbatim)

**Openers (para 1, graded by deference):**
- To YB Menteri: `Dengan segala hormat dan takzimnya saya merujuk kepada perkara di atas.`
- To Tan Sri/Datuk: `Dengan segala hormatnya saya merujuk kepada perkara di atas.`
- Standard: `Dengan hormatnya saya merujuk kepada perkara di atas.`
- On instruction (junior officer): `Dengan hormatnya saya diarah merujuk kepada perkara di atas.`
- Impersonal circular: `Dengan hormatnya merujuk kepada perkara di atas.` (drops "saya")
- Citing an antecedent: `… dan surat MOF.XXX-X/X/X (X) bertarikh [tarikh] adalah berkaitan.` (tag with **adalah berkaitan**)

**Informing (para 2):** `Untuk makluman puan, …` / `Sukacita dimaklumkan bahawa …` / `Sebagaimana pihak puan sedia maklum, …` / `Adalah dimaklumkan bahawa …` / `Bersama-sama ini dikemukakan … seperti di Lampiran A.`

**Pivot to the ask:** **`Sehubungan itu, …`** (the signature connective — use it). Others: `Oleh yang demikian, …`, `Walau bagaimanapun, …`, `Justeru, …`, `Mengambil kira perkara di atas, …`

**Requests (always passive, never imperative):**
- `kerjasama puan adalah dipohon untuk …`
- `Seksyen ini memohon jasa baik dan pertimbangan daripada pihak puan untuk …`
- `pertimbangan dan kelulusan pihak puan dipohon bagi perkara seperti yang dinyatakan di perenggan 5.`
- `tuan/puan adalah dijemput hadir atau menghantar wakil …`
- Hedged opinion: `seksyen ini berpandangan agar …` / `BDSP mencadangkan pilihan seperti berikut:`

**Contact clause:** `Sekiranya terdapat sebarang pertanyaan lanjut berkaitan perkara ini, pihak tuan/puan boleh berhubung dengan [Nama] di talian [no.].`

**Appreciation (penultimate):** `Perhatian dan kerjasama puan dalam perkara ini didahului dengan ucapan terima kasih.` / `Kerjasama daripada pihak tuan/puan adalah amat dihargai dan didahului dengan ucapan terima kasih.`

**THE SEKIAN RULE:** if the appreciation sentence already ends with `…ucapan terima kasih.`, close with bare **`Sekian.`**; otherwise **`Sekian, terima kasih.`** Never both.

## 7. Slogans & sign-off (bottom block, in order)

1. Slogans — bold, curly double quotes, each on its own line, newest on top. Adapt these to whatever the current national/departmental slogans are (they change with administrations — the examples below were current as of this skill's authoring):
   - `"MALAYSIA MADANI"` then `"BERKHIDMAT UNTUK NEGARA"`
   - Sports/club documents: `"MAJULAH SUKAN UNTUK NEGARA"`
2. `Saya yang menjalankan amanah,` — whenever signing b.p./on behalf. (Peer-to-peer at senior level: `Yang benar,`. Avoid the archaic "Saya yang menurut perintah" unless your office specifically still uses it.)
3. 3–4 blank lines, then **`(NAMA PENUH DALAM HURUF BESAR)`** — bold, in parentheses.
4. Title lines, e.g. `b.p. Ketua Setiausaha Perbendaharaan` / `[Bahagian]` / `Kementerian Kewangan Malaysia`. Dual hats chain with `merangkap`.
5. Contact block Arial 8 pt: `Tel.: [no.]` / `E-mel: [nama@agensi.gov.my]`.

## 8. s.k. (salinan kepada)

Label `s.k.:` then internal abbreviations one per line (`KSP`, `TKSP(M)`, `SBDSP`, …), smaller font (9–11 pt). **`Fail` is always the last entry.** Deferential annotation allowed: `KSP - untuk makluman YBhg. Tan Sri jua.`

## 9. Lampiran

- Each Lampiran is a new Word section; `LAMPIRAN A` right-aligned bold, ideally in the page header of that section; centered bold-underlined title below.
- Every cited instrument (memo terdahulu, surat, pekeliling) should be attached and referenced `(Lampiran A)`.
- Detail tables (costing, name lists, senarai edaran) go to Lampiran, keeping the body lean.

## 10. Policy citations

- Cite the operative instrument precisely and quote it verbatim when it drives the decision — e.g. `Arahan Perbendaharaan 168 (AP 168)`.
- Pekeliling Perbendaharaan by code, cited with function (e.g. `PP WP2.2`, `PK 2.10`) — see the `pekeliling-perbendaharaan-lookup` skill for how to find and verify the actual applicable circular rather than guessing a number.
- Funding always named precisely: `Maksud B10 – Perbendaharaan`, `Butiran/Aktiviti [kod]`, OS codes, trust account name, or club/vote source.
- Compliance boilerplate: `tertakluk kepada peruntukan yang diluluskan serta tatacara perolehan Kerajaan yang berkuat kuasa`.

## 11. Known typos to AVOID reproducing (they persist in old templates people copy from)

`SEKYEN` → SEKSYEN; `Perbendaharan` → Perbendaharaan; `Walaubagaimanapun` → Walau bagaimanapun; `dikalangan` → dalam kalangan; `pemantaua` → pemantauan; `korperat` → korporat.

## 12. Sibling skills

Document-type specifics live in: `memo-mof`, `surat-mof`, `kertas-kelulusan-mof`, `kertas-pertimbangan-mof` (same skills directory). For finding and citing the actual regulatory instrument behind a decision, see `pekeliling-perbendaharaan-lookup`. When producing the final .docx, apply the specs above (a `docx`-generation skill/tool is assumed).
