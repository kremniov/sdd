# Layout

Where things live. Read `invariants.md` first — this says where, that says what
must hold.

```
.claude-plugin/marketplace.json   the catalogue: one entry, pointing at plugins/sdd
plugins/sdd/
  .claude-plugin/plugin.json      name, version, license, keywords
  skills/<name>/SKILL.md          one skill per directory; the directory name is
                                  the skill name and the frontmatter must match
  skills/<name>/*.md              reference files a SKILL.md names, loaded on
                                  demand when the skill is past its word budget
  templates/
    _DESIGN.md _PLAN.md _ADR.md   artifact skeletons, read via ${CLAUDE_PLUGIN_ROOT}
    project/                      what adoption writes INTO a repo, with
                                  {{placeholders}} substituted from .sdd.yml
      CHANGES.md                  what each version changed; read by a re-run,
                                  written into no project
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

`README.md` for what the method is. Then `plugins/sdd/skills/work/SKILL.md` —
that file **is** the method: the gates, the tiers, the blockers and the
handing-over rules. `plugins/sdd/templates/project/CLAUDE.section.md` holds the
part that stays resident in a project, which is what must hold when no skill is
loaded (ADR 0018). The other skills are the procedures the frame calls for.
Before changing how a skill reaches a project, read `plugin-mechanics.md`.

## The two directories that look alike

`templates/` holds skeletons the model reads while writing an artifact in
someone's project. `templates/project/` holds files that get written into the
project once, at adoption, with placeholders substituted. Nothing under
`templates/` directly is ever copied.

A scaffold file is read once more after that, and only to compare: each carries
a `<!-- sdd:scaffold vN.N.N -->` fence around the part the plugin wrote, stamped
with the version its region last changed in. A re-run of `/sdd:setup` compares
that stamp against the template's and offers the entries `CHANGES.md` records in
between, so a project takes a correction into its own wording and keeps what it
wrote below (ADR 0009, ADR 0011; invariant 2). A major version may instead
retire a region outright, shown in full and removed on one explicit yes
(ADR 0020).

## Adding a skill

A directory under `plugins/sdd/skills/`, a `SKILL.md` whose frontmatter `name`
matches the directory, a description that says when to use it. Then
`./scripts/check.sh`, which also measures the file against invariant 12 — past
1200 words, move the surplus into a reference file beside it. Bump `version` in
`plugin.json`; installed copies update on a bump alone.
