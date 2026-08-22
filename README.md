<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="Agentic Engineering Review — an evidence-first review protocol for AI agents">
</p>

# Agentic Engineering Review

> Let your AI agent review a software project with evidence, applicability-aware scoring, explicit trade-offs, and prioritized next actions.

[简体中文](README.zh-CN.md)

> **Status: v0.4 — private incubation.** The review protocol and underlying methodology are being validated through real project work. This is an opinionated engineering system, not an industry standard or certification framework.

## Review a Project with One Prompt

If your AI agent can access this repository and the target project, start with:

> **Review `<TARGET_PROJECT>` using Agentic Engineering Review at `https://github.com/Charlie-Wang-03/agentic-engineering-review`. First read and follow `AGENT_REVIEW_PROTOCOL.md`. Inspect actual project evidence, determine which review dimensions materially apply, give me the structured Diagnostic Score and evidence-backed findings, and do not modify the target unless I explicitly ask.**

`<TARGET_PROJECT>` can be:

- the agent's current local workspace;
- a local project directory;
- a GitHub or other remote repository;
- a private or internal project the agent can actually inspect;
- a non-Git project source with sufficient accessible evidence.

The canonical, tool-independent execution contract is [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md). Reviews are **read-only by default**.

## What You Get

A normal review produces:

- an applicability-aware **0–100 Diagnostic Score** when evidence coverage is sufficient;
- **Evidence Coverage** so missing evidence is visible rather than guessed away;
- the highest-value engineering gaps worth fixing now;
- accepted trade-offs that should remain as they are;
- unresolved questions that need more evidence;
- deliberately deferred concerns where remediation costs more than it is worth;
- three to five prioritized next actions.

The score is a compact diagnostic summary, not certification and not a benchmark for comparing unrelated projects.

## How It Works

```text
Target Project
    ↓
Your AI Agent
    ↓
Agent Review Protocol
    ↓
Evidence → Applicability → Engineering Judgment → Trade-offs
    ↓
Structured Review
```

The protocol requires the agent to:

1. resolve what project state it can actually inspect;
2. understand the project's purpose, users, constraints, and maturity before judging it;
3. inspect real evidence rather than trusting branding or README claims alone;
4. mark each review dimension as `Material`, `Relevant`, or `N/A` before scoring;
5. use `NE — Not Enough Evidence` instead of inventing certainty;
6. distinguish real gaps from justified engineering trade-offs;
7. remain read-only unless the user separately authorizes implementation.

## Built for Agent-Heavy Project Work

Agentic Engineering Review is especially useful for:

- **AI-native builders** — independent developers and engineers who rely heavily on coding agents;
- **technical product builders** — AI product managers, prototypers, and independent AI developers working directly with repositories and agents;
- **FDE / solution engineers** — people operating across customer environments, deployment constraints, providers, permissions, data boundaries, and fast-changing project requirements;
- maintainers who want stronger engineering judgment without introducing a heavyweight compliance process.

The target does not need to be open source. Review dimensions that do not materially apply are marked `N/A` rather than treated as failures.

## Why It Is Different

### Evidence before judgment

The agent should inspect implementation, configuration, tests, CI, dependencies, history, runtime evidence, or other relevant project material before making broad claims.

### Applicability before scoring

The system does not force every project through the same checklist. A private internal project may reasonably treat openness as `N/A`; a static documentation project may have no meaningful local/remote runtime boundary.

### Trade-offs, not compliance

A non-default choice is not automatically a defect. Material deviations use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

A proprietary solver, cloud platform, or provider can be the correct engineering choice when the evidence supports it.

### Agent-executable, human-accountable

The protocol is written so capable AI agents can execute it directly, but engineering responsibility remains human. The agent produces structured judgment support; it does not replace accountable project decisions.

## Diagnostic Scoring

Each applicable dimension receives an applicability state first:

