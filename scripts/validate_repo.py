#!/usr/bin/env python3
"""Lightweight structural validation for Agentic Engineering Preferences."""

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
    "SECURITY.md",
    "AGENTS.md",
    "docs/preferences.md",
    "docs/decision-rules.md",
    "docs/project-conventions.md",
    "docs/used-in-practice.md",
    "templates/AGENTS.md.template",
]

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

CURRENT_IDENTITY_FILES = [
    "README.md",
    "README.zh-CN.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
]

def error(message: str) -> None:
    print(f"ERROR: {message}")

def validate_required_files() -> int:
    failures = 0
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            error(f"missing required file: {relative}")
            failures += 1
    return failures

def validate_readme_pair() -> int:
    en = (ROOT / "README.md").is_file()
    zh = (ROOT / "README.zh-CN.md").is_file()
    if en != zh:
        error("README bilingual pair is incomplete")
        return 1
    return 0

def validate_current_identity() -> int:
    failures = 0
    for relative in CURRENT_IDENTITY_FILES:
        path = ROOT / relative
        if path.is_file() and "Agentic Engineering Preferences" not in path.read_text(encoding="utf-8"):
            error(f"{relative} does not reference the current project identity")
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
    failures += validate_readme_pair()
    failures += validate_current_identity()
    failures += validate_local_markdown_links()

    if failures:
        print(f"Repository validation failed with {failures} issue(s).")
        return 1

    print("Repository validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
