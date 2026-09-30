# Decision Rules

These rules capture recurring engineering choices that otherwise tend to be reconsidered from scratch. They are defaults for judgment, not automatic requirements.

## When should a project add AGENTS.md?

**Default:** Add a concise root AGENTS.md when coding agents will repeatedly work in the repository and stable project context is not obvious.

Use it when the project has important commands, boundaries, invariants, validation paths, high-risk operations, or completion criteria that would otherwise need repeated explanation.

Skip or defer it when the repository is trivial, the README already provides sufficient operational context, or agents are not meaningfully involved.

## When should a project add CI?

**Default:** Establish a stable local validation command before automating it in CI.

Add CI when automatic regression checks materially protect a public, collaborative, long-lived, or release-producing project and the validation surface is stable enough to automate.

Defer CI when the project is still highly exploratory, the validation command itself is unstable, or CI would exist mainly for appearance.

## When should a dependency be added?

**Default:** Use a mature dependency when it solves a real problem more effectively than maintaining an in-house implementation.

Before adding one, consider value, maturity, maintenance, security, setup cost, lock-in, and replacement cost.

Avoid dependencies added for cosmetic sophistication, but also avoid reimplementing mature infrastructure merely to minimize dependency count.

## When should a GitHub Release be published?

**Default:** Publish a Release when a project state is a useful historical snapshot worth referencing, reproducing, testing, handing off, or discussing.

A Release is not certification that a project is correct, finished, or production-ready.

Do not publish a Release merely because several commits accumulated or because a repository should look mature.

## When should work use a branch and pull request?

**Default:** Prefer a branch and PR for non-trivial, cross-file, public, collaborative, high-impact, or broad agent-generated changes.

Direct changes can be reasonable for trivial, low-risk, immediately reviewable work when repository policy allows it.

The goal is reviewability and recovery, not process for its own sake.

## When is explicit human approval required?

Require explicit approval before operations that materially change ownership, visibility, history, access, or irreversible state, including:

- deletion;
- force push or history rewrite;
- repository visibility changes;
- release or tag creation;
- branch-protection, ruleset, or permission changes;
- secret or credential operations;
- destructive migrations;
- large irreversible restructuring.

A request to review, analyze, or inspect does not imply permission to mutate.

## When should documentation be bilingual?

**Default:** Do not require every document to exist in multiple languages.

Use bilingual documentation when the project materially serves both Chinese-speaking and international audiences, or when translation meaningfully improves onboarding, collaboration, or public discovery.

README entry points are often worth translating. Operational configuration, agent instructions, and internal technical documents usually do not need automatic duplication.

## When should a new standalone document be created?

Create a document when the information has a distinct responsibility, will be independently referenced, or would make an existing document materially harder to use if merged into it.

Avoid one-file-per-concept structures, duplicate normative text, and documents created only for completeness.

## When should an abstraction layer be introduced?

Add an abstraction when multiple real implementations exist, replacement is plausible, the boundary improves testing or maintenance, or provider-specific special cases are already creating friction.

Avoid abstraction for hypothetical future providers, branding claims such as “model agnostic,” or lowest-common-denominator design before concrete variability exists.

## When should a public-release or privacy audit be performed?

Perform a dedicated audit before:

- changing a private repository to public;
- extracting a reusable public template from private infrastructure;
- publishing datasets, artifacts, or delivery packages;
- external handoff of a repository or generated bundle.

Check current files, Git history, secrets, private paths, unpublished material, licenses, README claims, generated artifacts, archives, and external links as applicable.


## When should externally costly or stateful execution use an explicit budget?

**Default:** Bound the work before starting when execution spends money, consumes a rate limit, mutates external state, or can otherwise expand without a natural stopping point.

Use explicit ceilings such as request counts, retries, runtime, generated items, cloud jobs, or other task-appropriate limits. Prefer fail-closed behavior when the requested operation would exceed the approved budget.

Human approval answers whether an operation is authorized. A budget answers how far that authorization extends; both may be necessary.

Avoid unbounded retry, polling, fan-out, or “keep going until it works” behavior against paid or externally stateful systems.
