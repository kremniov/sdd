<!-- sdd:rules v1.0.0 -->
## Development method

This project runs spec-driven development. `/sdd:work` carries the method: the
gates, the tier table, the blockers, the review and the handing-over rules.
Invoke it when a task starts. The paths every skill reads are in `.sdd.yml`.

The rules below hold in every session, whether a skill is loaded or not.

### Handing over

The user integrates the branch. Bring the branch to merge-ready, push it, open
the pull request, and stop. `git merge`, `gh pr merge` and a push to the
integration branch are the user's decision, on every branch and at every tier.

### Evidence

Run `{{verify}}`, read its output, and then say that a thing is done, fixed or
passing. Name what you ran. A suite you did not watch finish is not evidence.
Where something fails or was skipped, say so and show the output.

### Tests

Run the test and watch it fail, for the reason you intend, before you write the
code that makes it pass.

### Comments

A comment carries the constraint that gives the code its current shape. Say what
the code cannot: a comment that restates the signature or the identifier is
deletion-safe. Keep history out — "used to", "instead of", "we removed X" belong
to the commit, the pull request and the decision record. The default for any
edit, a review fix included, is no new comment. Test before saving: cover the
comment and reread the code. Delete it if a competent reader reads on.

### Skills

Invoke `/sdd:work` when a task starts. Invoke another skill when the task is
plainly the one it covers.
<!-- /sdd:rules -->