| Applicability | Meaning | Weight |
| --- | --- | ---: |
| `Material` | Meaningfully affects project outcomes or risk | 2 |
| `Relevant` | Worth reviewing but secondary | 1 |
| `N/A` | Not meaningfully applicable | excluded |

Evidence-backed applicable dimensions are scored from `0` to `4` and assigned `High`, `Medium`, or `Low` confidence. Applicable dimensions without enough evidence are `NE` instead of receiving a guessed score.

An overall `/100` Diagnostic Score is issued only when weighted **Evidence Coverage ≥ 70%**. See the exact rules in the [Agent Review Protocol](AGENT_REVIEW_PROTOCOL.md) and the human-readable [Project Review](templates/PROJECT_REVIEW.md).

## Powered by an Agentic Engineering Methodology

The review system is backed by a methodology that is readable by both humans and agents.

Its meta-principle is **Outcomes over Dogma**:

> **Project outcomes come first. Principles guide engineering judgment; they do not replace it.**

The nine current principles are:

1. **Open by Default**
2. **Agent-Native, Human-Accountable**
3. **Portable over Model-Agnostic**
4. **User Sovereignty & Privacy by Default**
5. **Local-First When Practical**
6. **Justified Dependencies**
7. **Progressive Usability**
8. **Verifiable by Default**
9. **Reversible Change**

They intentionally mix durable values, engineering defaults, constraints, decision rules, and preferred means. They are applied selectively according to the target project's real purpose and constraints.

## Two Ways to Use It

### 1. External Review — default

Keep this repository outside the target project and invoke it at meaningful checkpoints such as:

- serious project start;
- major architecture or dependency decisions;
- substantial refactors;
- preparation for public release;
- important releases;
- post-incident or post-failure review.

A normal external review leaves no methodology-specific files in the target project.

### 2. Selective Adoption — when useful

If a review exposes recurring project-specific needs, translate only those needs into the target project's own engineering artifacts. For example:

- adapt [`templates/AGENTS.md.template`](templates/AGENTS.md.template) when coding-agent context is genuinely weak;
- use a [Decision Record](templates/DECISION_RECORD.md) for a high-impact choice that deserves durable evidence;
- add tests, validation, safeguards, or documentation because the target needs them—not to improve a methodology score.

Do not copy the full methodology into every project.

## Go Deeper

| Resource | Purpose |
| --- | --- |
| [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md) | Canonical agent-executable review procedure and output contract |
| [Principles](docs/principles.md) | Durable engineering defaults and values |
| [Decision Framework](docs/decision-framework.md) | Trade-offs, exceptions, evidence, and revisit rules |
| [Practices](docs/practices.md) | Faster-moving implementation guidance |
| [Governance](docs/governance.md) | How the methodology and protocol evolve |
| [Project Review](templates/PROJECT_REVIEW.md) | Human-readable review dimensions and scoring rubric |

## Limits

Agentic Engineering Review is **not**:

- a security certification or substitute for a dedicated security audit;
- a compliance framework;
- a guarantee of software quality;
- a universal maturity benchmark across unrelated projects;
- a requirement to use one model, agent, platform, or stack;
- permission for an agent to modify a target project merely because a review was requested.

If an agent cannot access important methodology or target-project evidence, it should report the limitation and degrade the review rather than fabricate completeness.

## Repository Status

This repository is also one of the system's own test subjects. It intentionally remains Markdown-first, with a small standard-library validator rather than a heavy documentation stack.

Run:

```bash
python3 scripts/validate_repo.py
```

English is the default operational language. Simplified Chinese is maintained as a first-class reading path for the README and core methodology documents. The canonical Agent Review Protocol remains English-first; review output should normally follow the user's language.

The repository remains private during incubation. Public release should happen only after dedicated methodology, documentation, privacy, Git-history, governance, and cross-agent protocol validation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should improve real engineering decisions, review reliability, or adoption rather than add process for its own sake.

## License

Licensed under the [Apache License 2.0](LICENSE).
