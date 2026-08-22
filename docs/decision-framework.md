# Decision Framework

[简体中文](decision-framework.zh-CN.md)

The methodology treats its principles as strong defaults rather than absolute rules. This framework defines how developers and agents make and explain exceptions without turning the methodology into either dogma or vague preference.

## Start with the Project Outcome

Before applying a principle, make the relevant project outcome explicit enough to reason about. Depending on the decision, this may include:

- the project's purpose and primary users;
- correctness and quality requirements;
- privacy, security, or safety boundaries;
- performance or resource constraints;
- maintainability and operational cost;
- compatibility commitments;
- delivery constraints or other explicit project goals.

Do not assume that satisfying more methodology principles automatically produces the better project outcome.

## The Decision Loop

Use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

### 1. Default

Start from the relevant methodology principle or established project default. Defaults reduce repeated debate and make project behavior more consistent.

### 2. Conflict

Identify the real conflict. Typical conflicts include:

- portability vs provider-specific capability;
- local execution vs usability or compute requirements;
- dependency restraint vs reuse of mature infrastructure;
- newcomer simplicity vs advanced configurability;
- rapid agent execution vs reviewability and safety.

Do not invent a conflict merely to justify a preferred implementation.

### 3. Trade-off

Compare meaningful consequences rather than counting how many principles each option satisfies.

Consider, as applicable:

- user value;
- correctness and quality;
- privacy and security;
- reliability and verifiability;
- performance;
- maintainability;
- operational and cognitive complexity;
- portability and lock-in;
- reversibility;
- short- and long-term cost.

Only use dimensions that materially affect the actual decision.

### 4. Exception

Choose the non-default option when the available evidence indicates that it materially improves the project outcome.

Scope the exception as narrowly as practical. Do not generalize a one-off exception into a new project-wide rule without evidence.

### 5. Evidence

Record enough reasoning that another developer or agent can understand why the deviation exists.

Evidence should be proportional to impact. It may be a PR description, decision note, benchmark, test result, issue discussion, operational constraint, or short design record.

Higher-impact or harder-to-reverse deviations require stronger evidence.

### 6. Revisit

Treat exceptions as decisions under current conditions, not permanent truths.

Revisit them when:

- underlying tools or models change;
- maintenance cost grows materially;
- the original constraint disappears;
- new evidence invalidates the original rationale;
- an exception starts spreading beyond its intended scope.

## Decision Quality over Principle Counting

A decision is not better merely because it satisfies more named principles. Principles exist to expose important engineering concerns, not to provide a scoring game.

When principles conflict, prioritize the option that best fits the project's explicit purpose, users, quality requirements, risk boundaries, maintainability needs, and current constraints.

## Documentation Proportional to Risk

Decision records should be proportional to impact.

- **Low impact:** a normal commit or PR explanation is usually sufficient.
- **Medium impact:** explicitly state the default, conflict, trade-off, and chosen exception.
- **High impact:** preserve durable evidence, alternatives considered, risks, rollback strategy, and revisit conditions.

High-impact examples include destructive migrations, privacy or security boundary changes, provider lock-in, repository visibility changes, major dependency commitments, and irreversible history changes.

Use [`templates/DECISION_RECORD.md`](../templates/DECISION_RECORD.md) when a decision deserves a durable record.

## Adding or Changing Methodology Rules

Before changing a core principle, ask:

1. What recurring engineering problem is not being handled well?
2. Is the problem cross-project rather than incidental?
3. Is the proposed change really a Principle, a Decision Rule, or a Practice?
4. If it is a Principle, is it primarily a value, default, constraint, decision rule, or preferred means?
5. Can an existing principle be clarified instead?
6. Is the proposal based on a durable engineering concern rather than a short-lived tool trend?
7. What real project evidence supports the change?

If those questions cannot be answered, prefer leaving the core methodology unchanged.

Changes to the methodology itself also follow the lightweight rules in [Governance](governance.md).
