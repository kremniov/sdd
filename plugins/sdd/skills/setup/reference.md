# Update managed guidance

Read this for existing scaffold files or a legacy rules section. Templates mark
the plugin-owned guidance; project content outside those markers is preserved.
Use `sdd:rules` for the current rules section and `sdd:scaffold` for other files.

## Versions and boundaries

Check marker count, order and version syntax before editing a file. Report
missing ends, duplicate pairs, reversed markers and invalid versions with a file
and location. Ask the user to resolve the boundary; leave that file unchanged.
A rules file with both current and legacy sections also requires resolution.

| State | Action |
|---|---|
| Project and template stamps match | Leave the region unchanged |
| Project stamp is older | Apply described changes below |
| Project stamp is newer | Report the older installed plugin and leave the file unchanged |
| A valid old fence has no stamp | Use the documented baseline `v0.2.0` |
| No fence | Show the proposed boundary and ask; add markers on approval at `v0.2.0`, then assess updates |
| Unknown version history | Report the missing migration basis and ask before editing |

Read `${CLAUDE_PLUGIN_ROOT}/templates/project/CHANGES.md` for entries after the
project's stamp and through the template's stamp. Use the current template as
the basis for the complete proposed region. Preserve project requirements,
terms, IDs and references; replace generic legacy prose with current wording.
Before carrying a rule, check whether current skills or configuration already
cover it. Show substantive changes and process conflicts for approval.

Use the migration entries to account for required changes and previous declines.
Keep declined requirements unchanged in the proposal unless the user now accepts
them; a current template does not override a decline. An entry already satisfied
needs no repeated edit. Preserve everything outside the approved region.

Advance the stamp to the highest contiguous version whose entries for that file
are all applied or already satisfied. If nothing is satisfied past the current
stamp, leave it. On re-run, re-offer declined changes; recognize already applied
entries by their meaning when a later accepted edit could not advance the stamp.


## Retire the legacy rules section

For a valid `sdd:method-section` region:

1. Show the complete old region and complete proposed `sdd:rules` replacement.
   Preserve project requirements and references; replace generic legacy prose.
   Check current skills and configuration before treating an old rule as a
   project-specific addition.
2. Explain that execution rules are now in `/sdd:work` and identify actual
   conflicts between the old rules and the installed skills.
3. Ask for the replacement once. On approval, replace only that region and
   retain project additions. On decline, preserve the old region and its stamp;
   leave the new fence unwritten.
4. Report whether the replacement applied. A declined migration leaves old
   resident rules with newer skills; report that conflict and re-offer later.

Do not create a second active method section. Propose fixes for obsolete links
separately. Existing project files are not deleted as part of reference cleanup.
