# Methodology Governance

[简体中文](governance.zh-CN.md)

This document governs how the methodology itself changes. It is intentionally lightweight: governance should protect coherence without turning a small methodology repository into a process-heavy standards body.

## 1. Normative Structure

The repository separates responsibilities:

- `docs/principles.md` — durable decision principles;
- `docs/decision-framework.md` — conflict, trade-off, exception, and evidence handling;
- `docs/practices.md` — faster-moving implementation guidance;
- `docs/governance.md` — how those documents evolve;
- `AGENTS.md` — operational constraints for agents working in this repository;
- `templates/` — reusable artifacts derived from the methodology;
- `README.md` — orientation, audience, scope, and adoption path.

When the same rule appears in multiple places, prefer one canonical normative source and links or short summaries elsewhere.

## 2. Change Thresholds

Different changes require different levels of evidence.

### Principle changes

Adding, removing, merging, or materially redefining a core principle requires the strongest justification. A proposal should identify:

- the recurring engineering problem;
- why existing principles and the decision framework are insufficient;
- evidence from real project work or durable external engineering practice;
- likely overlap with existing principles;
- downstream impact on practices, templates, and agent instructions.

During private incubation, prefer clarification over principle expansion.

### Decision Framework changes

Change the framework when real decisions reveal ambiguity, missing trade-off handling, or poor exception behavior. Preserve the basic goal: defaults should guide decisions without becoming absolute rules.

### Practice changes

Practices may change more freely as tools and engineering conventions evolve, but should still solve a real problem. Prominent external repositories are evidence sources, not authorities to copy mechanically.

### Repository implementation changes

Automation, scripts, templates, and repository structure should remain proportional to this repository's actual risk and maintenance needs.

## 3. Change Propagation

A methodology change is incomplete if derived artifacts become misleading.

When relevant, review:

- README summaries and navigation;
- paired core-language documents;
- `AGENTS.md`;
- templates;
- validation rules;
- pull-request guidance.

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

Operational files do not require automatic duplication. Files such as `AGENTS.md`, workflows, or contribution mechanics may remain English-first unless a translation provides real value.

Paired documents should remain semantically equivalent, but natural technical writing takes priority over literal translation.

## 5. Versioning

During private incubation, `v0.x` labels describe methodology maturity rather than a promise of strict semantic versioning.

- a minor incubation version should represent a coherent methodology milestone;
- ordinary wording or maintenance changes do not require a new version label;
- Git tags and GitHub Releases should be created only for intentionally published milestones;
- the first public release should have a dedicated release-readiness review rather than inheriting a version number automatically.

## 6. Evidence and Decision Records

Most methodology changes can be explained in a focused pull request. Use a durable Decision Record only when the choice has broad impact, is difficult to reverse, or is likely to be revisited later.

Governance should not create documentation merely to prove that governance exists.

## 7. Repository as a Test Subject

This repository is one of the methodology's own test subjects. If its stated principles and actual maintenance behavior diverge, treat the inconsistency as evidence that either:

1. the repository implementation should change; or
2. the methodology is too broad, expensive, or ambiguous and should be revised.

Self-consistency is a diagnostic tool, not a reason to over-engineer the repository.

## 8. Public Release

Before changing the repository from private incubation to public release, perform a dedicated review of:

- methodology coherence and scope;
- README and onboarding;
- privacy, secrets, and Git history;
- license and attribution;
- language promises;
- contribution and conduct guidance;
- validation status;
- repository settings and release boundaries.

Public release should be an explicit engineering decision.
