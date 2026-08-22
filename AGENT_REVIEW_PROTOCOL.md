# Agent Review Protocol

This file is the canonical, tool-independent execution protocol for using the **Agentic Open-Source Engineering Methodology** to review a separate target project.

It is intentionally different from this repository's [`AGENTS.md`](AGENTS.md):

- `AGENTS.md` governs agents **modifying this methodology repository**;
- `AGENT_REVIEW_PROTOCOL.md` governs agents **using this methodology to review another project**.

The target may be a GitHub repository, another remote repository, a local project directory, the current agent workspace, or another project source the agent can actually inspect. The target does not need to be open source or even Git-based. Apply only the methodology dimensions that materially fit the target.

## 1. Operating Mode

Unless the user explicitly asks for changes, operate in **read-only review mode**.

Do not:

- modify target files;
- create commits or pull requests;
- install dependencies;
- change repository or service settings;
- run destructive commands;
- upload private target material to another service merely to perform the review.

A request to "review", "check", "audit", "analyze", or similar language does not by itself authorize remediation.

This is a methodology review, not a security certification, compliance audit, or guarantee of software quality.

## 2. Resolve Review Scope and Access

Identify, without inventing unavailable state:

- the target project and the source through which it can be inspected;
- the methodology source and ref being used;
- whether the target is local, remote, public, private, or partially accessible;
- whether Git history, issues, pull requests, CI, runtime execution, or external services are accessible;
- whether the user requested a full review or a narrower question.

When possible, record the resolved methodology commit or immutable ref in the final review. If the user points to a moving branch such as `main`, use the state actually inspected.

If access is partial, continue with the available evidence but state the limitation. Never infer inaccessible repository state as fact.

## 3. Load the Minimum Methodology Context

Read, in this order:

1. this `AGENT_REVIEW_PROTOCOL.md`;
2. [`docs/principles.md`](docs/principles.md);
3. [`docs/decision-framework.md`](docs/decision-framework.md);
4. [`templates/PROJECT_REVIEW.md`](templates/PROJECT_REVIEW.md).

Read [`docs/practices.md`](docs/practices.md) when implementation guidance is needed.

Do not load unrelated methodology files merely for completeness. `docs/governance.md` normally concerns evolution of the methodology itself and is not required for a target-project review.

## 4. Understand the Target Before Judging It

Establish enough context to avoid evaluating the target against goals it does not have.

Determine, where evidence allows:

- purpose and primary users;
- project maturity and expected lifetime;
- whether public release, external contribution, or reuse is intended;
- how heavily AI agents participate in development or operation;
- deployment and execution model;
- data, privacy, security, or proprietary boundaries;
- important quality attributes and explicit constraints.

A methodology default may be irrelevant to a particular target. Do not manufacture a problem solely because a named principle exists.

## 5. Evidence Before Judgment

Inspect actual project evidence before making broad claims.

Useful evidence may include, as applicable:

- repository or project tree;
- README and onboarding material;
- project-level agent instructions;
- dependency manifests and lock files;
- configuration and deployment files;
- tests, validation scripts, CI, and reproducible examples;
- privacy, security, licensing, release, and contribution material;
- implementation code relevant to a claim;
- recent commits, issues, or pull requests when history is material;
- commands or runtime results when execution is available and safe;
- explicit user-provided constraints.

Prefer direct implementation or configuration evidence over branding or aspirational documentation when they conflict.

Do not claim that a property is implemented merely because the README says so when stronger evidence is available to inspect.

For important findings, identify the evidence used. If evidence is missing, say so.

## 6. Determine Applicability Before Scoring

Review the following dimensions. They are review dimensions, not a requirement that every target satisfy every methodology principle.

1. **Project Clarity & Outcomes**
2. **Agent Context & Human Accountability**
3. **Openness & Collaboration Boundary**
4. **User Sovereignty & Privacy**
5. **Local / Remote Boundary**
6. **Portability & Lock-in**
7. **Dependency Discipline**
8. **Progressive Usability**
9. **Verifiability**
10. **Reversibility**

For each dimension, assign one applicability state:

- **Material** — meaningfully affects project outcomes or risk; scoring weight `2`;
- **Relevant** — worth reviewing but secondary; scoring weight `1`;
- **N/A** — not meaningfully applicable to the target; excluded from scoring.

Examples:

