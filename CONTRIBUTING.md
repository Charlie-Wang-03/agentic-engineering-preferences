# Contributing

Thank you for considering a contribution to the Agentic Open-Source Engineering Methodology.

This repository is currently in private incubation. The contribution model is intentionally lightweight while the methodology is still being validated.

## What Makes a Good Contribution

Prefer changes that improve engineering decision quality rather than simply adding more terminology, files, or rules.

Before proposing a new principle, rule, practice, template, or automation, ask:

1. Does it address a real engineering problem?
2. Is it reusable across more than one narrow scenario?
3. Is it a Principle, Decision Rule, Practice, governance rule, or repository implementation detail?
4. If it is a Principle, is it primarily a value, default, constraint, decision rule, or preferred means?
5. Is it already covered by an existing principle or document?
6. Is it likely to remain useful as specific AI tools change?
7. Does it materially improve a decision, adoption path, agent context, or verification path?

## Contribution Expectations

- Keep changes focused and reviewable.
- Explain important trade-offs and exceptions.
- Preserve document responsibilities instead of duplicating normative text.
- Review the paired language document when changing core bilingual methodology content.
- Do not translate operational files merely for symmetry.
- Do not introduce private data, secrets, machine-specific paths, or unpublished project material.
- Avoid unnecessary dependencies, automation, generated artifacts, and process overhead.
- Preserve the distinction between durable principles, the Decision Framework, fast-moving Practices, and Governance.

## Language

English is the repository's default operational language for international open-source collaboration.

Simplified Chinese is maintained as a first-class reading path for the README and core methodology documents. User-facing templates may also be paired when translation materially improves adoption.

Operational files such as `AGENTS.md`, workflow configuration, and contribution mechanics do not require automatic translation. For paired documents, preserve semantic equivalence without forcing literal translation.

## Pull Requests

A pull request should state:

- what problem it addresses;
- what methodology or repository layer it changes;
- why the change is justified;
- how it was validated;
- whether any promised bilingual pair was reviewed;
- whether derived artifacts or agent instructions need to change.

The project follows the meta-principle **Outcomes over Dogma**. Deviation from a default is acceptable when the trade-off is explicit and justified.

For methodology changes, also follow [Methodology Governance](docs/governance.md).
