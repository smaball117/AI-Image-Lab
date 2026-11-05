#!/usr/bin/env python3
"""Standalone structural checks for AI Model Photography Prompt Optimizer.
No third-party modules. Does not test Codex or image-generation behavior.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/reference-routing.md",
    "references/vague-to-visual.md",
    "references/case-library.md",
    "references/optimization-qa.md",
    "references/realism-rules.md",
    "references/source-notes.md",
    "examples/briefs.md",
    "scripts/validate_skill.py",
    "scripts/test_optimization_cases.py",
    "tests/README.md",
    "tests/optimization-cases.json",
    "tests/experiment-log.md",
]
errors = []
for p in required:
    if not (root / p).is_file():
        errors.append("missing: " + p)

skill = (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", skill, re.S)
if not m:
    errors.append("SKILL.md requires YAML frontmatter")
else:
    name = re.search(r"^name:\s*(.*)$", m.group(1), re.M)
    desc = re.search(r"^description:\s*(.*)$", m.group(1), re.M)
    if not name or name.group(1).strip() != "ai-model-photography":
        errors.append("wrong YAML name")
    if not desc or len(desc.group(1).strip()) < 40 or len(desc.group(1).strip()) > 1024:
        errors.append("invalid YAML description")

for link in re.findall(r"\]\(([^)]+)\)", skill):
    if link.startswith(("http:", "https:", "#")):
        continue
    target = (root / link).resolve()
    if root not in target.parents or not target.is_file():
        errors.append("bad relative link: " + link)

for keyword in ["optimization", "vague", "existing prompt", "smallest"]:
    if keyword.lower() not in skill.lower():
        errors.append("optimizer mission unclear: " + keyword)

case_path = root / "tests" / "optimization-cases.json"
if case_path.is_file():
    try:
        data = json.loads(case_path.read_text(encoding="utf-8"))
        ids = [x["id"] for x in data["cases"]]
        if len(ids) < 10 or len(set(ids)) != len(ids):
            errors.append("need 10+ unique optimization cases")
    except (ValueError, KeyError, TypeError) as e:
        errors.append("invalid cases JSON: " + str(e))

if errors:
    print("FAIL:",len(errors),"issue(s)")
    for e in errors: print(" -", e)
    sys.exit(1)
print("PASS:", len(required), "required files; metadata, links, optimizer terms, case count")
print("NOTE: Does not prove actual Codex generation/activation.")
