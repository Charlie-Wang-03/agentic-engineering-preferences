# Project Review

[简体中文](PROJECT_REVIEW.zh-CN.md)

Use this review to expose important engineering gaps in an AI-agent-heavy open-source project. It is a diagnostic aid, not a certification checklist or maturity score.

Answer only what materially applies to the project. A short, explicit answer is better than process for its own sake.

## 1. Purpose and Users

- What does the project exist to achieve?
- Who are the primary users or contributors?
- What outcomes matter enough to influence engineering trade-offs?

## 2. Agent Context

- Can a coding agent identify the repository structure, important commands, constraints, and definition of done without relying on hidden local knowledge?
- Is there a concise repository instruction file such as `AGENTS.md` when it would materially help?
- Are important subsystem-specific invariants documented close to their scope when necessary?

## 3. Open-Source Boundary

- Is the license clear?
- Are public interfaces, formats, and contribution paths understandable where relevant?
- Is anything intentionally private, embargoed, proprietary, or otherwise outside the public boundary?

## 4. User Control and Privacy

- What user data, credentials, private files, or machine-specific information can the project touch?
- What data leaves the user's environment, and why?
- Are agent, automation, and service permissions no broader than necessary?

## 5. Local / Remote Boundary

- Which capabilities run locally and which depend on remote services?
- Is that boundary justified by capability, usability, cost, maintenance, or privacy needs?
- Can a user understand the important external data flows and dependencies?

## 6. Portability

- Which models, agents, providers, cloud services, platforms, or toolchains are hard dependencies?
- Is each lock-in intentional?
- Would a replaceable boundary provide enough value to justify its complexity?

## 7. Dependencies

For important dependencies:

- What problem does each dependency solve?
- Would reimplementation be meaningfully worse?
- What are the installation, maintenance, security, portability, and replacement costs?

## 8. Usability

Can a newcomer quickly determine:

1. what the project is;
2. whether it is for them;
3. the smallest useful way to try or adopt it;
4. major assumptions or limitations;
5. where advanced details live?

## 9. Verification

- What commands or evidence show that a change is acceptable?
- Are important claims testable, reproducible, or otherwise checkable where practical?
- Is the verification machinery proportional to the project's actual risk?

## 10. Reversibility

- Are changes reviewable and reasonably scoped?
- Which operations are destructive or difficult to undo?
- Do high-risk changes have backup, dry-run, rollback, or recovery paths when practical?

## 11. Exceptions and Evidence

For any important deviation from a methodology default, can another developer or agent understand:

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

Use a normal PR or commit explanation for ordinary decisions. Use a durable [Decision Record](DECISION_RECORD.md) only when the decision merits one.

## 12. Review Result

Do not calculate a score. Summarize only:

- the **highest-value gaps** worth fixing now;
- the **accepted trade-offs** that should remain as they are;
- the **uncertain decisions** that need evidence before changing;
- anything deliberately deferred because fixing it would add more complexity than value.