- `Openness & Collaboration Boundary` may be `N/A` for an intentionally private internal project with no public-release or external-contribution goal.
- `Local / Remote Boundary` may be `N/A` for a static documentation project with no meaningful runtime or data flow.
- `Portability & Lock-in` may be `N/A` when the project has no replaceable provider, platform, model, or tool boundary worth abstracting.

Do not penalize a target for a dimension that is genuinely `N/A`.

## 7. Diagnostic Scoring

The score is a compact user-facing diagnostic, not certification, compliance, or a universal maturity ranking.

For each applicable dimension with enough evidence, assign:

- **0 — Critical gap:** the current state materially conflicts with project needs or creates uncontrolled risk;
- **1 — Weak:** major gaps exist and important controls or decisions are missing;
- **2 — Partial:** some useful structure exists, but material gaps or inconsistencies remain;
- **3 — Good:** the dimension is handled well for the project's current needs, with limited gaps;
- **4 — Strong:** the project handles the dimension explicitly, proportionately, and with convincing evidence.

If evidence is insufficient to score an otherwise applicable dimension, mark it **NE — Not Enough Evidence**. Do not guess a numerical score.

Also assign an evidence confidence of **High / Medium / Low** to each numerical dimension score.

### Evidence Coverage

Let `w_i` be the applicability weight for every applicable dimension (`2` for Material, `1` for Relevant).

Evidence coverage is:

`100 × (sum of weights for numerically scored dimensions) / (sum of weights for all applicable dimensions)`

### Overall Diagnostic Score

Only issue an overall score when evidence coverage is at least **70%**.

For numerically scored dimensions:

`Diagnostic Score = 100 × Σ(w_i × score_i) / Σ(w_i × 4)`

Round to the nearest whole number.

Report it as, for example:

`Diagnostic Score: 78/100 · Evidence Coverage: 86%`

If coverage is below 70%, report:

`Diagnostic Score: Not issued · Evidence Coverage: <value>%`

A high overall score does not cancel a critical individual finding. Do not compare overall scores across unrelated projects as if they were benchmark results.

## 8. Apply the Decision Framework to Apparent Deviations

A low or non-default alignment is not automatically a defect.

For material deviations, use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

Distinguish among:

- an actual engineering gap;
- an intentional and justified trade-off;
- a decision that needs more evidence;
- a concern whose remediation cost currently exceeds its value.

For example, a project may reasonably depend on a proprietary solver, platform, or provider when that dependency is intrinsic to its purpose. Do not recommend abstraction merely to improve a portability score.

## 9. Output Contract

Unless the user requests another format, produce the review in the user's language and use this structure.

### Review Scope

State:

- target project;
- methodology source / resolved ref when available;
- evidence actually inspected;
- important access or execution limitations;
- whether the review was read-only.

### Executive Result

Give:

- overall Diagnostic Score when eligible;
- Evidence Coverage;
- a short assessment of the project's strongest engineering property and most important current risk or gap.

### Dimension Scorecard

Use a compact table with:

- Dimension;
- Applicability (`Material`, `Relevant`, `N/A`);
- Score (`0–4`, `NE`, or `N/A`);
- Confidence;
- Key evidence / rationale.

### Highest-Value Gaps

Report only the most consequential gaps worth acting on now. Prefer at most five.

For each important finding include:

- **Finding**;
- **Evidence**;
- **Why it matters**;
- **Recommended action**;
- **Methodology basis**;
- **Confidence**.

### Accepted Trade-offs

Identify non-default choices that should remain because they are currently justified.

### Evidence Needed

List important questions that cannot be resolved from available evidence.

### Deliberately Deferred

Identify real concerns that are not worth fixing now because remediation would add more complexity or cost than value.

### Suggested Next Actions

Give a short, prioritized list, normally three to five actions. Do not turn the review into a large backlog merely to appear comprehensive.

## 10. Degraded Review Mode

A partial review is preferable to fabricated completeness.

If the agent cannot access the methodology source, target source, or a material class of evidence:

- state exactly what is unavailable;
- do not pretend to have followed unread instructions;
- do not score dimensions whose evidence is inadequate;
- reduce Evidence Coverage accordingly;
- tell the user what additional access or files would materially improve the review.

## 11. Review Does Not Modify the Target

After presenting the review, the agent may recommend changes. It must not make them unless the user separately authorizes implementation.

If implementation is later requested, treat it as a new task: inspect the target's own instructions and constraints, scope the change, validate it, and preserve the target project's own governance rather than importing this methodology repository into it.
