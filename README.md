# Agentic Open-Source Engineering Methodology

> A practical, evolving methodology for designing, developing, verifying, maintaining, and evolving open-source software with AI agents.

[简体中文](README.zh-CN.md)

> **Status: v0.3 — private incubation.** The methodology is being tested and refined through real project work. It is an opinionated engineering methodology, not an industry standard.

## Review a Project with One Prompt

If your AI agent can access this repository and the target project, you can start with one prompt:

> **Review `<TARGET_PROJECT>` using the Agentic Open-Source Engineering Methodology at `https://github.com/Charlie-Wang-03/Agentic-Open-Source-Engineering-Methodology`. First read and follow `AGENT_REVIEW_PROTOCOL.md`. Inspect actual project evidence, adapt the methodology to what is applicable, give me the structured diagnostic score and evidence-backed findings, and do not modify the target unless I explicitly ask.**

`<TARGET_PROJECT>` may be the agent's current local workspace, a local project directory, a GitHub repository, another remote repository, or another project source the agent can actually inspect.

The target does **not** need to be open source or Git-based. The methodology remains oriented toward agentic open-source engineering, but the review protocol applies its dimensions selectively: genuinely irrelevant dimensions are marked `N/A` rather than treated as failures.

The review is evidence-first and read-only by default. See the canonical, tool-independent [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md).

If the agent cannot access either the methodology or material parts of the target, it should report the limitation rather than pretend to have completed a full review.

## Why This Exists

AI agents are making software generation dramatically cheaper. The resulting bottleneck increasingly shifts toward engineering judgment: defining constraints, structuring projects, validating changes, managing risk, preserving user control, and deciding when defaults should be overridden.

This repository develops a concise decision system primarily for open-source projects in which humans and AI agents work together, while also exposing a portable external-review protocol that can inspect broader project types where the methodology is materially applicable.

It aims to be:

- practical enough to change real engineering decisions;
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

Not every principle or review dimension is material to every target. Applicability must be determined from the target project's actual purpose and constraints before judging alignment.

## Methodology Structure

The methodology separates three operational layers and one governance layer:

1. **Principles** — durable values, defaults, constraints, and preferences that shape decisions;
2. **Decision Framework** — how to resolve conflicts, trade-offs, and justified exceptions;
3. **Practices** — how to implement the methodology in repositories, agent instructions, validation, contribution workflows, and releases;
4. **Governance** — how the methodology itself changes without drifting or accumulating rules for their own sake.

The external Agent Review Protocol is an execution interface over those sources; it does not create a new principle layer.

Start here:

- [Agent Review Protocol](AGENT_REVIEW_PROTOCOL.md) — execute a review of another project;
- [Principles](docs/principles.md) — durable decision defaults;
- [Decision Framework](docs/decision-framework.md) — trade-offs and justified exceptions;
- [Practices](docs/practices.md) — implementation guidance;
- [Governance](docs/governance.md) — evolution of the methodology itself.

## Two Ways to Use the Methodology

### 1. External Review — default

Keep the methodology outside the target project and use it at meaningful checkpoints such as:

- serious project start;
- major architecture or dependency decision;
- substantial refactor;
- preparation for public release;
- important release;
- post-incident or post-failure review.

The Agent Review Protocol produces an applicability-aware scorecard, evidence coverage, high-value gaps, accepted trade-offs, unresolved evidence needs, deferred concerns, and prioritized next actions.

The review should normally leave no methodology-specific files in the target project.

### 2. Selective Adoption — when useful

If a review exposes recurring project-specific needs, translate only those needs into the target project's own engineering artifacts.

For example:

- adapt [`templates/AGENTS.md.template`](templates/AGENTS.md.template) when clearer coding-agent context would materially help;
- use a [Decision Record](templates/DECISION_RECORD.md) for a high-impact decision that deserves durable evidence;
- add tests, validation, documentation, or safeguards because the target needs them—not merely to demonstrate methodology compliance.

Do not copy all principles or methodology files into every project.

## Diagnostic Scoring

The external review protocol provides a structured diagnostic score without turning the methodology into a certification framework.

For each applicable review dimension:

- applicability is classified as `Material`, `Relevant`, or `N/A`;
- evidence-backed dimensions receive a `0–4` score plus confidence;
- applicable dimensions with insufficient evidence are marked `NE` rather than guessed;
- `N/A` dimensions do not reduce the score;
- an overall `/100` Diagnostic Score is issued only when weighted Evidence Coverage reaches at least 70%.

The score summarizes the inspected state. It does not replace findings, does not erase critical individual gaps, and should not be used as a universal benchmark across unrelated projects.

See [Project Review](templates/PROJECT_REVIEW.md) and the [Agent Review Protocol](AGENT_REVIEW_PROTOCOL.md).

## Repository as Reference Implementation

This repository is also one of the methodology's test subjects. It should practice what it describes, while remaining proportionate to the fact that it is primarily a Markdown documentation repository.

It therefore favors:

- clear separation between [`AGENTS.md`](AGENTS.md), which governs work on this repository, and [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md), which governs reviews of external target projects;
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

The Agent Review Protocol remains a single English canonical operational file; reviews should normally be written in the user's language. Not every operational file is duplicated in both languages. Translation should improve actual accessibility, not exist only for symmetry. See [Governance](docs/governance.md#language-and-documentation-policy).

## Scope

This project focuses on engineering methodology for human-agent collaboration in open-source software. Its external review protocol can also examine private, local, internal, or non-Git projects by applying only the dimensions that materially fit the target.

It is **not** intended to be:

- a catalog of current AI products or models;
- a claim that all projects should use the same stack;
- a certification standard or compliance framework;
- a security audit substitute;
- a collection of invented case studies;
- a blog or content-marketing repository;
- a replacement for established software engineering, security, or open-source standards.

Tool-specific guidance belongs in the practice layer and may change rapidly.

## How It Evolves

The methodology is developed through real engineering feedback:

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Methodology`

External practices may inform the methodology, but they should be adopted only when they improve this project's decision system rather than because they are fashionable or widely used.

The repository remains private during incubation. A public release should happen only after a dedicated documentation, privacy, history, governance, methodology-consistency, and cross-agent review-protocol test.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). During private incubation, changes should remain evidence-driven and conservative about expanding the core principle set.

## License

Licensed under the [Apache License 2.0](LICENSE).
