# AGENTS.md

## Repository Purpose

This repository maintains **Agentic Engineering Preferences**: a public personal reference for recurring engineering preferences, decision rules, and project conventions used in AI-assisted software development.

It is intentionally personal rather than universal. Do not turn a maintainer preference into an industry best practice, standard, or compliance rule.

## Priority of Instructions

When these preferences are used in another project, the target project's own goals, evidence, constraints, and repository-local instructions take precedence.

For work on this repository itself, this file is the repository-local instruction source.

## Read First

Before substantive changes, read the smallest relevant set:

1. README.md or README.zh-CN.md;
2. docs/preferences.md when changing durable engineering tendencies;
3. docs/decision-rules.md when changing recurring decision guidance;
4. docs/project-conventions.md when changing implementation conventions;
5. CONTRIBUTING.md for contribution boundaries.

Do not load unrelated files merely for completeness.

## Document Responsibilities

- README files — product identity, scope, use model, and history;
- docs/preferences.md — relatively stable engineering preferences;
- docs/decision-rules.md — recurring engineering decisions;
- docs/project-conventions.md — practical implementation conventions;
- templates/AGENTS.md.template — reusable project-local agent instruction template;
- AGENTS.md — instructions for modifying this repository.

Avoid duplicating normative text across files.

## Editing Principles

- Prefer rules that reduce repeated engineering decisions or repeated agent communication.
- Do not add a rule solely because it is fashionable, common in industry, or supported by a new tool.
- Do not optimize for taxonomy completeness or symmetry.
- Prefer concrete defaults with clear boundaries over abstract slogans.
- Keep project-local context authoritative over generic preferences.
- Keep changes coherent, reviewable, and easy to reverse.
- Never introduce secrets, private paths, private project data, credentials, or unpublished sensitive material.
- Do not reintroduce retired project-scoring or generic review-protocol machinery into the current core.

## Adding or Changing Preferences

A new preference or decision rule should normally satisfy at least one of these:

- it has recurred across real project work;
- it repeatedly changes engineering decisions;
- it repeatedly costs time to re-explain to coding agents;
- it protects an important boundary such as privacy, reversibility, or validation.

If a rule only matters to one project, keep it in that project's own instructions.

## High-Risk Operations

Do not perform the following without explicit maintainer authorization:

- repository deletion or visibility changes;
- force push or history rewrite;
- release or tag creation;
- branch-protection, ruleset, or permission changes;
- secret or credential operations;
- destructive migrations;
- large irreversible restructuring.

## Validation

Before declaring repository work complete:

1. inspect the resulting diff;
2. run python3 scripts/validate_repo.py;
3. check affected links and README language entry points;
4. verify no private or machine-specific material was introduced;
5. check that the change reduces complexity rather than recreating retired methodology machinery.

## Definition of Done

A change is complete when its intent is clear, the relevant document owns the rule, validation passes, and the repository remains easier—not harder—for a capable agent or human maintainer to use.
