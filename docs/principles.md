# Principles

[简体中文](principles.zh-CN.md)

This document defines the durable decision principles of the Agentic Open-Source Engineering Methodology. They are strong defaults, not absolute laws.

The principles are intentionally not all the same kind of concept. Some express values, some define engineering defaults or preferences, some act as constraints, and some describe preferred means. They belong at the principle layer only when they repeatedly change engineering decisions across projects and remain meaningful as specific tools change.

## Meta-Principle: Outcomes over Dogma

Project outcomes come first. Principles improve engineering judgment; they do not replace it.

The relevant outcome is the explicit purpose, users, quality attributes, constraints, and engineering goals of the project under current conditions. When principles conflict with one another or with those outcomes, an explicit trade-off is allowed. Use the decision framework rather than following a principle mechanically.

> **Deviation is allowed; unexplained deviation is not.**

## Conceptual Roles

The labels below clarify what each principle mainly contributes; they are not additional methodology layers.

| Principle | Primary role |
| --- | --- |
| Open by Default | ecosystem value and default |
| Agent-Native, Human-Accountable | design default and accountability constraint |
| Portable over Model-Agnostic | architecture preference |
| User Sovereignty & Privacy by Default | user value and safety constraint |
| Local-First When Practical | execution preference / means |
| Justified Dependencies | engineering decision rule |
| Progressive Usability | product and documentation preference |
| Verifiable by Default | quality default |
| Reversible Change | risk-control default |

## 1. Open by Default

Prefer open-source-compatible choices, clear licensing, open formats and interfaces, understandable repository structures, interoperability, and contribution-friendly practices.

This principle is primarily about the project's relationship with its ecosystem, users, and contributors. Portability of particular models, providers, or tools is handled more specifically by **Portable over Model-Agnostic**.

Open by Default does not mean every artifact must be public. Private incubation, embargoed research, security-sensitive information, credentials, and user data may require controlled access.

## 2. Agent-Native, Human-Accountable

Design repositories so AI agents can understand, modify, test, verify, document, and maintain them with minimal hidden context.

Prefer explicit structure, commands, constraints, acceptance criteria, repository invariants, and machine-readable guidance. Agent-native is about machine executability; it is distinct from **Progressive Usability**, which focuses on human onboarding and cognitive load.

Agent-native does not mean "AI-generated" and does not remove human responsibility. Humans remain accountable for project decisions and released outcomes.

## 3. Portable over Model-Agnostic

Avoid unnecessary lock-in to a model, agent product, cloud platform, or toolchain. Prefer clear and replaceable boundaries where replacement has plausible value.

Do not force all implementations down to the lowest common denominator or build abstraction layers whose cost exceeds their portability benefit. A portable core may coexist with provider- or tool-specific optimizations when they produce meaningful value.

## 4. User Sovereignty & Privacy by Default

Users should retain meaningful control over their data, credentials, model choice, agent choice, execution environment, and generated artifacts.

Minimize unnecessary data transmission, permissions, telemetry, credential exposure, private-path leakage, and mixing of private material with public outputs.

This principle defines the desired user-control and privacy outcome. **Local-First When Practical** is one possible means of supporting it, not its definition.

## 5. Local-First When Practical

Prefer local execution when it materially improves privacy, autonomy, reproducibility, offline capability, or resilience without imposing unreasonable capability, maintenance, or usability costs.

Local-first is not local-only and does not by itself guarantee privacy or user sovereignty. Cloud services are acceptable when they are the better engineering choice, provided dependencies and relevant data flows are transparent.

## 6. Justified Dependencies

Every dependency should earn its place.

Evaluate what problem it solves, implementation cost, maturity, maintenance activity, security exposure, installation burden, replacement cost, portability impact, and long-term maintenance impact.

Do not reimplement mature infrastructure merely to reduce dependency count, and do not add tooling merely to make a project appear more engineered than its risk profile requires.

## 7. Progressive Usability

Keep simple tasks simple while allowing advanced users to access greater complexity when needed.

Prefer clear quick starts, sensible defaults, low initial cognitive load, progressive disclosure, and documentation that remains usable for newcomers, including people entering software development through AI agents.

This principle is primarily human-facing. Agent-specific context and execution constraints belong under **Agent-Native, Human-Accountable**.

## 8. Verifiable by Default

Prefer work that can be checked by tools rather than trusted by appearance.

Use tests, linting, type checks, deterministic commands, validation scripts, CI, acceptance criteria, and reproducible examples where they provide real value relative to the risk being controlled.

> **Agent-generated work should be verifiable by tools, not trusted by appearance.**

Verification answers: **How do we know the change is acceptable?**

## 9. Reversible Change

Prefer changes with controlled blast radius and clear recovery paths.

Use version control, focused commits, reviewable diffs, checkpoints, backups, dry-runs, reversible migrations, destructive-operation safeguards, and generated-artifact isolation when appropriate.

Reversibility answers a different question from verification: **What happens if the change is wrong or conditions change?**

## Evolving the Principles

A new principle should not be added because it sounds desirable or completes a checklist. It should address a recurring engineering decision that is not adequately handled by the existing principles or decision framework.

Before adding one, distinguish whether the proposal is actually a value, default, constraint, preferred means, decision rule, or fast-moving practice. Not every useful rule belongs at the principle layer.

The intended evolution loop is:

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Methodology`
