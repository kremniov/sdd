# Layout

Where things live. Read `invariants.md` first — this says where, that says what
must hold.

```
.claude-plugin/marketplace.json   the catalogue: one entry, pointing at plugins/sdd
plugins/sdd/
  .claude-plugin/plugin.json      name, version, license, keywords
  skills/<name>/SKILL.md          one skill per directory; the directory name is
                                  the skill name and the frontmatter must match
  templates/
    _DESIGN.md _PLAN.md _ADR.md   artifact skeletons, read via ${CLAUDE_PLUGIN_ROOT}
    project/                      what adoption writes INTO a repo, with
                                  {{placeholders}} substituted from .sdd.yml
docs/
  architecture/                   this canon
  adr/                            one decision per file
  features/<name>/                design.md + plan.md, frozen at merge
  tasks.md  roadmap.md
scripts/check.sh                  the structural gate
```

## Where to start reading

`README.md` for what the method is. Then `plugins/sdd/templates/project/CLAUDE.section.md`
— that file **is** the method, in the form a project receives it. The skills are
supporting procedures around it.

## The two directories that look alike

`templates/` holds skeletons the model reads while writing an artifact in
someone's project. `templates/project/` holds files that get written into the
project once, at adoption, with placeholders substituted. Nothing under
`templates/project/` is ever read after adoption; nothing under `templates/`
directly is ever copied.

## Adding a skill

A directory under `plugins/sdd/skills/`, a `SKILL.md` whose frontmatter `name`
matches the directory, a description that says when to use it. Then
`./scripts/check.sh`. Bump `version` in `plugin.json` — without a bump,
installed copies do not update.
