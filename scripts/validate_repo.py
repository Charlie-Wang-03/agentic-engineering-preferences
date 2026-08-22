#!/usr/bin/env python3
"""Lightweight structural validation for the Agentic Engineering Review repository.

The validator intentionally uses only the Python standard library. It checks
repository invariants that are cheap to verify automatically without turning a
Markdown-first project into a heavy documentation toolchain.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "AGENTS.md",
    "AGENT_REVIEW_PROTOCOL.md",
    "assets/readme/hero.svg",
    "docs/principles.md",
    "docs/principles.zh-CN.md",
    "docs/decision-framework.md",
    "docs/decision-framework.zh-CN.md",
    "docs/practices.md",
    "docs/practices.zh-CN.md",
    "docs/governance.md",
    "docs/governance.zh-CN.md",
    "templates/AGENTS.md.template",
    "templates/DECISION_RECORD.md",
    "templates/PROJECT_REVIEW.md",
    "templates/PROJECT_REVIEW.zh-CN.md",
]

BILINGUAL_PAIRS = [
    ("README.md", "README.zh-CN.md"),
    ("docs/principles.md", "docs/principles.zh-CN.md"),
    ("docs/decision-framework.md", "docs/decision-framework.zh-CN.md"),
    ("docs/practices.md", "docs/practices.zh-CN.md"),
    ("docs/governance.md", "docs/governance.zh-CN.md"),
    ("templates/PROJECT_REVIEW.md", "templates/PROJECT_REVIEW.zh-CN.md"),
]

PRINCIPLE_HEADINGS = [
    "## 1. Open by Default",
    "## 2. Agent-Native, Human-Accountable",
    "## 3. Portable over Model-Agnostic",
    "## 4. User Sovereignty & Privacy by Default",
    "## 5. Local-First When Practical",
    "## 6. Justified Dependencies",
    "## 7. Progressive Usability",
    "## 8. Verifiable by Default",
    "## 9. Reversible Change",
]

REQUIRED_PHRASES = {
    "README.md": [
        "Agentic Engineering Review",
        "Status: v0.4",
        "assets/readme/hero.svg",
        "AGENT_REVIEW_PROTOCOL.md",
        "Diagnostic Score",
        "Evidence Coverage",
        "N/A",
    ],
    "README.zh-CN.md": [
        "Agentic Engineering Review",
        "当前状态：v0.4",
        "assets/readme/hero.svg",
        "AGENT_REVIEW_PROTOCOL.md",
        "Diagnostic Score",
        "Evidence Coverage",
        "N/A",
    ],
    "docs/principles.md": [
        "Agentic Engineering Methodology",
        "Outcomes over Dogma",
    ],
    "docs/decision-framework.md": [
        "Default → Conflict → Trade-off → Exception → Evidence → Revisit",
    ],
    "docs/governance.md": [
        "Repository as a Test Subject",
        "Language and Documentation Policy",
        "Diagnostic Scoring Governance",
        "AGENT_REVIEW_PROTOCOL.md",
    ],
    "AGENTS.md": [
        "Agentic Engineering Review",
        "Agentic Engineering Methodology",
        "Deviation is allowed; unexplained deviation is not.",
        "Repository Invariants",
        "AGENT_REVIEW_PROTOCOL.md",
    ],
    "AGENT_REVIEW_PROTOCOL.md": [
        "Agentic Engineering Review",
        "Agentic Engineering Methodology",
        "read-only review mode",
        "Evidence Before Judgment",
        "Determine Applicability Before Scoring",
        "NE — Not Enough Evidence",
        "Evidence Coverage",
        "Diagnostic Score",
        "70%",
        "N/A",
    ],
    "templates/PROJECT_REVIEW.md": [
        "Agentic Engineering Review",
        "Applicability First",
        "NE — Not Enough Evidence",
        "Diagnostic Scale",
        "Diagnostic Score",
        "Evidence Coverage",
        "N/A",
    ],
}

LEGACY_IDENTITY = "Agentic Open-Source Engineering Methodology"
LEGACY_IDENTITY_FILES = [
    "README.md",
    "README.zh-CN.md",
    "AGENTS.md",
    "AGENT_REVIEW_PROTOCOL.md",
    "CONTRIBUTING.md",
    "docs/principles.md",
    "docs/principles.zh-CN.md",
    "templates/PROJECT_REVIEW.md",
    "templates/PROJECT_REVIEW.zh-CN.md",
]

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def error(message: str) -> None:
    print(f"ERROR: {message}")


def validate_required_files() -> int:
    failures = 0
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            error(f"missing required file: {relative}")
            failures += 1
    return failures


def validate_bilingual_pairs() -> int:
    failures = 0
    for english, chinese in BILINGUAL_PAIRS:
        en_exists = (ROOT / english).is_file()
        zh_exists = (ROOT / chinese).is_file()
        if en_exists != zh_exists:
            error(f"bilingual pair incomplete: {english} <-> {chinese}")
            failures += 1
    return failures


def validate_principles() -> int:
    failures = 0
    for relative in ("docs/principles.md", "docs/principles.zh-CN.md"):
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in PRINCIPLE_HEADINGS:
            if heading not in text:
                error(f"{relative} is missing principle heading: {heading}")
                failures += 1
    return failures


def validate_required_phrases() -> int:
    failures = 0
    for relative, phrases in REQUIRED_PHRASES.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                error(f"{relative} is missing required phrase: {phrase}")
                failures += 1
    return failures


def validate_legacy_identity() -> int:
    failures = 0
    for relative in LEGACY_IDENTITY_FILES:
        path = ROOT / relative
        if path.is_file() and LEGACY_IDENTITY in path.read_text(encoding="utf-8"):
            error(f"legacy project identity remains in current identity-bearing file: {relative}")
            failures += 1
    return failures


def validate_hero_svg() -> int:
    path = ROOT / "assets/readme/hero.svg"
    if not path.is_file():
        return 0

    text = path.read_text(encoding="utf-8")
    failures = 0
    required = [
        'viewBox="0 0 1200 400"',
        "<title",
        "<desc",
        "Agentic Engineering Review",
    ]
    for item in required:
        if item not in text:
            error(f"hero.svg is missing required SVG invariant: {item}")
            failures += 1

    forbidden = [
        "<script",
        "foreignObject",
        'href="http://',
        'href="https://',
        "href='http://",
        "href='https://",
    ]
    for item in forbidden:
        if item in text:
            error(f"hero.svg contains fragile or remote SVG content: {item}")
            failures += 1

    return failures


def validate_local_markdown_links() -> int:
    failures = 0
    markdown_files = list(ROOT.glob("*.md"))
    markdown_files += list((ROOT / "docs").glob("*.md"))
    markdown_files += list((ROOT / "templates").glob("*.md"))

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue

            file_target = unquote(target.split("#", 1)[0])
            if not file_target:
                continue

            resolved = (path.parent / file_target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                error(f"{path.relative_to(ROOT)} links outside repository: {target}")
                failures += 1
                continue

            if not resolved.exists():
                error(f"broken local link in {path.relative_to(ROOT)}: {target}")
                failures += 1

    return failures


def main() -> int:
    failures = 0
    failures += validate_required_files()
    failures += validate_bilingual_pairs()
    failures += validate_principles()
    failures += validate_required_phrases()
    failures += validate_legacy_identity()
    failures += validate_hero_svg()
    failures += validate_local_markdown_links()

    if failures:
        print(f"Repository validation failed with {failures} issue(s).")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
