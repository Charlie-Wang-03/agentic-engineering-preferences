# Practices

[简体中文](practices.zh-CN.md)

Practices are the fast-moving implementation layer of the methodology. They translate stable principles and decision rules into repository behavior.

Unlike the core principles, practices may change as tools, agent capabilities, hosting platforms, and engineering conventions evolve.

## 1. Repository Context for Agents

Provide clear repository-level instructions for coding agents.

Prefer:

- a concise `AGENTS.md` or equivalent repository instruction file;
- explicit commands for validation;
- clear directory responsibilities;
- explicit completion criteria;
- documented high-risk or destructive operations;
- minimal reliance on unwritten local knowledge.

Agent instructions should explain goals and constraints without prescribing unnecessary implementation detail.

## 2. Bilingual Documentation

For major normative documents, keep English and Simplified Chinese as first-class versions.

Prefer paired files such as:

- `README.md` / `README.zh-CN.md`;
- `docs/principles.md` / `docs/principles.zh-CN.md`.

Keep semantics aligned, but write naturally in each language instead of forcing literal translation.

## 3. Verifiable Changes

Prefer changes that have a clear verification path.

Depending on the repository, verification may include:

- tests;
- linting;
- type checking;
- deterministic scripts;
- schema validation;
- documentation structure checks;
- reproducible examples;
- CI checks.

Do not add validation machinery whose maintenance cost exceeds the risk it controls.

## 4. Reviewable and Reversible Work

Keep changes focused enough to understand and recover from.

Prefer:

- small or coherent commits;
- feature branches for non-trivial work;
- pull requests for reviewable changes;
- explicit rollback paths for risky migrations;
- backups or dry-runs for destructive operations.

Large agent-generated rewrites require stronger review and validation than localized edits.

## 5. Dependency Discipline

Before adding a dependency, identify:

- the problem it solves;
- why existing capabilities are insufficient;
- installation and maintenance cost;
- security and supply-chain exposure;
- replacement cost;
- portability impact.

Prefer mature external infrastructure over fragile reimplementation when the dependency is justified.

## 6. Privacy and Repository Hygiene

Keep private and public material intentionally separated.

At minimum:

- do not commit credentials or secrets;
- avoid machine-specific private paths;
- keep unpublished or private project data out of public artifacts;
- document external data transmission when it matters;
- use least-necessary permissions for agents and automation;
- review Git history before making a previously private repository public.

## 7. Progressive User Experience

Design onboarding in layers.

A newcomer should be able to answer quickly:

1. What is this project?
2. Who is it for?
3. What is the fastest safe way to try it?
4. What are the major assumptions or limitations?
5. Where can advanced configuration or internal details be found?

Do not force advanced architecture into the quick-start path.

## 8. Decision Records

Use formal decision records only when the decision merits them.

For ordinary work, a clear PR or commit explanation is enough. For higher-impact deviations, record the default, conflict, trade-off, exception, evidence, rollback considerations, and revisit condition.

The repository includes a lightweight decision-record template for this purpose.

## 9. Release Readiness

Before a public release or visibility change, review:

- license and attribution;
- README and onboarding;
- bilingual consistency;
- secrets and private data;
- repository history;
- dependencies;
- validation status;
- contribution and conduct guidance;
- release scope and known limitations.

Public release is an engineering decision, not merely a repository setting change.

## 10. Evolving Practices

Practices should be updated when real project experience or tooling changes justify it.

Do not promote a tool-specific practice into a stable principle unless it represents a durable engineering concern independent of the tool itself.
