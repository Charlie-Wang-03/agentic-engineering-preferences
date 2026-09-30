# Project Conventions

These are implementation-level conventions I usually prefer after a project decision has been made. They are not a universal repository skeleton.

## Repository Entry Surface

A serious project should make its purpose and operating surface discoverable. Depending on the project, useful root-level artifacts may include README.md, LICENSE, AGENTS.md when useful, .gitignore, docs, tests or validation, and .github for public or collaborative workflows.

Do not add files solely to resemble a “complete” repository.

## README

A useful README normally helps a reader answer:

1. What is this project?
2. Who is it for?
3. What is the smallest useful way to try or use it?
4. How is important behavior validated?
5. What assumptions or limitations matter?
6. Where are deeper details documented?

Avoid philosophy-heavy introductions, excessive badges, or long implementation details before the basic adoption path.

## Validation

Prefer one canonical validation entry point when practical. A capable agent should be able to determine how to check whether a change is acceptable.

Use stronger validation for higher-risk work; do not add machinery whose maintenance cost exceeds the risk it controls.

## Agent Context

When AGENTS.md is useful, keep the root file concise and include only stable information such as project purpose, files to read first, commands, repository boundaries, invariants, project-specific constraints, high-risk operations, and definition of done.

Add nested instructions only when a subsystem genuinely has different commands, invariants, or risks.

## Documentation

Prefer one document per meaningful responsibility, not one file per concept.

Keep a canonical source for facts or normative information rather than maintaining multiple independently editable sources of truth. Derived representations are reasonable when they serve materially different consumers—for example a human README, an LLM-oriented source map, structured metadata, or generated machine-readable exports—provided their provenance is clear and their synchronization cost is justified.

Translate documents when translation materially improves use, not for symmetry.

## Git and Change Scope

Prefer coherent diffs that are easy to understand and revert.

Inspect the resulting diff before completion. Avoid mixing unrelated cleanup into a focused change. Keep generated artifacts clearly separated from hand-maintained source where that reduces review noise or accidental edits.

Commit messages should explain intent, not merely restate file operations.

## Public and Private Hygiene

Never commit credentials or secrets.

Avoid leaking private machine paths, unpublished data, internal-only artifacts, or private source material into public repositories or release packages.

Before public release or visibility changes, inspect both current files and relevant Git history.

Use least-necessary permissions for agents, automation, and workflows.

## Dependencies and Tooling

Once a dependency is accepted, keep setup reproducible and document important external requirements.

Pin versions where the maintenance or supply-chain risk justifies it. For GitHub Actions or similarly privileged automation, prefer immutable or otherwise trustworthy references when practical.

## GitHub Repository Settings

For public GitHub repositories, prefer a small set of settings that reduce maintenance friction without creating unnecessary process:

- keep Issues enabled when the repository accepts bug reports, corrections, or contribution discussion;
- prefer squash merging as the default PR integration strategy;
- disable merge commits and rebase merging unless a repository has a concrete reason to preserve those histories;
- automatically delete head branches after merge;
- keep Wiki disabled unless it has a real documentation role that should not live in the repository;
- treat Projects, Discussions, auto-merge, update-branch behavior, and squash-message formatting as project-local choices rather than universal defaults.

Repository rulesets, branch protection, permissions, environments, Pages, secrets, and other higher-impact settings should be configured to match the project's actual collaboration and release model rather than copied mechanically from another repository.

## Releases and Artifacts

Keep source, generated artifacts, validation outputs, and delivery packages distinguishable.

A released or handed-off artifact should have enough provenance to identify what produced it and what project state it belongs to when that matters.

Do not confuse “the command completed” with “the artifact was validated.”

## Progressive Usability

For reusable or public-facing projects, prefer a clear quick start, sensible defaults, progressive disclosure of advanced configuration, low initial cognitive load, and visible limitations.

Do not impose newcomer-oriented UX work on an intentionally internal or expert-only project that does not need it.
