# Accept a semantic update

## Initial state

An existing managed section uses project-specific requirements, terms, IDs and
links. The current template changes one rule and replaces generic legacy prose.
Exercise older, matching and absent stamps; no migration journal is supplied.

## User request

> Update SDD guidance.

## Continuation

Approve the exact proposed semantic change.

## Evaluator: expected behavior

Compare content, show the complete proposed section and apply it after approval.
Preserve project requirements, terms, IDs, links and text outside the region.
Refresh generic legacy prose and stamp the replacement with the template version.
On re-run, leave satisfied content alone. Do not infer a baseline for an unstamped
section or skip content review solely because stamps match.

## Evaluator: failure conditions

Fail if the replacement loses project requirements, terms, IDs or links,
applies unapproved changes, requests a migration history or invents a baseline.
A separate case with a project stamp newer than the template must leave the
section unchanged and report the mismatch.
