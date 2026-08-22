# Decision Framework

[简体中文](decision-framework.zh-CN.md)

The methodology treats its principles as strong defaults rather than absolute rules. This framework defines how to make and explain exceptions without turning the methodology into either dogma or vague preference.

## The Decision Loop

Use:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

### 1. Default

Start from the relevant methodology principle. Defaults reduce repeated debate and make project behavior more consistent.

### 2. Conflict

Identify the real conflict. Typical conflicts include:

- portability vs provider-specific capability;
- local execution vs usability or compute requirements;
- fewer dependencies vs reuse of mature infrastructure;
- newcomer simplicity vs advanced configurability;
- rapid agent execution vs reviewability and safety.

Do not invent a conflict merely to justify a preferred implementation.

### 3. Trade-off

Compare the meaningful consequences rather than counting how many principles each option satisfies.

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

### 4. Exception

Choose the non-default option when the evidence indicates that it materially improves the project outcome.

An exception should be scoped as narrowly as practical. Do not generalize a one-off exception into a new project-wide rule without evidence.

### 5. Evidence

Record enough reasoning that another developer or agent can understand why the deviation exists.

Evidence may be lightweight. Depending on impact, it can be a PR description, decision note, benchmark, test result, issue discussion, or short design record.

Higher-impact or harder-to-reverse deviations require stronger evidence.

### 6. Revisit

Treat exceptions as decisions under current conditions, not permanent truths.

Revisit them when:

- underlying tools or models change;
- maintenance cost grows;
- the original constraint disappears;
- new evidence invalidates the original rationale;
- an exception starts spreading beyond its intended scope.

## Decision Quality over Principle Counting

A decision is not better merely because it satisfies more named principles. Principles exist to expose important engineering concerns, not to provide a scoring game.

When principles conflict, prioritize the outcome that best preserves user value, project quality, safety, maintainability, and the project's explicit goals.

## Documentation Proportional to Risk

Decision records should be proportional to impact.

- **Low impact:** normal commit or PR explanation is usually sufficient.
- **Medium impact:** explicitly state the default, conflict, trade-off, and chosen exception.
- **High impact:** preserve durable evidence, alternatives considered, risks, rollback strategy, and revisit conditions.

High-impact examples include destructive migrations, privacy or security boundary changes, provider lock-in, repository visibility changes, major dependency commitments, and irreversible history changes.

## Adding or Changing Methodology Rules

Before changing a core principle, ask:

1. What recurring engineering problem is not being handled well?
2. Is the problem cross-project rather than incidental?
3. Is the proposed change really a Principle, a Decision Rule, or a Practice?
4. Can an existing principle be clarified instead?
5. Is the proposal based on durable engineering concerns rather than a short-lived tool trend?
6. What real project evidence supports the change?

If those questions cannot be answered, prefer leaving the core methodology unchanged.
