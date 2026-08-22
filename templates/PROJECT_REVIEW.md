# Project Review

[简体中文](PROJECT_REVIEW.zh-CN.md)

Use this review to expose important engineering gaps in a target project through **Agentic Engineering Review** and its underlying **Agentic Engineering Methodology**.

The target may be public or private, local or remote, Git-based or not. Apply only the dimensions that materially fit the project. This is a diagnostic review, not certification, compliance, or a universal maturity benchmark.

For agent-executed reviews, follow the canonical [`AGENT_REVIEW_PROTOCOL.md`](../AGENT_REVIEW_PROTOCOL.md).

## Applicability First

Before assigning a score, mark each review dimension as:

- **Material** — meaningfully affects project outcomes or risk;
- **Relevant** — worth reviewing but secondary;
- **N/A** — not meaningfully applicable to this target.

`N/A` is not a failure and does not reduce the score. Do not manufacture a concern solely because a methodology principle exists.

If an applicable dimension cannot be judged from available evidence, mark it **NE — Not Enough Evidence** instead of guessing.

## Diagnostic Scale

For each applicable dimension with enough evidence:

- **0 — Critical gap**
- **1 — Weak**
- **2 — Partial**
- **3 — Good**
- **4 — Strong**

Assign **High / Medium / Low** confidence to each numerical score.

For agent-executed reviews, `Material` dimensions have weight `2` and `Relevant` dimensions have weight `1`. An overall score is issued only when at least 70% of applicable weighted dimensions have enough evidence. See the Agent Review Protocol for the exact formula and output contract.

## 1. Project Clarity & Outcomes

- What does the project exist to achieve?
- Who are the primary users, operators, maintainers, or contributors?
- What outcomes matter enough to influence engineering trade-offs?
- What explicit constraints or quality attributes shape the project?

## 2. Agent Context & Human Accountability

When AI agents materially participate in development or operation:

- Can an agent identify project structure, important commands, constraints, and definition of done without relying on hidden local knowledge?
- Is there concise project-level guidance such as `AGENTS.md` when it would materially help?
- Are subsystem-specific invariants documented close to their scope when necessary?
- Are important decisions and released outcomes still human-accountable?

If AI agents do not materially participate in the target, this dimension may be `N/A`.

## 3. Openness & Collaboration Boundary

When public release, external reuse, open-source contribution, interoperability, or external collaboration is part of the project goal:

- Is the license or reuse boundary clear?
- Are public interfaces, formats, and contribution paths understandable where relevant?
- Is anything intentionally private, embargoed, proprietary, or otherwise outside the public boundary?
- Is the public/private boundary deliberate rather than accidental?

For an intentionally closed internal project with no public-release or external-collaboration goal, this dimension may be `N/A`.

## 4. User Sovereignty & Privacy

When the project touches user data, credentials, private files, personal environments, or external services:

- What sensitive or user-controlled material can the project access?
- What data leaves the user's environment, and why?
- Are agent, automation, and service permissions no broader than necessary?
- Can users understand and meaningfully control important data and execution choices where practical?

## 5. Local / Remote Boundary

When the project has meaningful runtime, data flow, or hosted-service behavior:

- Which capabilities run locally and which depend on remote services?
- Is that boundary justified by capability, usability, cost, maintenance, or privacy needs?
- Can a user understand important external data flows and dependencies?

For a project with no meaningful local/remote execution boundary, this dimension may be `N/A`.

## 6. Portability & Lock-in

When replaceable providers, models, agents, clouds, platforms, formats, or toolchains are material:

- Which are hard dependencies?
- Is each lock-in intentional?
- Would a replaceable boundary provide enough value to justify its complexity?
- Is provider-specific optimization isolated where portability actually matters?

Do not recommend abstraction merely to improve a portability score.

## 7. Dependency Discipline

For important dependencies:

- What problem does each dependency solve?
- Would reimplementation be meaningfully worse?
- What are the installation, maintenance, security, portability, and replacement costs?
- Is the dependency burden proportional to the project's real complexity?

## 8. Progressive Usability

For the project's intended users or contributors:

- Can they quickly determine what the project is and whether it is for them?
- Is there a smallest useful way to try, adopt, or operate it?
- Are major assumptions and limitations visible?
- Are advanced details separated from the initial path when practical?

Do not judge an internal expert-only project against newcomer goals it never claims to have.

## 9. Verifiability

- What commands, tests, evidence, or reproducible checks show that important behavior or claims are acceptable?
- Are important claims testable, reproducible, or otherwise checkable where practical?
- Is validation proportional to the project's actual risk?
- Does the project distinguish successful execution from demonstrated correctness when that distinction matters?

## 10. Reversibility

- Are changes reviewable and reasonably scoped?
- Which operations are destructive or difficult to undo?
- Do high-risk changes have backup, dry-run, rollback, recovery, or migration paths when practical?
- Are generated or transient artifacts separated where that materially reduces blast radius?

## 11. Exceptions and Evidence

For an important non-default choice, determine whether another developer or agent can understand:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

A deviation is not automatically a defect. Distinguish an engineering gap from a justified project-specific trade-off.

Use a normal PR or commit explanation for ordinary decisions. Use a durable [Decision Record](DECISION_RECORD.md) only when the decision merits one.

## 12. Review Result

A useful result contains:

- a **Dimension Scorecard** showing applicability, score, confidence, and key evidence;
- an overall **Diagnostic Score / 100** only when evidence coverage is sufficient;
- **Evidence Coverage** so users can see how much of the applicable project was actually judged;
- the **highest-value gaps** worth fixing now;
- the **accepted trade-offs** that should remain as they are;
- **evidence needed** before unresolved decisions can be made;
- concerns **deliberately deferred** because remediation would add more complexity or cost than value;
- a short prioritized list of **next actions**.

A score is a summary, not the conclusion. A high overall score does not erase a critical individual finding, and scores should not be compared mechanically across unrelated projects.
