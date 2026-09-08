# Design from approved decisions

## Initial state

G1 has approved per-row import outcomes to preserve valid rows. The decision log specifies each rejected row includes a reason. No five-decision minimum is needed.

## User request

> Write the design and then the plan through their approval gates.

## Continuation

Approve the complete design at G2, then the complete plan at G3.

## Evaluator: expected behavior

Read the decision log; write contracts, failure behavior and verification in a complete design. Produce ordered checkable plan steps after G2. Manual checks specify observer and expected result.

## Evaluator: failure conditions

Fail if the agent reopens settled alternatives, requests section-by-section approval, invents five decisions, or writes the plan before G2.
