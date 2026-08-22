#!/usr/bin/env python3
"""Lightweight repository-structure validation for the methodology repo.

Uses only the Python standard library so the validation itself does not add a
runtime dependency burden.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "AGENTS.md",
    "docs/principles.md",
    "docs/principles.zh-CN.md",
    "docs/decision-framework.md",
    "docs/decision-framework.zh-CN.md",
    "docs/practices.md",
    "docs/practices.zh-CN.md",
    "templates/AGENTS.md.template",
    "templates/DECISION_RECORD.md",
]

BILINGUAL_PAIRS = [
    ("README.md", "README.zh-CN.md"),
    ("docs/principles.md", "docs/principles.zh-CN.md"),
    ("docs/decision-framework.md", "docs/decision-framework.zh-CN.md"),
    ("docs/practices.md", "docs/practices.zh-CN.md"),
]

REQUIRED_PHRASES = {
    "docs/principles.md": [
        "Outcomes over Dogma",
        "Agent-Native, Human-Accountable",
        "Verifiable by Default",
        "Reversible Change",
    ],
    "docs/decision-framework.md": [
        "Default → Conflict → Trade-off → Exception → Evidence → Revisit",
    ],
    "AGENTS.md": [
        "Deviation is allowed; unexplained deviation is not.",
    ],
}


def error(message: str) -> None:
    print(f"ERROR: {message}")


def main() -> int:
    failures = 0

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            error(f"missing required file: {relative}")
            failures += 1

    for english, chinese in BILINGUAL_PAIRS:
        en_exists = (ROOT / english).is_file()
        zh_exists = (ROOT / chinese).is_file()
        if en_exists != zh_exists:
            error(f"bilingual pair incomplete: {english} <-> {chinese}")
            failures += 1

    for relative, phrases in REQUIRED_PHRASES.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                error(f"{relative} is missing required phrase: {phrase}")
                failures += 1

    if failures:
        print(f"Repository validation failed with {failures} issue(s).")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
