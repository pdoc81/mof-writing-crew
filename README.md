# MOF Writing Crew

Claude Code (and Codex) agents and skills for drafting and reviewing official Malaysian government correspondence — Memo, Surat Rasmi, Kertas Kelulusan, Kertas Pertimbangan — in the house style of Perbendaharaan Malaysia (Ministry of Finance), plus a regulatory-pathway advisor backed by a local, searchable database of every current Pekeliling Perbendaharaan.

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
| Agent | **Ijah** | Finds which Pekeliling Perbendaharaan (all 7 bidang: PB, PK, WP, AM, PS, PA, LB) / Arahan Perbendaharaan applies to an issue, checks it is still in force, quotes the clause with page citation, and proposes pathway options with pros/cons |
| Tools | `tools/` | Free, fully local pipeline that mirrors the Portal Pekeliling Perbendaharaan and extracts full text (pdftotext + PaddleOCR for scanned pages) |

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

### Required one-time setup for Ijah: build the Pekeliling database

Ijah and its skill (`pekeliling-perbendaharaan-lookup`) use a placeholder, `<PEKELILING_FOLDER>`. That is the local folder holding the Pekeliling database. Before first use:

1. Choose a folder, e.g. `~/Pekeliling`. Copy `tools/` into it and build the database by following [`tools/README.md`](tools/README.md). This mirrors the **current** circulars from https://ppp.treasury.gov.my/, arranged by bidang and topic as on the portal, and extracts the full text of every page into `text/*.md` with page markers. It runs entirely on your own machine, with no paid OCR service.
2. Find-and-replace `<PEKELILING_FOLDER>` with that folder's absolute path in `~/.claude/agents/ijah.md` and `~/.claude/skills/pekeliling-perbendaharaan-lookup/SKILL.md` (for Codex, also `~/.codex/agents/ijah.toml`).
3. Re-run `download.py` → `text_audit.py` → `extract.py` from time to time to pick up new or amended circulars. Unchanged files are skipped. Ijah tells you the database snapshot date in every answer, and checks the portal's Makluman Terkini when the snapshot is more than 30 days old.
4. Ijah will create and maintain a running decision log at `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md` — every issue it researches gets logged there so future sessions don't repeat the same research and stay consistent with precedent.

**This log file will contain your own real working decisions — keep it in a private location, not a public repo.** The repo's `.gitignore` excludes the database, extracted text and log in case you build them inside a clone.

**What Ijah does with the database:** searches the full text (not filenames) across every bidang the issue touches, and reads the whole page before quoting. It checks each instrument's status (berkuat kuasa / dipinda / dibatalkan) against later Surat Edaran. When a key figure comes from a scanned page, it renders that page and checks the number against the image. Citations take the form *PK 2.5 Kontrak Pusat, perenggan 4.2, ms 6*. Arahan Perbendaharaan itself isn't on the portal, so it is looked up from official web sources.

## ⚠️ Disclaimer

- This is an **unofficial, personal tooling project**, reverse-engineered from observed document patterns. It is **not affiliated with, endorsed by, or representative of the Ministry of Finance Malaysia** or any government agency.
- House-style conventions (fonts, phrases, slogans, honorific ladders) reflect one office's practice at one point in time. Government templates, slogans, and circular numbers change — verify against your own office's current template and current official sources before using any output in a real submission.
- **Ijah does not guarantee regulatory accuracy.** It labels every citation as `[DISAHKAN — Fail Tempatan]`, `[DISAHKAN — Sumber Rasmi]`, or `[BELUM DISAHKAN]` specifically because circular numbers and thresholds are easy to get wrong and costly to get wrong in a signed government paper. Always independently verify a `[BELUM DISAHKAN]` citation, and spot-check `[DISAHKAN]` ones too before relying on them for anything consequential.
- No real names, file reference numbers, or specific matters from the original source documents are included in this repo — all examples are genericized/fictional templates.

## License

MIT — see [LICENSE](LICENSE).
