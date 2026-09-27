# Structural migrations

Read this during an update. A comparison with the current template cannot
derive these changes: they move files, convert content or install tools. For
each entry, check its condition in the project. Propose every entry whose
condition holds and apply it after approval. An entry whose condition does not
hold needs no action. Entries are append-only.

## 1.2.0

### Configuration in `.sdd/`

**Applies when:** the project has `.sdd.yml` and no `.sdd/config.yml`.

Move `.sdd.yml` to `.sdd/config.yml` with its history. Change each reference to
the old path in the rules file and project documents. Keep every key.

### Ticket files

**Applies when:** the config has no `tickets` key, and the `tasks` file is a
queue in the `/sdd:tasks` format of an earlier version: tickets and a Done
section in one file.

Propose `tickets` and `tasks_done` paths. Write one file per entry in the format
of `/sdd:tasks`. Keep each ID, title and body. A completed entry becomes a
closed ticket: its one-line result becomes the Result field, and its change
reference becomes `ref`. Recover a title or body from the version history when
the completed entry lost it. Create `tasks_done` from `tasks-done.md`, replace
the managed region of `tasks` with the current template, add the index markers
after it and run `.sdd/tasks-index`. The conversion needs approval of the
ticket format and the moved content. A declined conversion leaves `tickets`
unset.

### Index tool

**Applies when:** the config sets `tickets` and `.sdd/tasks-index` is missing.

Copy `tasks-index` to `.sdd/tasks-index` as an executable file. Propose adding
`.sdd/tasks-index --check` to the `verify` command.
