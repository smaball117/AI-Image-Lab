#!/usr/bin/env python3
"""Standalone static validator for the ai-model-photography skill (stdlib only).

Does not test Codex runtime discovery, image-generation quality or prompt compliance.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/reference-routing.md",
    "references/realism-rules.md",
    "references/qa-rubric.md",
    "references/source-notes.md",
    "examples/briefs.md",
    "tests/README.md",
    "tests/cases.json",
    "tests/experiment-log.md",
]
errors: list[str] = []

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

skill_path = ROOT / "SKILL.md"
if skill_path.is_file():
    text = skill_path.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        frontmatter = m.group(1)
        name = re.search(r"^name:\s*(.+)\s*$", frontmatter, re.M)
        desc = re.search(r"^description:\s*(.+)\s*$", frontmatter, re.M)
        if not name or name.group(1).strip() != "ai-model-photography":
            errors.append("Skill name is invalid or does not match folder")
        if not desc or not (10 <= len(desc.group(1).strip()) <= 1024):
            errors.append("Skill description missing or outside 10..1024 characters")
        if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip()):
            errors.append("Skill name must be lowercase kebab-case")

    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (ROOT / target).resolve()
        if ROOT not in resolved.parents and resolved != ROOT:
            errors.append(f"Link escapes skill root: {target}")
        elif not resolved.exists():
            errors.append(f"Broken SKILL.md link: {target}")

    if re.search(r"\bTODO\b|\bTBD\b|PLACEHOLDER", text, re.I):
        errors.append("Unresolved placeholder in SKILL.md")

fixture = ROOT / "tests" / "cases.json"
if fixture.is_file():
    try:
        data = json.loads(fixture.read_text(encoding="utf-8"))
        cases = data["cases"]
        ids = [x["id"] for x in cases]
        if len(cases) < 8:
            errors.append("Need at least 8 routing/test fixtures")
        if len(ids) != len(set(ids)):
            errors.append("Fixture ids must be unique")
        if not any(c.get("trigger") is True for c in cases):
            errors.append("Missing positive trigger cases")
        if not any(c.get("trigger") is False for c in cases):
            errors.append("Missing negative trigger cases")
        for c in cases:
            if not c.get("user_prompt") or not c.get("expected_focus"):
                errors.append(f"Incomplete case: {c.get('id', '?')}")
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid cases.json: {exc}")

if errors:
    print(f"FAIL: {len(errors)} structural issue(s)")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print(f"PASS: {len(REQUIRED)} required files, skill metadata, links and fixtures")
print("NOTICE: Codex discovery and actual image outputs remain unverified")
