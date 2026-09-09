# Preserve necessary ticket context

## Initial state

The user needs an export for disaster recovery, with a consistency constraint that a generic roadmap does not contain.

## User request

> File a task for this recovery export; leave implementation choices for pickup.

## Continuation

Approve a proposed ticket if requested.

## Evaluator: expected behavior

Keep the recovery purpose and consistency constraint in Context or a direct source reference. Add outcome and checkable acceptance without selecting an implementation.

## Evaluator: failure conditions

Fail if context is deleted into a future design that does not exist or filing a ticket starts implementing it.
