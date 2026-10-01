# Used in Practice

This page links selected Agentic Engineering Preferences to public project evidence.

It is deliberately a lightweight adoption index, not a case-study catalog, scoring system, or claim that a preference caused a better project outcome. The examples below show where a preference or decision rule is already visible in real project design, documentation, validation, or maintenance history.

Only publicly inspectable evidence is included. Examples are selected for clarity rather than coverage, and a missing example does not imply that a preference is unimportant or unused.

## Engineering Preferences

### Outcomes over Convention

**AI4Math Radar** preserves the inherited native AIHOT runtime while using a much lighter `static-chatgpt` profile as the active operating path. Existing capability is retained without treating its operational cost as mandatory.

Evidence:

- [AI4Math Radar README](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/README.md)
- [Active deployment profile](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/deployment/active.json)

**Sightline** keeps a deliberately narrow product boundary around cross-agent instruction-surface comparison rather than expanding into a general prompt linter, synchronizer, or agent-configuration suite.

Evidence:

- [Sightline product contract](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/PRODUCT_CONTRACT.md)
- [Sightline AGENTS.md](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/AGENTS.md)

### Verifiable over Plausible

**Sightline** treats evidence state as part of the product model. DeepSeek Harness runtime evidence may be marked observed; Codex and Claude Code results are predicted from documented semantics; unavailable evidence remains unavailable rather than being silently converted into absence or observation.

Evidence:

- [Sightline product contract](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/PRODUCT_CONTRACT.md)
- [Sightline compatibility notes](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/COMPATIBILITY.md)

**SLURM Dashboard** separates automated tests, simulated degradation, and real SLURM / GPU / browser acceptance. A simulated or mocked environment is not presented as evidence that the same behavior was verified on a real cluster.

Evidence:

