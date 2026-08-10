# ADR 0008 — The catalogue spells each plugin source in full

**Status:** accepted · **Date:** 2026-08-10

## Context

The marketplace documentation describes `metadata.pluginRoot` as a base
directory prepended to relative plugin sources, with the example `"./plugins"`
letting an entry read `"source": "formatter"` instead of
`"source": "./plugins/formatter"`.

Measured against Claude Code 2.1.226, both halves of that are wrong:

- `"source": "formatter"` fails schema validation — `plugins.0.source: Invalid
  input`. A string source must start with `./`.
- `"source": "./formatter"` passes validation, but `pluginRoot` is not
  prepended. The path resolves from the marketplace root, and installation fails
  with `Source path does not exist`.

So `pluginRoot` has no effect on string sources in this version, and the two
spellings it exists to enable are respectively rejected and misresolved. This
cost us a broken release: `0.1.0` shipped with `"source": "sdd"` and could not be
installed by anyone.

`claude plugin validate` does not close the gap. It checks the schema, not the
filesystem — it reports `Validation passed` on `"./sdd"`, a source pointing at a
directory that does not exist.

## Decision

Every entry in `plugins` names the plugin's full path from the marketplace root,
`./`-prefixed: `"source": "./plugins/sdd"`. The `metadata.pluginRoot` key is not
used.

`scripts/check_marketplace.py` resolves each source that way and requires a
`.claude-plugin/plugin.json` under it naming the same plugin. It fails on a
`pluginRoot` key, on a source without the `./` prefix, and on a source that
resolves nowhere. `check.sh` additionally runs `claude plugin validate` when the
CLI is on PATH, and says so when it is not.

## Alternatives

- **Keep `pluginRoot` and the short source.** Documented, and does not work.
- **Keep `pluginRoot` alongside the full source.** Harmless today, but it states
  a relationship the loader does not honour, and the next person to read the docs
  will shorten the source to match it.
- **Trust `claude plugin validate` as the gate.** It passed the manifest that
  broke the release.

## Consequences

The full path is redundant with the repository layout and will look like
something to tidy up — the checker's failure message names this ADR so the
reason arrives with the failure.

If a later version of Claude Code implements `pluginRoot` as documented, this
decision costs nothing: a fully spelled source is correct under both readings.
Revisit only to shorten, and only with a measurement rather than the
documentation.
