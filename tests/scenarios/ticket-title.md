# Name a ticket by its work or symptom

## Initial state

A fresh queue in the skill's format. The user reports a defect in prose and
states the desired behavior.

## User request

> File a bug: when the nightly export job is retried, the report lists each
> order twice. The report must list each order once. The retry appends its rows
> again; code is in `jobs/export.py`. This queue edit and its verification are
> approved.

## Evaluator: expected behavior

The title is a short noun phrase that names the symptom, for example "Duplicate
orders in the nightly report". The Outcome states the target behavior. Acceptance
is checkable. The known cause and code location are kept in Context or Pointers.

## Evaluator: failure conditions

Fail if the title is a sentence that states the target behavior, or restates the
Outcome in other words. Fail if filing the ticket starts implementing it.
