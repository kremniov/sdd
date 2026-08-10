<!-- sdd:scaffold v0.2.0 -->
# Architectural invariants

Canonical list. These rules apply to all work, every feature. Any change that
violates one is an architectural regression and requires an explicit, documented
invariant change — open an ADR under `{{adr}}`.

This is the single source of truth for the invariants. The rules file and feature
designs **link here**; they do not restate them.

<!--
Populate and extend this list with `/sdd:canon` — it establishes the
list from the codebase, adds a line when a merging branch earns one, and audits
the list against code that has drifted.

An invariant is a rule the code obeys today and that a reviewer would push back
on breaking — not an aspiration. Each entry carries three parts:

    N. **Short name.** What must hold, phrased so a reviewer can decide whether
       a diff violates it.
       *Detect:* a command, a grep, or the question a reviewer asks.
       *On violation:* reject, or open an ADR to move the rule.

The detection note belongs on the rule, never in a summary at the foot of the
file — a footer drifts the first time a checker grows, and nothing catches it.
A rule whose *Detect* is only a question is a convention; say so rather than
implying a rigour that is absent.

Numbers are stable: other documents cite them. Append, never renumber. A retired
rule keeps its number, struck through, naming the ADR that retired it.
-->
<!-- /sdd:scaffold -->

1. **<Name>.** <What must hold.>
   *Detect:* <command, grep, or review question>
   *On violation:* <reject | ADR to move the rule>

## Per-layer responsibilities

Where the codebase has layers, state what each owns and what it must not do —
the "must not" column is what makes the table usable in review.

| Layer | Location | Owns | Must NOT |
|---|---|---|---|
| | | | |
