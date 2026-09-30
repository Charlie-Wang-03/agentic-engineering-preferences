# Engineering Preferences

These are the relatively stable engineering tendencies I use across AI-assisted software projects. They are defaults, not mandates. A project's own goals, evidence, constraints, and local instructions take precedence.

## 1. Outcomes over Convention

Cross-project preferences exist to reduce repeated decisions, not to override project reality.

Prefer the option that best serves the current project's actual purpose, users, correctness requirements, risk boundaries, maintainability, cost, and delivery constraints. A convention that does not improve the project should not be followed merely for consistency.

## 2. Verifiable over Plausible

Prefer results that can be checked by tools or reproducible evidence.

For agent-generated or large-scale changes, tests, validation commands, runtime evidence, artifact checks, or reproducible examples are more trustworthy than output that merely looks reasonable.

> Agent-generated work should be verifiable by tools, not trusted by appearance.

Separate execution status from domain acceptance whenever that distinction materially affects correctness. A command, pipeline, training run, build, or API call completing successfully should not automatically imply that the resulting scientific, data-quality, business, or engineering acceptance criteria passed.

Verification effort should remain proportional to the project's risk.

## 3. Reversible over Unnecessarily Risky

Prefer coherent, reviewable changes with controlled blast radius and a clear recovery path.

Use version control, focused diffs, branches, backups, dry-runs, rollback plans, migration safeguards, or generated-artifact isolation when they materially reduce risk. Do not mechanically optimize for tiny commits; optimize for understandable and recoverable change.

When an artifact needs to remain citable or reproducible, freeze that artifact or release boundary rather than unnecessarily freezing every surrounding document or presentation layer. Preserve the immutable evidence anchor while allowing clearly separated maintenance or presentation surfaces to evolve.

## 4. Explicit over Hidden Context

Prefer important project knowledge to be discoverable from the repository or its documented interfaces.

Commands, validation paths, repository boundaries, invariants, generated-artifact rules, high-risk operations, and definitions of done should be explicit when they materially affect work. A capable agent should not need repeated conversational reconstruction of stable project facts.

Explicit does not mean eager. Keep stable context discoverable, but load only the smallest task-relevant subset by default and expand into deeper governance, architecture, or historical context when the task actually requires it.

## 5. Dependencies Must Earn Their Cost

A dependency is justified by the problem it solves, not by dependency count.

Consider capability, implementation cost, maturity, maintenance activity, installation burden, security exposure, portability impact, and replacement cost. Prefer mature infrastructure over fragile reimplementation when the dependency is worthwhile; avoid adding tools solely for sophistication or fashion.

## 6. Privacy and Boundaries Should Be Deliberate

Treat secrets, credentials, private paths, unpublished data, public/private repository boundaries, external uploads, and agent permissions as explicit engineering concerns.

Use the least access necessary, keep private and public artifacts intentionally separated, and inspect repository history before making previously private material public when that history may contain sensitive information.

## 7. Portability and Locality Are Means, Not Goals

Prefer replaceable boundaries or local execution when they provide concrete value in privacy, reproducibility, autonomy, maintenance, cost, testing, or future flexibility.

Do not add abstraction merely to claim model/provider agnosticism, and do not force local execution when a remote service is clearly the better engineering choice. Optimize for useful boundaries, not ideological purity.
