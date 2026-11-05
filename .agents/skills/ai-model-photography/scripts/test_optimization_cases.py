#!/usr/bin/env python3
"""Validate authored test specifications and demonstration coverage.
No LLM call: this is NOT a Codex behavior test.
"""
from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1]
data=json.loads((root/"tests/optimization-cases.json").read_text(encoding="utf-8"))
cases=data["cases"]
errors=[]
if len(cases)<12:errors.append("expected at least 12 cases")
for case in cases:
    if not case.get("input") or not case.get("expected_focus"):
        errors.append(case.get("id","?")+": missing input/focus")
    if case.get("mode")!="route_out" and not case.get("expected_dimensions"):
        errors.append(case.get("id","?")+": missing dimensions")
    if "reference" in case.get("expected_focus","").lower():
        errors.append(case.get("id","?")+": reference image must not be mandatory")
examples=(root/"examples/briefs.md").read_text(encoding="utf-8")
for phrase in ["白色耳机","皮肤细腻","光线柔和","自然站立","高清","双眼","对焦","避免"]:
    if phrase not in examples:
        errors.append("Full example missing "+phrase)
if errors:
    print("FAIL fixture specs",len(errors))
    for item in errors:print("-",item)
    sys.exit(1)
print("PASS",len(cases),"authored scenario specs + six-dimension example coverage")
print("NOTE: tests have not asked Codex to produce or evaluate a new prompt")
