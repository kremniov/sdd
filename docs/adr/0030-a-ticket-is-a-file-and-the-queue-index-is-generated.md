# 0030. A ticket is a file and the queue index is generated

Date: 2026-09-26
Status: Accepted
PR: —

## Context

A queue in one file forced an agent to read every ticket, including the closed
history, to find one piece of work. In an adopting project the file reached
55 KB, and each read cost about 14k tokens. Closing a ticket collapsed its body
into a one-line Done entry, so the outcome, context and acceptance survived
only in version history.

## Decision

Each ticket is a file `<tickets><ID>.md` with frontmatter for type, phase,
areas, status, group and, when closed, the closing date and change reference.
Closing keeps the file, its title and its body, and adds a Result field.

`.sdd/tasks-index` generates two indexes from the ticket files: `tasks` lists
open tickets by group and status, and `tasks_done` lists closed tickets, most
recently closed first. An agent reads the open index to choose work and reads
the closed index only for closed work. The tool's `--check` mode fails on a
stale index or a malformed ticket, and belongs in the project's `verify`
command.

The frontmatter is a restricted subset of YAML, and the tool rejects anything
outside it: unknown keys, empty values, nested values, escapes and plain text
that YAML would read with another meaning. The tool reads every value as text.
A YAML parser reads the same text for every accepted value, but can type a
bare number or the closing date; the schema is string-valued, so that type
carries no meaning. The tool needs no YAML library.

A project without a `tickets` directory keeps its single queue file with its
own conventions. Setup offers conversion.

## Alternatives

- **An external tracker through MCP.** Ticket state would leave the branch, so
  closing would no longer travel in the reviewed integration commit. Tool
  schemas would load into every session, and the method would depend on one
  product.
- **An index maintained by hand.** Tags and titles would live in two places and
  drift from the first edit.
- **Full YAML frontmatter.** Parsing it needs a library outside the standard
  library of the tool's interpreter, which an adopting project would have to
  install. Ticket metadata needs only flat scalars and flat lists.
- **One index with open and closed sections.** The closed section was more than
  half of the index in the adopting project and grows with every merge.

## Consequences

The open index stays near the size of the open work. Closed tickets keep their
full text. A ticket edit also regenerates the indexes, and the regenerated
indexes travel in the same commit. Parallel branches can still conflict in an
index; regeneration resolves the conflict.
