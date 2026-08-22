# Agentic Open-Source Engineering Methodology

> A practical, evolving methodology for designing, developing, verifying, maintaining, and evolving open-source software with AI agents.

[简体中文](README.zh-CN.md)

> **Status: v0.2 — private incubation.** The methodology is being tested and refined through real project work. It is an opinionated engineering methodology, not an industry standard.

## Why This Exists

AI agents are making software generation dramatically cheaper. The resulting bottleneck increasingly shifts toward engineering judgment: defining constraints, structuring repositories, validating changes, managing risk, preserving user control, and deciding when defaults should be overridden.

This repository develops a concise decision system for open-source projects in which humans and AI agents work together.

It aims to be:

- practical enough to change real repository decisions;
- explicit enough for developers and coding agents to follow;
- stable at the principle layer while allowing practices to evolve;
- lightweight enough for small teams and independent developers;
- open to adaptation rather than prescriptive about one stack or workflow.

## Who This Is For

The methodology is especially intended for:

- independent developers who use coding agents heavily;
- developers entering software engineering through AI-assisted development;
- technical AI product builders and product managers who work directly with prototypes, repositories, and coding agents;
- maintainers who want clearer human-agent collaboration without introducing a heavyweight process framework.

It assumes that AI agents can accelerate implementation but do not replace accountable engineering judgment.

## Meta-Principle

### Outcomes over Dogma

**Project outcomes come first. Principles guide engineering judgment; they do not replace it.**

When a default conflicts with the explicit goals, users, quality, security, performance, maintainability, or constraints of a project, use:

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

The principles intentionally mix durable values, engineering defaults, constraints, and preferred means. What makes them principles in this methodology is that they repeatedly change engineering decisions across projects. See [Principles](docs/principles.md).

## Methodology Structure

The methodology separates three operational layers and one governance layer:

1. **Principles** — durable values, defaults, constraints, and preferences that shape decisions;
2. **Decision Framework** — how to resolve conflicts, trade-offs, and justified exceptions;
3. **Practices** — how to implement the methodology in repositories, agent instructions, validation, contribution workflows, and releases;
4. **Governance** — how the methodology itself changes without drifting or accumulating rules for their own sake.

Start here:

- [Principles](docs/principles.md)
- [Decision Framework](docs/decision-framework.md)
- [Practices](docs/practices.md)
- [Governance](docs/governance.md)

## Using It in a Project

A lightweight adoption path is:

1. define the project purpose, users, constraints, and meaningful outcomes;
2. identify only the methodology defaults that materially affect the project;
3. adapt [`templates/AGENTS.md.template`](templates/AGENTS.md.template) into repository-level agent instructions;
4. use the [Project Review](templates/PROJECT_REVIEW.md) to expose important gaps without turning adoption into a certification exercise;
5. use the decision framework when defaults conflict;
6. record only higher-impact decisions that deserve durable evidence;
7. feed real failures and successes back into the methodology.

A lightweight [Decision Record](templates/DECISION_RECORD.md) is available for decisions that need more than a normal commit or pull-request explanation.

## Repository as Reference Implementation

This repository is also one of the methodology's test subjects. It should practice what it describes, while remaining proportionate to the fact that it is primarily a Markdown documentation repository.

It therefore favors:

- clear agent-facing instructions in [`AGENTS.md`](AGENTS.md);
- bilingual entry points and paired core methodology documents;
- lightweight automated validation rather than a large documentation toolchain;
- focused and reversible changes;
- explicit document responsibilities;
- minimal unnecessary dependencies and automation.

Run repository validation with:

```bash
python3 scripts/validate_repo.py
```

## Language Policy

English is the default language for repository operations and international open-source collaboration. Simplified Chinese is maintained as a first-class reading path for the README and core methodology documents.

Not every operational file is duplicated in both languages. Translation should improve actual accessibility, not exist only for symmetry. See [Governance](docs/governance.md#language-and-documentation-policy).

## Scope

This project focuses on engineering methodology for human-agent collaboration in open-source software.

It is **not** intended to be:

- a catalog of current AI products or models;
- a claim that all projects should use the same stack;
- a certification standard or compliance framework;
- a collection of invented case studies;
- a blog or content-marketing repository;
- a replacement for established software engineering, security, or open-source standards.

Tool-specific guidance belongs in the practice layer and may change rapidly.

## How It Evolves

The methodology is developed through real engineering feedback:

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Methodology`

External practices may inform the methodology, but they should be adopted only when they improve this project's decision system rather than because they are fashionable or widely used.

The repository remains private during incubation. A public release should happen only after a dedicated documentation, privacy, history, governance, and methodology-consistency review.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). During private incubation, changes should remain evidence-driven and conservative about expanding the core principle set.

## License

Licensed under the [Apache License 2.0](LICENSE).
