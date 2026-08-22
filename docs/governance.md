# Methodology Governance

[简体中文](governance.zh-CN.md)

This document governs how the methodology itself changes. It is intentionally lightweight: governance should protect coherence without turning a small methodology repository into a process-heavy standards body.

## 1. Normative Structure

The repository separates responsibilities:

- `docs/principles.md` — durable decision principles;
- `docs/decision-framework.md` — conflict, trade-off, exception, and evidence handling;
- `docs/practices.md` — faster-moving implementation guidance;
- `docs/governance.md` — how those documents evolve;
- `AGENT_REVIEW_PROTOCOL.md` — canonical execution contract for agents reviewing an external target project;
- `AGENTS.md` — operational constraints for agents working on this methodology repository;
- `templates/PROJECT_REVIEW.md` — review dimensions and human-readable diagnostic rubric;
- other `templates/` — reusable artifacts derived from the methodology;
- `README.md` — orientation, audience, scope, and adoption path.

`AGENTS.md` and `AGENT_REVIEW_PROTOCOL.md` must not be conflated: one governs modification of this repository; the other governs application of this repository to a separate target project.

When the same rule appears in multiple places, prefer one canonical normative source and links or short summaries elsewhere.

## 2. Change Thresholds

Different changes require different levels of evidence.

### Principle changes

Adding, removing, merging, or materially redefining a core principle requires the strongest justification. A proposal should identify:

- the recurring engineering problem;
- why existing principles and the decision framework are insufficient;
- evidence from real project work or durable external engineering practice;
- likely overlap with existing principles;
- downstream impact on practices, review dimensions, templates, and agent instructions.

During private incubation, prefer clarification over principle expansion.

### Decision Framework changes

Change the framework when real decisions reveal ambiguity, missing trade-off handling, or poor exception behavior. Preserve the basic goal: defaults should guide decisions without becoming absolute rules.

### Practice and review-protocol changes

Practices and the Agent Review Protocol may evolve more freely as tools, access patterns, and engineering conventions change, but they should still solve demonstrated problems.

Changes to the review protocol should preserve these invariants unless evidence justifies revisiting them:

- evidence before judgment;
- applicability before scoring;
- `N/A` without penalty for genuinely irrelevant dimensions;
- explicit treatment of insufficient evidence;
- read-only review by default;
- separation of gaps from justified trade-offs;
- structured output without claiming certification.

Prominent external repositories and agent tools are evidence sources, not authorities to copy mechanically.

### Repository implementation changes

Automation, scripts, templates, and repository structure should remain proportional to this repository's actual risk and maintenance needs.

## 3. Change Propagation

A methodology change is incomplete if derived artifacts become misleading.

When relevant, review:

- README summaries, one-prompt entry points, and navigation;
- paired core-language documents;
- `AGENT_REVIEW_PROTOCOL.md`;
- `AGENTS.md`;
- `templates/PROJECT_REVIEW*` and other affected templates;
- validation rules;
- pull-request guidance.

A principle change does not automatically require a scoring change. Likewise, a protocol wording change should not trigger unrelated methodology edits merely for synchronization.

Do not update unrelated files merely to create a large synchronized change.

## 4. Language and Documentation Policy

English is the default operational language for international open-source collaboration. Simplified Chinese is a first-class reading path for the repository's core methodology.

Maintain paired English / Simplified Chinese versions for:

- `README.md` / `README.zh-CN.md`;
- Principles;
- Decision Framework;
- Practices;
- Governance;
- user-facing templates when translation materially improves adoption.

Operational files do not require automatic duplication. Files such as `AGENTS.md`, `AGENT_REVIEW_PROTOCOL.md`, workflows, or contribution mechanics may remain English-first unless a translation provides real value.

The README should provide a usable Chinese one-prompt entry path even when the canonical review protocol remains English-only. Agent-executed reviews should normally respond in the user's language.

Paired documents should remain semantically equivalent, but natural technical writing takes priority over literal translation.

## 5. Versioning and Review Traceability

During private incubation, `v0.x` labels describe methodology maturity rather than a promise of strict semantic versioning.

- a minor incubation version should represent a coherent methodology milestone;
- ordinary wording or maintenance changes do not require a new version label;
- Git tags and GitHub Releases should be created only for intentionally published milestones;
- the first public release should have a dedicated release-readiness review rather than inheriting a version number automatically.

Agent-executed reviews should record the methodology source and resolved commit or immutable ref when available. This provides useful traceability without requiring a separate protocol-versioning system during incubation.

## 6. Diagnostic Scoring Governance

Diagnostic scores exist to make an evidence-backed review easier for users to interpret; they are not certification or a universal project benchmark.

The scoring rules are canonical in `AGENT_REVIEW_PROTOCOL.md`. Changes to the formula, thresholds, applicability weights, or score meanings should require evidence that the current scheme produces misleading or unstable decisions.

Scoring must continue to allow:

- `N/A` for dimensions genuinely outside a target's goals;
- `NE` when evidence is insufficient;
- evidence coverage reporting;
- critical findings to remain visible regardless of aggregate score.

Do not optimize the methodology for higher scores or encourage target projects to add low-value machinery merely to improve a score.

## 7. Evidence and Decision Records

Most methodology changes can be explained in a focused pull request. Use a durable Decision Record only when the choice has broad impact, is difficult to reverse, or is likely to be revisited later.

Governance should not create documentation merely to prove that governance exists.

## 8. Repository as a Test Subject

This repository is one of the methodology's own test subjects. If its stated principles and actual maintenance behavior diverge, treat the inconsistency as evidence that either:

1. the repository implementation should change; or
2. the methodology is too broad, expensive, or ambiguous and should be revised.

The Agent Review Protocol is also a testable artifact. Before public release, it should be exercised against multiple target-project shapes and, where practical, multiple capable agent environments. Test behavioral invariants rather than expecting identical prose from different models.

Self-consistency is a diagnostic tool, not a reason to over-engineer the repository.

## 9. Public Release

Before changing the repository from private incubation to public release, perform a dedicated review of:

- methodology coherence and scope;
- README and onboarding;
- the one-prompt external-review path;
- review-protocol behavior on representative targets;
- privacy, secrets, and Git history;
- license and attribution;
- language promises;
- contribution and conduct guidance;
- validation status;
- repository settings and release boundaries.

Public release should be an explicit engineering decision.
