# Layout

| Path | Responsibility |
|---|---|
| `.claude-plugin/marketplace.json` | Catalogue entry resolving the plugin |
| `plugins/sdd/.claude-plugin/plugin.json` | Plugin identity and version |
| `plugins/sdd/skills/<name>/SKILL.md` | One procedure with matching frontmatter |
| `plugins/sdd/skills/<name>/*.md` | Conditional procedure references |
| `plugins/sdd/skills/{design,plan,work}/templates/_*.md` | Design, plan and ADR skeletons, read in place |
| `plugins/sdd/skills/setup/templates/project/` | Rendered scaffold; CHANGES.md stays in the plugin |
| `docs/method.md` | Complete agreed method |
| `docs/architecture/` | Current invariants, map and plugin interactions |
| `docs/adr/` | Durable decision history |
| `docs/features/<name>/` | Feature artifacts, historical after merge |
| `docs/tasks.md`, `docs/roadmap.md` | Queue and direction |
| `tests/scenarios/` | Behavioral cases and evaluation procedure |
| `tests/test_register.py` | Register checker behavior tests |
| `scripts/check.sh` | Entry point for structural checks |
| `docs/stuff/` | Ignored discussion, status and evaluation evidence |

Start with `docs/method.md` for behavior, then the relevant skill. Read
`invariants.md` before changing plugin rules and `plugin-mechanics.md` before
changing adoption or file resolution. Scenario results must identify whether they
are textual walkthroughs or observed agent runs.
