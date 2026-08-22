# Agentic Open-Source Engineering Methodology

> A practical, evolving methodology for designing, developing, verifying, maintaining, and evolving open-source software with AI agents.

[简体中文](README.zh-CN.md)

> **Status: v0.1 — private incubation.** The methodology is still being tested against real project work and should not yet be treated as an industry standard or a finished specification.

## Why This Exists

AI agents are making software generation dramatically cheaper. That does not remove the need for engineering judgment; it increases the importance of clear constraints, verification, reviewability, privacy boundaries, and maintainable project structure.

This repository develops an opinionated but adaptable engineering decision system for open-source projects in which humans and AI agents work together.

It is designed to be:

- practical enough to guide real repository decisions;
- executable enough to inform `AGENTS.md`, templates, checks, and automation;
- stable at the principle layer while allowing practices to evolve with tools;
- open and reusable without pretending that one workflow fits every project.

## Meta-Principle

### Outcomes over Dogma

**Project outcomes come first. Principles guide engineering judgment; they do not replace it.**

When a default conflicts with user value, quality, security, performance, maintainability, or another principle, use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

> **Deviation is allowed; unexplained deviation is not.**

## Core Principles

1. **Open by Default**
2. **Agent-Native, Human-Accountable**
3. **Portable over Model-Agnostic**
4. **User Sovereignty & Privacy by Default**
5. **Local-First When Practical**
6. **Justified Dependencies**
7. **Progressive Usability**
8. **Verifiable by Default**
9. **Reversible Change**

Read the rationale and boundaries in [Principles](docs/principles.md).

## Methodology Structure

The methodology separates three layers that change at different speeds:

1. **Principles** — what values and engineering properties should be preferred;
2. **Decision Framework** — how to resolve conflicts, trade-offs, and justified exceptions;
3. **Practices** — how to implement the methodology in repositories, agent instructions, validation, contribution workflows, and releases.

Start here:

- [Principles](docs/principles.md)
- [Decision Framework](docs/decision-framework.md)
- [Practices](docs/practices.md)

## Using It in a Project

A lightweight adoption path is:

1. read the core principles;
2. choose the defaults that materially affect your project;
3. adapt [`templates/AGENTS.md.template`](templates/AGENTS.md.template) into repository-level agent instructions;
4. use the decision framework when defaults conflict;
5. record only higher-impact decisions that deserve durable evidence;
6. feed real project failures and successes back into the methodology.

A lightweight [decision record template](templates/DECISION_RECORD.md) is included for decisions that need more than a normal commit or pull-request explanation.

## Repository as Reference Implementation

This repository should practice what it describes. In particular, it aims to maintain:

- clear agent-facing instructions in [`AGENTS.md`](AGENTS.md);
- first-class English and Simplified Chinese documentation;
- lightweight automated validation;
- focused and reversible changes;
- explicit contribution rules;
- minimal unnecessary dependencies.

Run the current repository validation with:

```bash
python3 scripts/validate_repo.py
```

## Scope

This project focuses on engineering methodology for human–agent collaboration in open-source software.

It is **not** intended to be:

- a catalog of current AI products or models;
- a claim that all projects should use the same stack;
- a collection of invented case studies;
- a blog or content-marketing repository;
- a replacement for established software engineering, security, or open-source standards.

Tool-specific guidance belongs in the practice layer and may change rapidly.

## Incubation and Evolution

The repository is intentionally being developed privately before its first public release. The methodology is expected to evolve through:

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Principles`

Public release should happen only after documentation, privacy, history, repository governance, and methodology consistency have been reviewed.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). During private incubation, changes should remain evidence-driven and conservative about expanding the core principle set.

## License

Licensed under the [Apache License 2.0](LICENSE).
