# AGENTS.md

## Purpose

This repository develops the **Agentic Open-Source Engineering Methodology**. AI agents should treat the repository as both documentation and a lightweight reference implementation of the methodology it describes.

## Read First

Before making substantive changes, read the smallest relevant set of files:

1. `README.md` or `README.zh-CN.md`;
2. `docs/principles.md`;
3. `docs/decision-framework.md`;
4. `docs/practices.md` when changing implementation guidance;
5. `docs/governance.md` when changing the methodology itself, document policy, or repository structure;
6. `CONTRIBUTING.md` for contribution expectations.

Do not load or rewrite unrelated documents merely for completeness.

## Core Operating Rule

Follow **Outcomes over Dogma**:

> Principles guide engineering judgment; they do not replace it.

When a default conflicts with the project's explicit purpose, users, quality requirements, risk boundaries, maintainability needs, or current constraints, use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

Deviation is allowed; unexplained deviation is not.

## Repository Invariants

- Keep Principles, Decision Framework, Practices, and Governance conceptually distinct.
- Do not add a core principle merely for completeness, trend coverage, or terminology symmetry.
- Distinguish values, defaults, constraints, decision rules, and preferred means when changing the principle layer.
- Do not present project-specific opinions as established industry consensus.
- Keep tool-, provider-, and model-specific guidance out of stable principles unless discussing a durable engineering concern.
- Preserve semantic alignment for the bilingual documents the repository explicitly promises to maintain.
- Do not duplicate every operational file in both languages merely for symmetry.
- Prefer focused, reviewable, reversible changes.
- Do not add `cases/` or `blog/` without an explicit repository-level decision.
- Do not add dependencies, frameworks, generated artifacts, or automation without demonstrated value.
- Remember that this is primarily a Markdown documentation repository; validation and process should remain proportional to its risk.
- Never commit secrets, private paths, private project data, credentials, or unpublished sensitive material.

## Document Responsibilities

Use the existing document boundaries instead of duplicating normative text:

- `README*` — positioning, audience, scope, adoption path;
- `docs/principles*` — durable decision principles;
- `docs/decision-framework*` — trade-offs and exceptions;
- `docs/practices*` — implementation guidance;
- `docs/governance*` — methodology evolution;
- `AGENTS.md` — operational constraints for agents;
- `templates/` — reusable derived artifacts.

When a rule already has a canonical source, link to it or summarize it briefly rather than maintaining a second full copy.

## Bilingual Scope

Paired English / Simplified Chinese versions are expected for:

- the README;
- Principles;
- Decision Framework;
- Practices;
- Governance;
- user-facing templates where translation materially improves adoption.

Operational files may remain English-first unless a translation provides real value.

## Agent Instructions as Scoped Context

For projects adopting this methodology, prefer a concise root `AGENTS.md`. Add nested or scoped agent instructions only when a subsystem has materially different commands, invariants, or risks. Do not create instruction files for every directory by default.

## Validation Before Completion

Before declaring work complete:

1. inspect the resulting diff;
2. confirm the change belongs to the correct methodology or governance layer;
3. check whether any promised bilingual pair is affected;
4. check links and derived artifacts when normative text changes;
5. run `python3 scripts/validate_repo.py`;
6. confirm no private or machine-specific information was introduced;
7. summarize any deliberate deviation from defaults.

## Change Philosophy

Prefer the smallest coherent change that meaningfully improves the methodology or its implementation. The repository should remain understandable to both human contributors and coding agents.

Self-consistency is a diagnostic tool: if practicing the methodology would require disproportionate machinery for this repository, reconsider the methodology or the practice before adding the machinery.
