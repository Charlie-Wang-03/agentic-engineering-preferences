# AGENTS.md

## Purpose

This repository develops **Agentic Engineering Review**, an open, agent-executable engineering review system backed by the **Agentic Engineering Methodology**. AI agents should treat the repository as both product documentation and a lightweight reference implementation of the methodology and review protocol it describes.

This file governs agents **modifying this repository**. It is not the execution protocol for reviewing another project. External project reviews must follow [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md).

## Read First

Before making substantive changes, read the smallest relevant set of files:

1. `README.md` or `README.zh-CN.md`;
2. `docs/principles.md`;
3. `docs/decision-framework.md`;
4. `docs/practices.md` when changing implementation guidance;
5. `docs/governance.md` when changing the methodology itself, document policy, scoring policy, review protocol, or repository structure;
6. `AGENT_REVIEW_PROTOCOL.md` when changing external-review behavior;
7. `CONTRIBUTING.md` for contribution expectations.

Do not load or rewrite unrelated documents merely for completeness.

## Core Operating Rule

Follow **Outcomes over Dogma**:

> Principles guide engineering judgment; they do not replace it.

When a default conflicts with the project's explicit purpose, users, quality requirements, risk boundaries, maintainability needs, or current constraints, use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

Deviation is allowed; unexplained deviation is not.

## Repository Invariants

- Keep the product identity, Principles, Decision Framework, Practices, Governance, and the external Agent Review Protocol conceptually distinct.
- Do not conflate `AGENTS.md` with `AGENT_REVIEW_PROTOCOL.md`: repository maintenance and target-project review are different execution contexts.
- Do not add a core principle merely for completeness, trend coverage, or terminology symmetry.
- Distinguish values, defaults, constraints, decision rules, and preferred means when changing the principle layer.
- Do not present project-specific opinions as established industry consensus.
- Keep tool-, provider-, and model-specific guidance out of stable principles unless discussing a durable engineering concern.
- Preserve semantic alignment for the bilingual documents the repository explicitly promises to maintain.
- Do not duplicate every operational file in both languages merely for symmetry.
- Preserve review-protocol invariants unless evidence supports changing them: evidence before judgment, applicability before scoring, `N/A` without penalty, explicit insufficient-evidence handling, and read-only review by default.
- Diagnostic scores are summaries, not certification or cross-project rankings.
- Prefer focused, reviewable, reversible changes.
- Do not add `cases/` or `blog/` without an explicit repository-level decision.
- Do not add dependencies, frameworks, generated artifacts, or automation without demonstrated value.
- Remember that this is primarily a Markdown documentation repository; validation and process should remain proportional to its risk.
- Never commit secrets, private paths, private project data, credentials, or unpublished sensitive material.

## Document Responsibilities

Use the existing document boundaries instead of duplicating normative text:

- `README*` — product positioning, audience, scope, one-prompt entry, adoption path;
- `AGENT_REVIEW_PROTOCOL.md` — canonical external target-project review procedure, scoring formula, and output contract;
- `docs/principles*` — durable decision principles of the Agentic Engineering Methodology;
- `docs/decision-framework*` — trade-offs and exceptions;
- `docs/practices*` — implementation guidance;
- `docs/governance*` — methodology and review-protocol evolution;
- `AGENTS.md` — operational constraints for agents modifying this repository;
- `templates/PROJECT_REVIEW*` — human-readable review dimensions and diagnostic rubric;
- other `templates/` — reusable derived artifacts.

When a rule already has a canonical source, link to it or summarize it briefly rather than maintaining a second full copy.

## Bilingual Scope

Paired English / Simplified Chinese versions are expected for:

- the README;
- Principles;
- Decision Framework;
- Practices;
- Governance;
- user-facing templates where translation materially improves adoption.

Operational files such as `AGENTS.md` and `AGENT_REVIEW_PROTOCOL.md` may remain English-first unless a translation provides real value. The README should still provide a usable Chinese entry prompt.

## External Review Context

When asked to use Agentic Engineering Review to review a separate target project, do not apply the maintenance instructions in this file as the target-project protocol. Follow [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md) instead.

A target project may be local or remote, public or private, Git-based or not. Apply only materially relevant review dimensions and do not modify the target unless the user explicitly authorizes implementation.

## Agent Instructions as Scoped Context

For projects selectively adopting methodology-derived practices, prefer a concise root `AGENTS.md`. Add nested or scoped agent instructions only when a subsystem has materially different commands, invariants, or risks. Do not create instruction files for every directory by default.

## Validation Before Completion

Before declaring work complete:

1. inspect the resulting diff;
2. confirm the change belongs to the correct product, methodology, governance, or review-protocol layer;
3. check whether any promised bilingual pair is affected;
4. check links and derived artifacts when normative text changes;
5. if review behavior changed, check `README*`, `AGENT_REVIEW_PROTOCOL.md`, `templates/PROJECT_REVIEW*`, and scoring references for consistency;
6. run `python3 scripts/validate_repo.py`;
7. confirm no private or machine-specific information was introduced;
8. summarize any deliberate deviation from defaults.

## Change Philosophy

Prefer the smallest coherent change that meaningfully improves the review system, methodology, or their implementation. The repository should remain understandable to both human contributors and coding agents.

Self-consistency is a diagnostic tool: if practicing the methodology would require disproportionate machinery for this repository, reconsider the methodology or the practice before adding the machinery.
