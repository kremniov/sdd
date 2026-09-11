"""Skills and templates must name no language, tool or framework.

The method is stack-agnostic, so any ecosystem vocabulary in the shipped text is
a leak of whatever codebase an example was drawn from. The list below is
deliberately broad across ecosystems rather than tuned to one — a check that
enumerates a single project's stack is itself a description of that project.
"""

import re
import sys
from pathlib import Path

TERMS = [
    # languages and runtimes
    "golang", "rust", "python", "ruby", "java", "kotlin", "swift", "scala",
    "elixir", "erlang", "haskell", "clojure", "php", "perl", "dotnet", "csharp",
    "typescript", "javascript", "nodejs", "deno", "bun",
    # build and package tooling
    "npm", "pnpm", "yarn", "cargo", "maven", "gradle", "bundler", "poetry",
    "pipenv", "composer", "makefile", "cmake", "bazel", "webpack", "vite",
    # frameworks
    "django", "flask", "rails", "spring boot", "laravel", "express",
    "fastapi", "nextjs", "nuxt", "svelte", "angular", "vuejs", "react",
    # data stores and infra
    "postgres", "postgresql", "mysql", "sqlite", "mongodb", "redis",
    "cassandra", "elasticsearch", "kafka", "rabbitmq", "pgvector",
    "kubernetes", "docker", "terraform", "ansible",
    # codegen, migrations, orm
    "sqlc", "oapi-codegen", "openapi", "graphql", "protobuf", "goose",
    "flyway", "liquibase", "alembic", "prisma", "sequelize", "hibernate",
    # test runners
    "pytest", "jest", "vitest", "rspec", "junit", "mocha", "cypress",
    "playwright",
]

# Words that are ordinary English in context and must not be matched bare.
PATTERNS = {t: re.compile(rf"(?<![\w-]){re.escape(t)}(?![\w-])", re.I) for t in TERMS}

# A stack also arrives without its name: a source path carries the extension, and
# a build tool is invoked as a verb. "go", "gem" and "mix" are ordinary English,
# so these shapes match them only where the syntax gives them away.
SHAPES = {
    "a source file extension": re.compile(
        r"\.(?:go|rs|py|rb|ts|tsx|jsx|java|kt|swift|scala|ex|exs|hs|clj|cljs"
        r"|php|cs|fs|cpp|hpp|erl|pl|dart|m|mm)(?![\w-])"
    ),
    "a build tool as a command": re.compile(
        r"(?<![\w-])(?:go|gem|mix|dotnet|swift|cabal|stack|sbt|rebar3|dune|lein"
        r"|tsc|node|ruby|python3?)\s+(?:test|build|run|get|install|mod|exec|fmt)"
        r"(?![\w-])", re.I
    ),
}
PATTERNS.update(SHAPES)

# A line that surveys several ecosystems neutrally reveals nothing about any one
# project. Each exemption names the file, the term, and why it is not a leak.
EXEMPT = {
    ("plugins/sdd/skills/setup/SKILL.md", "makefile"):
        "lists Makefile / package.json / justfile / Taskfile side by side, so the "
        "agent can find the verify command in whatever ecosystem it landed in",
}

roots = [Path("plugins/sdd/skills")]
hits = []
for root in roots:
    for path in sorted(root.rglob("*.md")):
        for n, line in enumerate(path.read_text().splitlines(), 1):
            for term, pat in PATTERNS.items():
                if pat.search(line) and (str(path), term) not in EXEMPT:
                    hits.append((path, n, term, line.strip()))

if hits:
    for path, n, term, line in hits:
        print(f"  FAIL    {path}:{n} names {term!r}")
        print(f"          {line[:100]}")
    sys.exit(1)

print(f"  OK      no stack vocabulary in skills or templates "
      f"({len(TERMS)} terms, {len(SHAPES)} shapes checked)")
sys.exit(0)
