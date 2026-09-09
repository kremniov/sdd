# Establish a canon

Read the request, code, checks and relevant requirements or accepted decisions.
Survey entry points, component boundaries, interactions, recurring patterns,
structural tests and exceptions. Read enough implementations to establish a
claim; report sampling limits in a large codebase.

Apply the candidate filter in `SKILL.md`. Distinguish observed patterns,
required rules and unconfirmed proposals. Check actual detector coverage.
Present candidates with evidence and mark manual enforcement explicitly.
Ask the user to confirm rules and resolve discrepancies between code and
obligations. A repeated pattern does not prove that deviations are forbidden.

Write approved entries into the scaffold's `invariants.md` under `canon`, using
the entry format. If the scaffold is missing, use `/sdd:setup` first. Create or
update `layout.md` with component responsibilities, entry points and the reading
map. Use `/sdd:subsystem` when interactions need a separate explanation.

When evidence supports no invariant, report that result. A short note can state
that the canon is not established. Keep suggested future rules outside the
current invariant list and ask before recording them as tasks.
