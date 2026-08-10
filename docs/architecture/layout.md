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
    invariants.md                 the rules
    layout.md                     this file
    plugin-mechanics.md           what crosses the plugin/project boundary, when
  adr/                            one decision per file
  features/<name>/                design.md + plan.md, frozen at merge
  tasks.md  roadmap.md
scripts/check.sh                  the structural gate
```

## Where to start reading

`README.md` for what the method is. Then `plugins/sdd/templates/project/CLAUDE.section.md`
— that file **is** the method, in the form a project receives it. The skills are
supporting procedures around it. Before changing how a skill reaches a project,
read `plugin-mechanics.md`.

## The two directories that look alike

`templates/` holds skeletons the model reads while writing an artifact in
someone's project. `templates/project/` holds files that get written into the
project once, at adoption, with placeholders substituted. Nothing under
`templates/` directly is ever copied.

A scaffold file is read once more after that, and only to compare: each carries
a `<!-- sdd:scaffold -->` fence around the part the plugin wrote, and a re-run
of `/sdd:setup` diffs that region against the current template so a project can
take a correction without losing what it wrote below (ADR 0009).

## Adding a skill

A directory under `plugins/sdd/skills/`, a `SKILL.md` whose frontmatter `name`
matches the directory, a description that says when to use it. Then
`./scripts/check.sh`. Bump `version` in `plugin.json` — without a bump,
installed copies do not update.
