#!/usr/bin/env python3
"""Check authored scenario specifications, not model responses."""
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "tests" / "optimization-cases.json").read_text(encoding="utf-8"))
cases = data["cases"]
errors = []
if len(cases) < 14:
    errors.append("expected 14+ scenario cases")
for case in cases:
    if not case.get("id") or not case.get("input") or not case.get("expected_focus"):
        errors.append("missing id/input/focus")
    if case.get("mode") != "route_out" and not case.get("expected_dimensions"):
        errors.append(case.get("id", "?") + ": missing dimensions")

examples = (root / "examples" / "briefs.md").read_text(encoding="utf-8")
for token in ("18岁", "韩国", "卷发", "唇釉", "耳机", "12岁", "沙发", "柔光", "对焦", "避免"):
    if token not in examples:
        errors.append("examples missing: " + token)
experience = (root / "references" / "field-notes.md").read_text(encoding="utf-8")
for token in ("E02", "E03", "E04", "E05", "差不多"):
    if token not in experience:
        errors.append("experience log missing: " + token)

if errors:
    print("FAIL:", len(errors), "scenario specification issues")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("PASS:", len(cases), "authored scenarios and example coverage")
print("NOTE: no Codex response or image-generation model was executed")
