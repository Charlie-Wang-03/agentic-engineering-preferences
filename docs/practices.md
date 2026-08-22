# Practices

[简体中文](practices.zh-CN.md)

Practices are the fast-moving implementation layer of the methodology. They translate durable principles and decision rules into repository behavior.

Unlike the core principles, practices may change as tools, agent capabilities, hosting platforms, and engineering conventions evolve.

## 1. Repository Context for Agents

Provide clear repository-level instructions for coding agents.

Prefer:

- a concise root `AGENTS.md` or equivalent repository instruction file;
- explicit validation commands;
- clear directory responsibilities and repository invariants;
- explicit completion criteria;
- documented high-risk or destructive operations;
- minimal reliance on unwritten local knowledge.

Agent instructions should explain goals, constraints, invariants, and verification paths without prescribing unnecessary implementation detail.

For larger repositories, scoped or nested agent instructions may be useful when a subsystem has genuinely different commands, constraints, or invariants. Do not create instruction files for every directory merely because the mechanism exists.

## 2. Documentation Responsibilities

Give each document a clear job instead of turning one file into a universal source of detail.

A useful default is:

- `README.md` — discovery, audience, scope, and adoption path;
- `docs/principles*` — durable engineering principles;
- `docs/decision-framework*` — conflict and exception handling;
- `docs/practices*` — implementation guidance that may evolve faster;
- `docs/governance*` — how the methodology itself changes;
- `AGENTS.md` — agent operating constraints for this repository;
- `CONTRIBUTING.md` — contribution workflow and expectations;
- `templates/` — reusable derived artifacts.

Avoid duplicating the same normative text across multiple files. Link to the canonical document instead.

## 3. Language and Translation

Use bilingual documentation where it materially improves access, not as a requirement for every repository file.

For this methodology repository, maintain English and Simplified Chinese pairs for:

- the README;
- core methodology documents intended for regular human reading;
- user-facing templates when the translation has practical value.

Operational files such as `AGENTS.md`, workflow configuration, or contribution mechanics may remain English-first unless a translation materially improves usability.

Keep paired documents semantically aligned, but write naturally in each language rather than forcing literal translation.

## 4. Verifiable Changes

Prefer changes that have a clear verification path.

Depending on the repository, verification may include:

- tests;
- linting;
- type checking;
- deterministic scripts;
- schema validation;
- documentation structure or link checks;
- reproducible examples;
- CI checks.

Verification should be proportional to the repository and the risk. Do not add validation machinery whose maintenance cost exceeds the risk it controls.

## 5. Reviewable and Reversible Work

Keep changes focused enough to understand and recover from.

Prefer:

- small or coherent commits;
- feature branches for non-trivial work;
- pull requests for reviewable changes;
- explicit rollback paths for risky migrations;
- backups or dry-runs for destructive operations.

Large agent-generated rewrites require stronger review and validation than localized edits.

## 6. Dependency Discipline

Before adding a dependency, identify:

- the problem it solves;
- why existing capabilities are insufficient;
- installation and maintenance cost;
- security and supply-chain exposure;
- replacement cost;
- portability impact.

Prefer mature external infrastructure over fragile reimplementation when the dependency is justified. For documentation-only repositories, keep the tooling baseline especially small unless stronger automation solves a demonstrated problem.

## 7. Privacy and Repository Hygiene

Keep private and public material intentionally separated.

At minimum:

- do not commit credentials or secrets;
- avoid machine-specific private paths;
- keep unpublished or private project data out of public artifacts;
- document external data transmission when it matters;
- use least-necessary permissions for agents and automation;
- review Git history before making a previously private repository public.

## 8. Progressive User Experience

Design onboarding in layers.

A newcomer should be able to answer quickly:

1. What is this project?
2. Who is it for?
3. What is the smallest useful way to adopt or try it?
4. What are the major assumptions or limitations?
5. Where can advanced or internal details be found?

Do not force advanced architecture or every methodology concept into the initial adoption path.

## 9. Project Review

Use a lightweight project review to expose missing engineering decisions before adding more process.

The review should ask about purpose, users, agent context, privacy boundaries, dependencies, validation, reversibility, portability, and onboarding. It is a diagnostic aid, not a certification score.

See [`templates/PROJECT_REVIEW.md`](../templates/PROJECT_REVIEW.md).

## 10. Decision Records

Use formal decision records only when the decision merits them.

For ordinary work, a clear PR or commit explanation is enough. For higher-impact deviations, record the default, conflict, trade-off, exception, evidence, rollback considerations, and revisit condition.

See [`templates/DECISION_RECORD.md`](../templates/DECISION_RECORD.md).

## 11. Release Readiness

Before a public release or visibility change, review:

- license and attribution;
- README and onboarding;
- language coverage that the project actually promises;
- secrets and private data;
- repository history;
- dependencies;
- validation status;
- contribution and conduct guidance;
- release scope and known limitations.

Public release is an engineering decision, not merely a repository setting change.

## 12. Evolving Practices

Practices should be updated when real project experience or tooling changes justify it.

External repositories can provide useful mechanisms and examples, but adoption should be selective. Do not import a process, file structure, tool, or convention only because a prominent project uses it.

Do not promote a tool-specific practice into a stable principle unless it represents a durable engineering concern independent of the tool itself.
