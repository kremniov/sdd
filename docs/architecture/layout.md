# Layout

| Path | Responsibility |
|---|---|
| `.claude-plugin/marketplace.json` | Catalogue entry resolving the plugin |
| `plugins/sdd/.claude-plugin/plugin.json` | Plugin identity and version |
| `plugins/sdd/skills/<name>/SKILL.md` | One procedure with matching frontmatter |
| `plugins/sdd/skills/<name>/*.md` | Conditional procedure references |
| `plugins/sdd/skills/{design,plan,work}/templates/_*.md` | Design, plan and ADR skeletons, read in place |
| `plugins/sdd/skills/setup/templates/project/` | Rendered scaffold and shipped tools; CHANGES.md stays in the plugin |
| `docs/method.md` | Complete agreed method |
| `docs/architecture/` | Current invariants, map and plugin interactions |
| `docs/adr/` | Durable decision history |
| `docs/features/<name>/` | Feature artifacts, historical after merge |
| `docs/tasks/`, `docs/tasks.md`, `docs/tasks-done.md` | Ticket files and their generated open and closed indexes |
| `docs/roadmap.md` | Direction |
| `.sdd/` | Project config and the copy of the shipped index tool |
| `tests/scenarios/` | Behavioral cases and evaluation procedure |
| `tests/test_*.py` | Checker and shipped-tool behavior tests |
| `scripts/check.sh` | Entry point for structural checks |
| `docs/stuff/` | Ignored discussion, status and evaluation evidence |

Start with `docs/method.md` for behavior, then the relevant skill. Read
`invariants.md` before changing plugin rules and `plugin-mechanics.md` before
changing adoption or file resolution. Scenario results must identify whether they
are textual walkthroughs or observed agent runs.
