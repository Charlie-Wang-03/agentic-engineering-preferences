# AGENTS.md

## Purpose

This repository develops the **Agentic Open-Source Engineering Methodology**. AI agents should treat the repository as both documentation and a reference implementation of the methodology it describes.

## Read First

Before making substantive changes, read:

1. `README.md` or `README.zh-CN.md`;
2. `docs/principles.md`;
3. `docs/decision-framework.md`;
4. `CONTRIBUTING.md`.

## Core Operating Rule

Follow **Outcomes over Dogma**:

> Principles guide engineering judgment; they do not replace it.

When a default conflicts with project quality, user value, security, maintainability, or another principle, use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

Deviation is allowed; unexplained deviation is not.

## Repository Rules

- Keep Principles, Decision Framework, and Practices conceptually separate.
- Do not add a new core principle merely for completeness or trend coverage.
- Do not present project-specific opinions as established industry consensus.
- Keep tool-, provider-, and model-specific guidance out of stable principles unless the text is explicitly discussing a practice.
- Preserve bilingual semantic equivalence for major normative documents.
- Prefer focused, reviewable, reversible changes.
- Do not add `cases/` or `blog/` without an explicit repository-level decision.
- Do not add unnecessary dependencies, frameworks, generated artifacts, or automation.
- Never commit secrets, private paths, private project data, credentials, or unpublished sensitive material.

## Bilingual Documentation

For paired documents such as:

- `README.md` / `README.zh-CN.md`
- `docs/principles.md` / `docs/principles.zh-CN.md`
- `docs/decision-framework.md` / `docs/decision-framework.zh-CN.md`

make sure that important rules and factual claims remain semantically aligned. Do not force literal translation when natural technical phrasing differs by language.

## Validation Before Completion

Before declaring work complete:

1. inspect the resulting diff;
2. confirm the change belongs to the correct methodology layer;
3. check paired-language impact;
4. run available repository validation;
5. confirm no private or machine-specific information was introduced;
6. summarize any deliberate deviation from defaults.

## Change Philosophy

Prefer the smallest change that meaningfully improves the methodology or its implementation. The repository should remain understandable to both human contributors and coding agents.
