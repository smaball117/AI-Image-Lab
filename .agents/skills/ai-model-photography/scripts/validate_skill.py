#!/usr/bin/env python3
"""Validate packaging metadata, required files, internal links and mission wording.
This does NOT invoke Codex, image generation, or test output quality.
"""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "agents/openai.yaml",
    "references/vague-to-visual.md", "references/case-library.md",
    "references/decision-rules.md", "references/field-notes.md",
    "references/optimization-qa.md", "references/source-notes.md",
    "examples/briefs.md", "docs/USAGE.md", "docs/usage-manual.html",
    "tests/README.md", "tests/optimization-cases.json",
    "tests/experiment-log.md",
    "scripts/validate_skill.py", "scripts/test_optimization_cases.py",
]
errors = []
for name in required:
    if not (root / name).is_file():
        errors.append("missing: " + name)

skillfile = root / "SKILL.md"
skill = skillfile.read_text(encoding="utf-8") if skillfile.exists() else ""
match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", skill, re.S)
if not match:
    errors.append("bad SKILL.md front matter")
else:
    name = re.search(r"^name:\s*(.+)$", match.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", match.group(1), re.M)
    if not name or name.group(1).strip() != "ai-model-photography":
        errors.append("incorrect name")
    if not desc or not (40 <= len(desc.group(1).strip()) <= 1024):
        errors.append("invalid description length")

for link in re.findall(r"\]\(([^)]+)\)", skill):
    if link.startswith(("http://", "https://", "#")):
        continue
    target = (root / link).resolve()
    if root not in target.parents or not target.is_file():
        errors.append("broken SKILL.md link: " + link)

for term in ("模糊", "光影", "皮肤", "姿态", "服装", "对焦", "不要求参考图"):
    if term not in skill:
        errors.append("missing required mission term: " + term)

html_file = root / "docs" / "usage-manual.html"
if html_file.is_file():
    html = html_file.read_text(encoding="utf-8")
    for token in ('lang="zh-CN"', 'id="start"', 'id="example"', 'id="install"', 'id="copy-cmd"', "ai-model-photography"):
        if token not in html:
            errors.append("HTML manual missing " + token)

casefile = root / "tests" / "optimization-cases.json"
if casefile.is_file():
    try:
        cases = json.loads(casefile.read_text(encoding="utf-8"))["cases"]
        ids = [c["id"] for c in cases]
        if len(cases) < 14 or len(set(ids)) != len(ids):
            errors.append("expected at least 14 unique test cases")
    except (KeyError, ValueError, TypeError) as exc:
        errors.append("invalid test specs: " + str(exc))

if errors:
    print("FAIL:", len(errors), "issue(s)")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("PASS:", len(required), "required files, front matter, internal links, manual and test specs")
print("NOT TESTED: Codex invocation, actual prompt quality, real image output")
