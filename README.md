# Agentic Engineering Preferences

A public, evolving reference for how I usually structure, build, validate, and maintain software projects with AI agents.

[简体中文](README.zh-CN.md)

> **Personal, not universal. Defaults, not mandates. Project-local context takes precedence.**

## Why This Exists

I work on software projects with coding agents such as ChatGPT, Claude Code, Codex, and similar tools. Across projects, the same engineering questions recur: how much validation is enough, when CI is worth adding, when a dependency is justified, when a Release is meaningful, when an operation needs explicit approval, and how much context an agent should receive up front.

This repository reduces that repeated decision and communication cost. It records the defaults I tend to prefer so capable agents can reuse them as secondary context instead of reconstructing them from scratch in every conversation.

## What This Is

This repository contains:

- **[Preferences](docs/preferences.md)** — relatively stable engineering tendencies;
- **[Decision Rules](docs/decision-rules.md)** — how I usually handle recurring engineering choices;
- **[Project Conventions](docs/project-conventions.md)** — how I usually structure and maintain projects once a choice has been made;
- **[AGENTS.md template](templates/AGENTS.md.template)** — a lightweight starting point for project-local agent instructions.

The repository is intentionally opinionated because it documents my working preferences. It is not intended to establish industry consensus.

## What This Is Not

It is not an industry standard, universal software-engineering methodology, compliance framework, project scoring system, mandatory repository template, or substitute for understanding the target project's own goals and constraints.

## How Agents Should Use It

When working on one of my projects:

1. inspect the actual project state;
2. read the target repository's own instructions first;
3. understand the project's goals, constraints, users, and maturity;
4. use this repository only as reusable secondary preference context;
5. apply only the preferences that materially fit the project;
6. prefer project-local evidence and instructions when they conflict with this repository;
7. do not perform destructive or high-impact actions without explicit authorization.

The goal is to reduce repeated explanation, not to replace engineering judgment.

## Core Themes

The current preferences emphasize:

- project outcomes over cross-project convention;
- verifiable results over plausible-looking output;
- reversible, reviewable changes over unnecessary blast radius;
- explicit project context over hidden local knowledge;
- dependencies that justify their maintenance cost;
- deliberate privacy, permission, and public/private boundaries;
- portability and local execution when they provide concrete value.

See [Preferences](docs/preferences.md) for the current wording.

## Repository Status

This repository is an evolving personal reference. Rules should be added only when they reduce recurring engineering decisions or recurring agent communication.

Before this positioning, the repository hosted **Agentic Engineering Review**, an evidence-first project-review system. That design remains preserved in the historical [v0.4 release](https://github.com/Charlie-Wang-03/agentic-engineering-preferences/releases/tag/v0.4). The current repository no longer maintains the diagnostic scoring or review-protocol product as its primary direction.

## Validation

Run:

    python3 scripts/validate_repo.py

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under the [Apache License 2.0](LICENSE).
