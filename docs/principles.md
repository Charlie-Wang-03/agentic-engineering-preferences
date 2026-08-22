# Principles

[简体中文](principles.zh-CN.md)

This document defines the stable value layer of the Agentic Open-Source Engineering Methodology. These principles are strong defaults, not absolute laws.

## Meta-Principle: Outcomes over Dogma

Project outcomes come first. Principles improve engineering judgment; they do not replace it.

When principles conflict with one another or with user value, quality, security, performance, or maintainability, an explicit trade-off is allowed. Use the decision framework rather than following a principle mechanically.

> **Deviation is allowed; unexplained deviation is not.**

## 1. Open by Default

Prefer open-source-compatible choices, clear licensing, open formats and interfaces, understandable repository structures, interoperability, and contribution-friendly practices.

Open by Default does not mean every artifact must be public. Private incubation, embargoed research, security-sensitive information, credentials, and user data may require controlled access.

## 2. Agent-Native, Human-Accountable

Design repositories so AI agents can understand, modify, test, verify, document, and maintain them with minimal hidden context.

Prefer explicit structure, commands, constraints, acceptance criteria, and machine-readable guidance. Agent-native does not mean "AI-generated" and does not remove human responsibility. Humans remain accountable for project decisions and released outcomes.

## 3. Portable over Model-Agnostic

Avoid unnecessary lock-in to a model, agent product, cloud platform, or toolchain. Prefer clear and replaceable boundaries.

Do not force all implementations down to the lowest common denominator. A portable core may coexist with provider- or tool-specific optimizations when they produce meaningful value.

## 4. User Sovereignty & Privacy by Default

Users should retain meaningful control over their data, credentials, model choice, agent choice, execution environment, and generated artifacts.

Minimize unnecessary data transmission, permissions, telemetry, credential exposure, private-path leakage, and mixing of private material with public outputs.

## 5. Local-First When Practical

Prefer local execution when it materially improves privacy, autonomy, reproducibility, offline capability, or resilience without imposing unreasonable capability, maintenance, or usability costs.

Local-first is not local-only. Cloud services are acceptable when they are the better engineering choice, provided dependencies and relevant data flows are transparent.

## 6. Justified Dependencies

Every dependency should earn its place.

Evaluate what problem it solves, implementation cost, maturity, maintenance activity, security exposure, installation burden, replacement cost, and long-term maintenance impact. Do not reimplement mature infrastructure merely to reduce dependency count.

## 7. Progressive Usability

Keep simple tasks simple while allowing advanced users to access greater complexity when needed.

Prefer clear quick starts, sensible defaults, low initial cognitive load, progressive disclosure, and documentation that remains usable for newcomers, including developers entering software engineering through AI agents.

## 8. Verifiable by Default

Prefer work that can be checked by tools rather than trusted by appearance.

Use tests, linting, type checks, deterministic commands, validation scripts, CI, acceptance criteria, and reproducible examples where they provide real value.

> **Agent-generated work should be verifiable by tools, not trusted by appearance.**

## 9. Reversible Change

Prefer changes with controlled blast radius and clear recovery paths.

Use version control, focused commits, reviewable diffs, checkpoints, backups, dry-runs, reversible migrations, destructive-operation safeguards, and generated-artifact isolation when appropriate.

## Evolving the Principles

A new principle should not be added because it sounds desirable or completes a checklist. It should address a recurring engineering decision that is not adequately handled by the existing principles or decision framework.

The intended evolution loop is:

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Principles`
