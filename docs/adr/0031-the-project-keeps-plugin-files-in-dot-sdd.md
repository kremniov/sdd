# 0031. The project keeps plugin files in `.sdd/`

Date: 2026-09-26
Status: Accepted
PR: [#11](https://github.com/kremniov/sdd/pull/11)

## Context

The index generator must run in the adopting project, including in its
continuous integration, where the plugin is not installed. The project needs a
copy of the tool and a place for it. The configuration file `.sdd.yml` was the
only plugin file at the repository root.

## Decision

The `.sdd/` directory holds the project configuration, `.sdd/config.yml`, and
the tools that setup copies from the plugin. A shipped tool is scaffold: it
carries its version on a `# sdd:scaffold vN.N.N` line, the plugin owns the whole
file, and setup replaces it when the project copy is older. Setup moves a
legacy `.sdd.yml` into `.sdd/config.yml` with its history.

A tool reads its paths from the configuration and carries no project
vocabulary. It uses the interpreter that the plugin's own checks use, with the
standard library only.

## Consequences

Invariant 2 covers shipped tools, and `check_scaffold.py` checks their stamps
beside the fenced files. This repository keeps its own copy in `.sdd/`, and
`check.sh` fails when the copy differs from the template. Every skill reads
`.sdd/config.yml`; a project that still has `.sdd.yml` is sent to setup.
