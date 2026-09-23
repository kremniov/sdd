# Integration

G4 is explicit user permission to integrate a specific PR, such as "merge
this PR". Then:

1. Check independent review and readiness through status/checks. If review is
   missing or a known blocker remains, retain permission and pause integration.
   Resolve blockers and run available checks before the final commit; return
   changed decisions or scope to the user.
2. Close any ticket through `/sdd:tasks` and fill missing ADR PR references in
   the same final branch commit.
3. Run required project checks and push. Call merge only after prerequisites
   pass; report the actual result.

Implementation approval is not merge permission. Given integration permission,
do not ask again. A Done entry records the approval; report the merge result
separately.

If merge fails, report the cause and branch state. Permission persists within
scope: resolve technical blockers, verify and retry when ready. Missing access
or changed decisions or scope trigger the Stop conditions of `/sdd:work`. Preserve history if
repairs follow the final commit: append verified repair commits. Do not rewrite
published history or add an empty final commit to keep Done last.
