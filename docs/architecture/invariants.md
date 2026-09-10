# Architectural invariants

Current rules for this plugin. [The method](../method.md) specifies workflow
behavior. Decision records preserve history. Link these entries by number.

1. **Project locations come from configuration.** Skills read project paths
   from `.sdd.yml`. Example configurations may show illustrative paths.
   *Detect:* manual review of skill inputs and every project file operation.
   *On violation:* use the configured location.
2. **Skeletons and scaffold have different lifecycles.** Skills read artifact
   skeletons in place from the plugin. Setup writes scaffold into missing project
   files. Existing managed guidance updates through stamped, described changes;
   matching versions need no edit. Generic prose refresh follows ADR 0029; legacy retirement follows ADR 0020.
   *Detect:* `./scripts/check.sh` checks paths, reachability, fences, stamps and
   migration entries; manual scenario review checks semantic updates.
   *On violation:* correct the reference or migration before release.
3. **Adoption preserves project content.** Existing-file changes require an
   approved concrete proposal. Preserve unrelated text and project additions.
   Legacy region replacement is shown in full and requires explicit approval.
   *Detect:* fresh, existing-process, accepted-update, declined-update and
   malformed-marker scenarios compare file contents with the approved edits.
   These are manual or agent-run checks, not assertions made by the structural suite.
   *On violation:* restore unapproved changes and correct the setup procedure.
4. **Instructions load where they are needed.** Resident text holds cross-session
   constraints and routing. Work owns the execution sequence; specialized skills
   own their procedures and standalone inputs. References have loading conditions.
   Templates specify artifact content. Setup also carries the constraints needed
   before resident rules are adopted. See ADR 0028, amending ADR 0022.
   *Detect:* manual coverage review against `docs/method.md` and scenario inputs.
   *On violation:* assign a rule to its owner and remove unnecessary duplication.
5. **The method is portable across project stacks.** Skills and templates do
   not require the origin project's technology or domain. Examples are generic.
   *Detect:* `./scripts/check.sh` checks ecosystem terms and source/command
   patterns; manual review covers assumptions outside that vocabulary list.
   *On violation:* replace the project-specific requirement with a portable one.
6. **Canon rules require evidence and accepted obligations.** Separate current
   behavior, required rules and proposals. A violation does not authorize changing
   the obligation. See ADR 0023, amending ADR 0003.
   *Detect:* manual review of rule evidence and detector coverage; canon scenarios
   check unsupported proposals and widespread violations.
   *On violation:* report the discrepancy and obtain agreement before changing a rule.
7. **Working instructions change an action or decision.** State actions,
   conditions, authority and results. Keep a reason only when needed to choose
   correctly. Omit rhetoric and incident history. Migration entries may explain
   replaced guidance; ADRs preserve decision history. See ADR 0023, amending ADR 0015.
   *Detect:* manual deletion test: would removing the sentence change a justified
   action, decision or result? Scenario evaluation checks the remaining behavior.
   *On violation:* remove or rewrite unnecessary prose.
8. **Invariant numbers are stable.** Append new rules. Retired entries retain
   their number and link the retirement ADR.
   *Detect:* compare numbered entries with the base revision.
   *On violation:* restore numbering and correct references.
9. **The repository rules are rendered from the scaffold.** Substitute `.sdd.yml`
   into `templates/project/CLAUDE.section.md` to produce the managed CLAUDE section.
   *Detect:* `./scripts/check.sh` checks that the render is present in CLAUDE.md.
   *On violation:* edit the template and re-render.
10. **Catalogue sources resolve to matching manifests.** Spell the source in
    full relative to the marketplace root, prefixed with `./`; omit pluginRoot.
    *Detect:* `./scripts/check.sh` resolves each source and checks plugin identity.
    *On violation:* correct the catalogue path or manifest.
11. **Active skill references resolve.** Use `/sdd:<skill>` and matching skill
    directories and frontmatter. Historical records can retain old names.
    *Detect:* `./scripts/check.sh` scans active documents and resolves skill names.
    *On violation:* update the reference and any affected migration guidance.
12. **Size checks and behavior checks are distinct.** A SKILL.md has at most
    1200 words including examples; resident rules have at most 400. Skill,
    resident and skeleton headings stop at H3 outside fenced examples. Negation
    frequency is advisory. Report reference and migration text volume separately
    from any measured session load. See ADR 0024, replacing ADR 0021's density gate.
    *Detect:* `./scripts/check.sh` checks size/depth and checker tests. Scenario
    review and observed runs assess behavior; the counters do not establish it.
    *On violation:* reduce excess size or depth; investigate behavior separately.

## Layout responsibilities

| Part | Location | Responsibility |
|---|---|---|
| Catalogue | `.claude-plugin/` | Resolve the plugin source |
| Manifest | `plugins/sdd/.claude-plugin/` | Version and package metadata |
| Skills | `plugins/sdd/skills/` | Scoped procedures and conditional references |
| Skeletons | `plugins/sdd/templates/_*.md` | Artifact content, read in place |
| Scaffold | `plugins/sdd/templates/project/` | Rendered project guidance and semantic migration history |
| Method | `docs/method.md` | Complete agreed behavior for readers and maintainers |
| Scenarios | `tests/scenarios/` | Versioned input cases and evaluator expectations |
| Behavioral fixtures | `tests/behavior/` | Reproducible repositories, prompts and local agent runner |
| Checks | `scripts/`, `tests/test_*.py` | Structural checks using the standard library |
