# MOF Writing Crew

Claude Code (and Codex) agents and skills for drafting and reviewing official Malaysian government correspondence — Memo, Surat Rasmi, Kertas Kelulusan, Kertas Pertimbangan — in the house style of Perbendaharaan Malaysia (Ministry of Finance), plus a regulatory-pathway advisor backed by a local, searchable database of the Arahan Perbendaharaan and every current Pekeliling Perbendaharaan ([ready-made text database](https://github.com/pdoc81/pekeliling-perbendaharaan-text)).

Reverse-engineered from real internal correspondence patterns (2018–2026): fonts, spacing, honorifics, fixed Malay phrases, numbering conventions, decision-block mechanics, and argumentation strategy — not a generic template, but what these documents actually look like in practice.

## What's inside

| | Name | What it does |
|---|---|---|
| Skill | `mof-house-style` | Shared house style — fonts, honorifics, fixed phrases, numbering, RM formatting. Load this for anything. |
| Skill | `memo-mof` | Internal running-letter memo structure |
| Skill | `surat-mof` | Official external letter structure (address blocks, "Melalui" routing, honorific grading) |
| Skill | `kertas-kelulusan-mof` | Approval-paper structure — PARA/PERKARA table, multi-tier DISOKONG→DILULUSKAN decision chain |
| Skill | `kertas-pertimbangan-mof` | Policy consideration-paper structure — the mature 6-para skeleton (adds DASAR SEMASA + ULASAN) |
| Skill | `pekeliling-perbendaharaan-lookup` | Database layout, search method, in-force status checks, source priority and citation-confidence rules for finding the right circular |
| Agent | **Aisyah** | Reviews a draft against the house style — formatting, font, spacing, tables, honorifics, language |
| Agent | **Ijah** | Starts from the governing Arahan Perbendaharaan (AP), then finds the Pekeliling Perbendaharaan (all 7 bidang: PB, PK, WP, AM, PS, PA, LB) that implement it, checks it is still in force, quotes the clause with page citation, and proposes pathway options with pros/cons |
| Data | [pekeliling-perbendaharaan-text](https://github.com/pdoc81/pekeliling-perbendaharaan-text) | Ready-made text database Ijah searches (AP + 267 current circulars, page-cited) |
| Tools | `tools/` | Free, fully local pipeline that mirrors the Arahan Perbendaharaan (mof.gov.my) and the Portal Pekeliling Perbendaharaan and extracts full text (pdftotext + PaddleOCR for scanned pages) |

## Naming convention: why "Aisyah" and "Ijah"?

Every agent here is named after a real personality trait, not a generic function name like `formatter-agent` or `compliance-checker`.

- **Aisyah** is named after the person who always corrects the author's everything. Now she can corrects the documents' formatting digitally.
- **Ijah** is named after a relative who always asking about which Pekeliling applies to something. This agent is a revenge: now she does that job digitally instead.

If you extend this toolkit, keep the tradition — name your agent after a real trait or person in your life (with their blessing), and note why in your own fork's README. It keeps agents feeling like colleagues you're delegating to, not tools you're invoking.

## Installation

```bash
git clone https://github.com/pdoc81/mof-writing-crew.git
cp mof-writing-crew/agents/*.md ~/.claude/agents/
cp -r mof-writing-crew/skills/* ~/.claude/skills/
```

Claude Code loads skills automatically when relevant (e.g. asking it to "draft a kertas pertimbangan for..."), and agents are invoked by name ("ask aisyah to review this draft", "ijah, what pekeliling applies to...").

### Codex

Codex reads skills from `.agents/skills/` and custom agents from `.codex/agents/*.toml`. The agent prompts point at `~/.claude/skills/`, so keep the skills there and link them:

```bash
mkdir -p ~/.claude/skills ~/.agents ~/.codex/agents
cp -r mof-writing-crew/skills/* ~/.claude/skills/
ln -sfn ~/.claude/skills ~/.agents/skills
cp mof-writing-crew/codex/agents/*.toml ~/.codex/agents/
```

`codex/agents/*.toml` are generated from `agents/*.md`. If you edit an agent, regenerate its TOML file too.

### Required one-time setup for Ijah: get the Pekeliling database

Ijah searches a local database: the full text of the Arahan Perbendaharaan and every **current** Pekeliling Perbendaharaan. A ready-made copy is published at **[pdoc81/pekeliling-perbendaharaan-text](https://github.com/pdoc81/pekeliling-perbendaharaan-text)**, so nothing needs to be downloaded or OCR'd.

1. Clone the text database anywhere you like, e.g. `~/Pekeliling`:
   ```bash
   git clone https://github.com/pdoc81/pekeliling-perbendaharaan-text.git ~/Pekeliling
   ```
2. Ijah and its skill use a placeholder, `<PEKELILING_FOLDER>`, for that folder. Replace it with the absolute path:
   ```bash
   P="$HOME/Pekeliling"
   sed -i "s#<PEKELILING_FOLDER>#$P#g" ~/.claude/agents/ijah.md ~/.claude/skills/pekeliling-perbendaharaan-lookup/SKILL.md
   sed -i "s#<PEKELILING_FOLDER>#$P#g" ~/.codex/agents/ijah.toml   # Codex only
   ```
3. Run `cd ~/Pekeliling && git pull` from time to time to get newer snapshots. Ijah tells you the snapshot date in every answer, and checks the portal's Makluman Terkini when the snapshot is more than 30 days old.
4. Ijah creates and maintains a running decision log at `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md`. Every issue it researches is logged there so future sessions don't repeat the same research and stay consistent with precedent.

The text clone has no PDFs. When Ijah needs to check a figure from a scanned (OCR) page against the original image, it downloads that one official PDF from the `source_url` in the file's front matter.

**The decision log will contain your own real working decisions. Keep it private.** The text repo's `.gitignore` ignores everything except `text/`, `manifest.json` and its README, so the log can't be committed by accident, and this repo's `.gitignore` excludes it too.

#### Optional: build the database yourself

To rebuild from the official sources (or to keep the PDFs locally), follow [`tools/README.md`](tools/README.md). It downloads the AP from mof.gov.my and the current circulars from https://ppp.treasury.gov.my/, then extracts every page with pdftotext + PaddleOCR. It's free and runs entirely on your own machine, but OCR takes about an hour on a 20-core CPU. The result has the same layout as the text repo.

**What Ijah does with the database:** reasons top-down (Akta Tatacara Kewangan 1957 → **Arahan Perbendaharaan first** → Pekeliling Perbendaharaan → Surat Edaran). It always identifies and quotes the governing AP paragraph before any Pekeliling, and checks the AP amendment notices. It searches the full text (not filenames) across every bidang the issue touches, and reads the whole page before quoting. It checks each instrument's status (berkuat kuasa / dipinda / dibatalkan) against later Surat Edaran. When a key figure comes from a scanned page, it renders that page and checks the number against the image. Citations take the form *PK 2.5 Kontrak Pusat, perenggan 4.2, ms 6*. Since the AP isn't on the portal, `tools/scripts/add_ap.py` fetches it from mof.gov.my.

## ⚠️ Disclaimer

- This is an **unofficial, personal tooling project**, reverse-engineered from observed document patterns. It is **not affiliated with, endorsed by, or representative of the Ministry of Finance Malaysia** or any government agency.
- House-style conventions (fonts, phrases, slogans, honorific ladders) reflect one office's practice at one point in time. Government templates, slogans, and circular numbers change — verify against your own office's current template and current official sources before using any output in a real submission.
- **Ijah does not guarantee regulatory accuracy.** It labels every citation as `[DISAHKAN — Fail Tempatan]`, `[DISAHKAN — Sumber Rasmi]`, or `[BELUM DISAHKAN]` specifically because circular numbers and thresholds are easy to get wrong and costly to get wrong in a signed government paper. Always independently verify a `[BELUM DISAHKAN]` citation, and spot-check `[DISAHKAN]` ones too before relying on them for anything consequential.
- No real names, file reference numbers, or specific matters from the original source documents are included in this repo — all examples are genericized/fictional templates.

## License

MIT — see [LICENSE](LICENSE).
