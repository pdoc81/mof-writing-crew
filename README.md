# MOF Writing Crew

Claude Code agents and skills for drafting and reviewing official Malaysian government correspondence — Memo, Surat Rasmi, Kertas Kelulusan, Kertas Pertimbangan — in the house style of Perbendaharaan Malaysia (Ministry of Finance), plus a regulatory-pathway advisor for Pekeliling Perbendaharaan / Arahan Perbendaharaan lookups.

Reverse-engineered from real internal correspondence patterns (2018–2026): fonts, spacing, honorifics, fixed Malay phrases, numbering conventions, decision-block mechanics, and argumentation strategy — not a generic template, but what these documents actually look like in practice.

## What's inside

| | Name | What it does |
|---|---|---|
| Skill | `mof-house-style` | Shared house style — fonts, honorifics, fixed phrases, numbering, RM formatting. Load this for anything. |
| Skill | `memo-mof` | Internal running-letter memo structure |
| Skill | `surat-mof` | Official external letter structure (address blocks, "Melalui" routing, honorific grading) |
| Skill | `kertas-kelulusan-mof` | Approval-paper structure — PARA/PERKARA table, multi-tier DISOKONG→DILULUSKAN decision chain |
| Skill | `kertas-pertimbangan-mof` | Policy consideration-paper structure — the mature 6-para skeleton (adds DASAR SEMASA + ULASAN) |
| Skill | `pekeliling-perbendaharaan-lookup` | Source-priority and citation-confidence rules for finding the right circular |
| Agent | **Aisyah** | Reviews a draft against the house style — formatting, font, spacing, tables, honorifics, language |
| Agent | **Ijah** | Finds which Pekeliling/Arahan Perbendaharaan applies to a given issue and proposes pathway options with pros/cons |

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

### Required one-time setup for Ijah

Ijah and its skill (`pekeliling-perbendaharaan-lookup`) reference a placeholder `<PEKELILING_FOLDER>` — the local folder where you keep saved Pekeliling Perbendaharaan / Arahan Perbendaharaan / garis panduan reference files. Before first use:

1. Create (or point to) a folder where you keep these reference documents.
2. Find-and-replace `<PEKELILING_FOLDER>` in `~/.claude/agents/ijah.md` with that folder's absolute path.
3. Ijah will create and maintain a running decision log at `<PEKELILING_FOLDER>/00 - Log Rujukan Pekeliling & Keputusan.md` — every issue it researches gets logged there so future sessions don't repeat the same research and stay consistent with precedent.

**This log file will contain your own real working decisions — keep it in a private location, not a public repo.**

## ⚠️ Disclaimer

- This is an **unofficial, personal tooling project**, reverse-engineered from observed document patterns. It is **not affiliated with, endorsed by, or representative of the Ministry of Finance Malaysia** or any government agency.
- House-style conventions (fonts, phrases, slogans, honorific ladders) reflect one office's practice at one point in time. Government templates, slogans, and circular numbers change — verify against your own office's current template and current official sources before using any output in a real submission.
- **Ijah does not guarantee regulatory accuracy.** It labels every citation as `[DISAHKAN — Fail Tempatan]`, `[DISAHKAN — Sumber Rasmi]`, or `[BELUM DISAHKAN]` specifically because circular numbers and thresholds are easy to get wrong and costly to get wrong in a signed government paper. Always independently verify a `[BELUM DISAHKAN]` citation, and spot-check `[DISAHKAN]` ones too before relying on them for anything consequential.
- No real names, file reference numbers, or specific matters from the original source documents are included in this repo — all examples are genericized/fictional templates.

## License

MIT — see [LICENSE](LICENSE).
