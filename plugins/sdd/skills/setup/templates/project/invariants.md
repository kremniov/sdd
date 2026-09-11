<!-- sdd:scaffold v1.1.14 -->
# Architectural invariants

Use `/sdd:canon` to establish, amend or audit this list. Record current rules
supported by evidence and accepted obligations. Each rule states its scope,
detector and response to a violation. Label manual detection as manual.

Preserve numbers. Append new entries. Keep retired numbers, struck through and
linked to their ADR under `{{adr}}`. Agree changes and retirement with the user.
A code violation does not by itself authorize changing the rule.

Entry format:

    N. **Name.** Rule and scope.
       *Detect:* command or explicitly manual review question.
       *On violation:* reject, or agree a rule change and record its ADR.

Link rules from other documents rather than restating them. Keep proposals
outside the current list until confirmed. An empty list is a valid initial state.
<!-- /sdd:scaffold -->
