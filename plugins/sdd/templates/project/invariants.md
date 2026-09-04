<!-- sdd:scaffold v1.0.0 -->
# Architectural invariants

The canonical list. These rules govern all work in this repository. A change that
violates one is an architectural regression and needs a documented invariant
change — an ADR under `{{adr}}`.

This file is the single source of truth. The rules file and the feature designs
link here; each rule is stated once.

<!--
`/sdd:canon` maintains this list. It establishes the list from the codebase, adds
a line when a merging branch earns one, and audits the list against code that has
drifted.

An invariant is a rule the code obeys today and that a reviewer pushes back on
breaking. Each entry carries three parts:

    N. **Short name.** What must hold, phrased so a reviewer can decide whether
       a diff violates it.
       *Detect:* a command, a grep, or the question a reviewer asks.
       *On violation:* reject, or open an ADR to move the rule.

The detection note lives on the rule. In a footer it drifts the first time a
checker grows, and the drift is silent. A rule whose *Detect* is a question is a
convention; say so, so the entry claims the rigour it has.

Numbers are stable, because other documents cite them. Append them; renumber
none. A retired rule keeps its number, struck through, naming the ADR that
retired it.
-->
<!-- /sdd:scaffold -->

1. **<Name>.** <What must hold.>
   *Detect:* <command, grep, or review question>
   *On violation:* <reject | ADR to move the rule>

## Per-layer responsibilities

Where the codebase has layers, state what each one owns and what it must keep
out. The "must NOT" column is what makes the table usable in review.

| Layer | Location | Owns | Must NOT |
|---|---|---|---|
| | | | |
