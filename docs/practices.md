# Practices

[简体中文](practices.zh-CN.md)

Practices are the fast-moving implementation layer of the methodology. They translate durable principles and decision rules into project behavior.

Unlike the core principles, practices may change as tools, agent capabilities, hosting platforms, and engineering conventions evolve.

## 1. Project Context for Agents

Provide clear project-level instructions for coding agents when they materially help.

Prefer:

- a concise root `AGENTS.md` or equivalent project instruction file;
- explicit validation commands;
- clear directory responsibilities and project invariants;
- explicit completion criteria;
- documented high-risk or destructive operations;
- minimal reliance on unwritten local knowledge.

Agent instructions should explain goals, constraints, invariants, and verification paths without prescribing unnecessary implementation detail.

For larger projects, scoped or nested agent instructions may be useful when a subsystem has genuinely different commands, constraints, or invariants. Do not create instruction files for every directory merely because the mechanism exists.

## 2. Documentation Responsibilities

Give each document a clear job instead of turning one file into a universal source of detail.

For this methodology repository, a useful separation is:

- `README.md` — discovery, audience, scope, and adoption path;
- `AGENT_REVIEW_PROTOCOL.md` — canonical execution protocol for reviewing an external target project;
- `docs/principles*` — durable engineering principles;
- `docs/decision-framework*` — conflict and exception handling;
- `docs/practices*` — implementation guidance that may evolve faster;
- `docs/governance*` — how the methodology itself changes;
- `AGENTS.md` — agent operating constraints for this methodology repository;
- `CONTRIBUTING.md` — contribution workflow and expectations;
- `templates/` — reusable derived artifacts.

Avoid duplicating the same normative text across multiple files. Link to the canonical document instead.

## 3. Language and Translation

Use bilingual documentation where it materially improves access, not as a requirement for every repository file.

For this methodology repository, maintain English and Simplified Chinese pairs for:

- the README;
- core methodology documents intended for regular human reading;
- user-facing templates when the translation has practical value.

Operational files such as `AGENTS.md`, `AGENT_REVIEW_PROTOCOL.md`, workflow configuration, or contribution mechanics may remain English-first unless a translation materially improves usability.

Agent-executed reviews should normally be written in the user's language.

Keep paired documents semantically aligned, but write naturally in each language rather than forcing literal translation.

## 4. Verifiable Changes

Prefer changes that have a clear verification path.

Depending on the project, verification may include:

- tests;
- linting;
- type checking;
- deterministic scripts;
- schema validation;
- documentation structure or link checks;
- reproducible examples;
- CI checks.

Verification should be proportional to the project and the risk. Do not add validation machinery whose maintenance cost exceeds the risk it controls.

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

## 7. Privacy and Project Hygiene

Keep private and public material intentionally separated.

At minimum, where relevant:

- do not commit credentials or secrets;
- avoid leaking machine-specific private paths into public artifacts;
- keep unpublished or private project data out of unintended public outputs;
- document external data transmission when it matters;
- use least-necessary permissions for agents and automation;
- review Git history before making a previously private repository public.

For external reviews of private or local targets, do not upload target material to another service merely to perform the review unless the user explicitly authorizes that data flow.

## 8. Progressive User Experience

Design onboarding in layers around the users a project actually serves.

A newcomer-facing project should make it easy to answer:

1. What is this project?
2. Who is it for?
3. What is the smallest useful way to adopt or try it?
4. What are the major assumptions or limitations?
5. Where can advanced or internal details be found?

Do not force advanced architecture or every methodology concept into the initial adoption path. Likewise, do not judge an intentionally expert-only internal project against a newcomer experience it never claims to provide.

## 9. External Methodology Review

The default adoption model is an **external review lens**, not inheritance of methodology files into every project.

At meaningful checkpoints, an AI agent may use this repository to review a target project without modifying it. The target may be local or remote, public or private, Git-based or not.

Use the canonical [`AGENT_REVIEW_PROTOCOL.md`](../AGENT_REVIEW_PROTOCOL.md) for agent-executed reviews and [`templates/PROJECT_REVIEW.md`](../templates/PROJECT_REVIEW.md) for the review dimensions.

Important behaviors:

- inspect actual evidence before judging the project;
- determine applicability before scoring;
- allow `N/A` where a methodology dimension is genuinely irrelevant;
- distinguish gaps from justified trade-offs;
- expose evidence limitations instead of guessing;
- remain read-only unless remediation is separately authorized.

The review should normally leave no methodology-specific files in the target project.

## 10. Diagnostic Scoring

A structured score can help users understand a review, but it must remain subordinate to evidence and findings.

The standard review uses:

- `Material`, `Relevant`, or `N/A` applicability;
- `0–4` evidence-backed dimension scores;
- `NE` when evidence is insufficient;
- per-dimension evidence confidence;
- an overall `/100` Diagnostic Score only when weighted Evidence Coverage reaches at least 70%.

`N/A` does not reduce the score. A high aggregate score does not erase a critical individual gap. Do not use scores as universal benchmarks across unrelated projects.

The exact formula and output contract are normative in [`AGENT_REVIEW_PROTOCOL.md`](../AGENT_REVIEW_PROTOCOL.md).

## 11. Decision Records

Use formal decision records only when the decision merits them.

For ordinary work, a clear PR or commit explanation is enough. For higher-impact deviations, record the default, conflict, trade-off, exception, evidence, rollback considerations, and revisit condition.

See [`templates/DECISION_RECORD.md`](../templates/DECISION_RECORD.md).

## 12. Release Readiness

Before a public release or visibility change, review:

- license and attribution;
- README and onboarding;
- language coverage that the project actually promises;
- secrets and private data;
- repository history where applicable;
- dependencies;
- validation status;
- contribution and conduct guidance when relevant;
- release scope and known limitations.

Public release is an engineering decision, not merely a repository setting change.

## 13. Evolving Practices

Practices should be updated when real project experience or tooling changes justify it.

External repositories can provide useful mechanisms and examples, but adoption should be selective. Do not import a process, file structure, tool, or convention only because a prominent project uses it.

Do not promote a tool-specific practice into a stable principle unless it represents a durable engineering concern independent of the tool itself.