- [SLURM Dashboard README](https://github.com/Charlie-Wang-03/slurm-dashboard/blob/main/README.md)
- [Manual acceptance walk-through](https://github.com/Charlie-Wang-03/slurm-dashboard/blob/main/docs/testing.md)

**jev-testbench** separates vendor claims, local measurements, derived calculations, and limitations; keeps negative and null results; and preserves frozen evidence as a citable historical artifact.

Evidence:

- [jev-testbench README](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/README.md)
- [v0.1.0 public evidence freeze](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/docs/evidence/v0.1.0/PUBLIC_EVIDENCE_FREEZE.md)

### Reversible over Unnecessarily Risky

**jev-testbench** freezes its scientific evidence at a versioned release while allowing the maintained repository and presentation surfaces to continue evolving. The immutable evidence anchor is preserved instead of freezing every surrounding document.

Evidence:

- [v0.1.0 public evidence freeze](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/docs/evidence/v0.1.0/PUBLIC_EVIDENCE_FREEZE.md)
- [Publication closure](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/docs/publication/PUBLICATION_CLOSURE.md)

**The GitHub profile repository** uses short-lived branches, focused pull requests, CI, review, squash merge, and explicit approval for high-impact identity, privacy, security, or governance changes.

Evidence:

- [Profile maintenance guide](https://github.com/Charlie-Wang-03/Charlie-Wang-03/blob/main/MAINTENANCE.md)
- [Profile AGENTS.md](https://github.com/Charlie-Wang-03/Charlie-Wang-03/blob/main/AGENTS.md)

### Explicit over Hidden Context

Several public projects keep stable, project-specific operating context in repository-readable agent instructions rather than relying on repeated conversational reconstruction.

- **SLURM Dashboard** makes its real SLURM side effects, local-user trust boundary, validation paths, privacy-sensitive data, and high-risk changes explicit in [AGENTS.md](https://github.com/Charlie-Wang-03/slurm-dashboard/blob/main/AGENTS.md).
- **Sightline** records evidence semantics, adapter boundaries, compatibility expectations, mutation limits, and release constraints in [AGENTS.md](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/AGENTS.md).
- **AI4Math Radar** records domain boundaries, calibration expectations, paid-request safeguards, validation commands, and scope limits in [AGENTS.md](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/AGENTS.md).
- **The GitHub profile repository** records public-evidence authority, private/public boundaries, bilingual responsibilities, and high-impact approval gates in [AGENTS.md](https://github.com/Charlie-Wang-03/Charlie-Wang-03/blob/main/AGENTS.md).

The pattern is not that every repository must contain the same instruction file. The recurring preference is that stable project context should be discoverable when agents repeatedly need it.

### Privacy and Boundaries Should Be Deliberate

**SLURM Dashboard** models remote-network, local-user, browser-origin, command-execution, filesystem, runtime-data, and repository boundaries separately. In particular, loopback binding is not treated as protection from other users on the same host.

Evidence:

- [SLURM Dashboard security model](https://github.com/Charlie-Wang-03/slurm-dashboard/blob/main/SECURITY.md)
- [SLURM Dashboard AGENTS.md](https://github.com/Charlie-Wang-03/slurm-dashboard/blob/main/AGENTS.md)

**Sightline** keeps a fuller canonical report for the DSH Web ToolView while sending a narrower model-facing projection that omits absolute workspace paths and full diagnostic messages by default.

Evidence:

- [Sightline product contract](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/PRODUCT_CONTRACT.md)

**jev-testbench** distinguishes an agent instruction from a real security mechanism, keeps live credentials outside Git, audits publication boundaries, and treats committed measurement logs as intentionally public data.

Evidence:

- [jev-testbench security model](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/SECURITY.md)

### Portability and Locality Are Means, Not Goals

**Sightline** keeps its shipped core local-first and network-free because that serves privacy, determinism, and product scope, while allowing networked documentation and compatibility research during development.

Evidence:

- [Sightline product contract](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/PRODUCT_CONTRACT.md)
- [Sightline AGENTS.md](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/AGENTS.md)

**AI4Math Radar** preserves the heavier native AIHOT runtime while keeping it inactive under the current `static-chatgpt` operating profile. Capability preservation and active operational responsibility are treated as separate decisions.

Evidence:

- [AI4Math Radar README](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/README.md)
- [Active deployment profile](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/deployment/active.json)

## Selected Decision Rules in Practice

### Add AGENTS.md when stable context repeatedly matters

The clearest evidence is not the number of repositories containing `AGENTS.md`, but how different their contracts are.

For example, [SLURM Dashboard PR #1](https://github.com/Charlie-Wang-03/slurm-dashboard/pull/1) added a concise root `AGENTS.md` because stable security, side-effect, privacy, and validation boundaries materially affected repeated agent work. The same calibration explicitly avoided unrelated CI-matrix, dependency, product, and release changes.

### Make CI proportional to the changed surface

[AI4Math Radar PR #62](https://github.com/Charlie-Wang-03/ai4math-radar/pull/62) introduced a conservative content-only fast path. An edit limited exactly to the canonical selected-content file keeps the content validator, static build, and output smoke checks while skipping unrelated native runtime, database, backend, and Docker work. Any broader change falls back to full CI.

This is an example of narrowing validation only when the changed surface can be classified reliably.

### Publish releases as useful historical snapshots

**jev-testbench** uses `v0.1.0` as an immutable scientific evidence anchor while later repository and publication work continues separately.

Evidence:

- [v0.1.0 public evidence freeze](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/docs/evidence/v0.1.0/PUBLIC_EVIDENCE_FREEZE.md)

**Sightline** records exact-artifact publication and post-release verification rather than treating release creation alone as proof of correctness.

Evidence:

- [Sightline release checklist](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/RELEASE_CHECKLIST.md)

### Require explicit approval for high-impact changes

The [GitHub profile maintenance contract](https://github.com/Charlie-Wang-03/Charlie-Wang-03/blob/main/MAINTENANCE.md) distinguishes ordinary maintenance from identity, privacy, security, governance, and other high-impact changes that require explicit owner approval.

The same pattern appears in project-specific agent instructions where release creation, visibility changes, destructive operations, or trust-boundary changes are not implied by a request to inspect or edit.

### Use bilingual documentation where it serves real audiences

Public entry surfaces are bilingual in projects such as:

- [SLURM Dashboard](https://github.com/Charlie-Wang-03/slurm-dashboard)
- [Sightline](https://github.com/Charlie-Wang-03/dsh-sightline)
- [AI4Math Radar](https://github.com/Charlie-Wang-03/ai4math-radar)
- [the GitHub profile repository](https://github.com/Charlie-Wang-03/Charlie-Wang-03)

The pattern is selective rather than symmetric: public-facing entry points are translated where useful, while operational or internal technical material is not automatically duplicated.

### Introduce abstraction after real variation exists

**Sightline** has three concrete agent-specific discovery and precedence implementations. Their differences are isolated behind adapters while the comparison core remains free of agent-specific filesystem rules and DSH runtime dependencies.

Evidence:

- [Sightline architecture](https://github.com/Charlie-Wang-03/dsh-sightline/blob/main/docs/ARCHITECTURE.md)

### Bound externally costly execution

**jev-testbench** requires explicit request ceilings for live API work. A bulk `run-all` operation refuses to start unless `--max-requests` covers the selected tier, and the behavior is itself tested.

Evidence:

- [jev-testbench reproducibility guide](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/docs/guides/reproducibility.md)
- [Offline integration tests](https://github.com/Charlie-Wang-03/jev-testbench/blob/main/tests/test_integration_offline.py)

### Calibrate behavioral thresholds from evidence

**AI4Math Radar** treats selection thresholds as calibration decisions rather than intuition-only constants. Its project instructions require representative or gold examples before changing selection behavior, and its calibration documentation provides a concrete path for collecting candidate data.

Evidence:

- [AI4Math Radar AGENTS.md](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/AGENTS.md)
- [Selection documentation](https://github.com/Charlie-Wang-03/ai4math-radar/blob/main/docs/selection.md)

## What Is Deliberately Not Claimed

These examples show adoption, not causation.

This page does not claim that:

- a listed preference caused a project to succeed;
- every preference is equally mature or equally well represented;
- every project should copy the same implementation;
- unlisted projects do not use these preferences;
- the examples constitute an industry standard or external validation of these preferences.

The index should stay selective. New examples are worth adding when they make an engineering decision materially clearer, not merely because another repository happens to resemble an existing pattern.
