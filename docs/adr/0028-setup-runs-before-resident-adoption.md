# 0028. Setup runs before resident adoption

Date: 2026-09-10
Status: Accepted

## Context

The first Vortex field run loaded legacy resident instructions before setup.
Current writing and discussion rules cannot depend on the resident section that
setup has yet to install. This qualifies the ownership rule in ADR 0022 and
invariant 4.

## Decision

Setup repeats the minimum approval, discussion, writing, branch and handover
constraints needed for its own execution. Work retains the full implementation,
review and integration procedures. Consolidate these constraints within setup.

## Consequences

This intentional overlap must stay aligned with resident rules and work. It
supports adoption in legacy and new repositories without copying the complete
workflow into setup.
