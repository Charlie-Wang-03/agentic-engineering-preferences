## Problem

What problem or decision does this pull request address?

## Change Type

- [ ] Principle
- [ ] Decision Framework
- [ ] Practice
- [ ] Governance
- [ ] Agent Review Protocol / Scoring
- [ ] Template / Agent Instruction
- [ ] Repository Implementation / Maintenance

## Rationale and Trade-offs

Why is this change justified? If it deviates from an existing default, briefly state the default, conflict, trade-off, and exception.

For principle changes, explain why clarification of an existing principle is insufficient and what recurring evidence supports the change.

For review-protocol or scoring changes, explain what observed failure, ambiguity, or evidence justifies changing current behavior.

## Validation

What was checked or run?

- [ ] `python3 scripts/validate_repo.py`
- [ ] Resulting diff reviewed
- [ ] No secrets, private paths, or unpublished private material introduced

## Documentation, Protocol, and Language Impact

- [ ] Relevant canonical document was updated rather than duplicated elsewhere
- [ ] Any promised English / Simplified Chinese pair was reviewed or updated
- [ ] `AGENT_REVIEW_PROTOCOL.md`, `templates/PROJECT_REVIEW*`, README one-prompt entry, and scoring references were checked when review behavior changed
- [ ] Derived artifacts such as `AGENTS.md`, templates, or validation rules were checked when relevant
- [ ] Not applicable

## Reversibility / Follow-up

Is rollback straightforward? Is there a condition under which this decision should be revisited?
