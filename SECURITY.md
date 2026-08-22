# Security Policy

Agentic Engineering Review is primarily a Markdown-first review protocol and methodology repository. Security issues can still arise in repository automation, agent-facing instructions, accidental disclosure, or guidance that could cause unsafe behavior when followed by an AI agent.

## Supported Version

During the `v0.x` public-preview phase, only the latest state of the default branch is actively maintained. Older commits and draft protocol behavior are historical references, not separately supported release lines.

## Reporting a Vulnerability

Please **do not open a public issue** for a suspected vulnerability, leaked secret, or other security-sensitive report.

Preferred reporting path:

1. Use this repository's **private vulnerability reporting / Security Advisory** flow when it is available.
2. If private vulnerability reporting is unavailable, contact the maintainer privately using the contact information on the maintainer's GitHub profile.

Include, when practical:

- a concise description of the issue;
- affected file, workflow, protocol behavior, or commit;
- reproduction steps or a minimal example;
- likely impact;
- any suggested mitigation.

Do not include real credentials, private target-project material, or unnecessary personal data in the report.

## What Counts as Security-Relevant

Examples include:

- exposed credentials or private data in the repository or its history;
- workflow permissions broader than necessary;
- agent instructions that can reasonably lead to unauthorized writes, destructive actions, secret disclosure, or unintended data transfer;
- vulnerabilities in repository automation or third-party Actions;
- unsafe defaults that materially contradict the documented read-only review boundary.

General methodology disagreements, scoring disagreements, documentation quality issues, and ordinary feature requests should use normal Issues or Pull Requests instead.

## Disclosure

Please allow reasonable time to investigate and remediate a valid report before public disclosure. The maintainer will aim to acknowledge actionable reports and keep the reporter informed when practical.
