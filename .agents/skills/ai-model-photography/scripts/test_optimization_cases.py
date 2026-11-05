#!/usr/bin/env python3
"""Validate the *curated golden examples*; does not invoke an LLM or image generator."""
from pathlib import Path
import json
import sys
root = Path(__file__).resolve().parents[1]
data = json.loads((root/"tests"/"optimization-cases.json").read_text(encoding="utf-8"))
errors=[]
cases=data["cases"]
if len(cases)<10: errors.append("Expected 10 or more examples")
ids=[x["id"] for x in cases]
if len(ids)!=len(set(ids)): errors.append("Duplicate IDs")
for case in cases:
    o=case["optimized"]
    if o.strip()==case["input"].strip(): errors.append(case["id"]+": unchanged input")
    for v in case["must_keep"]+case["must_include"]:
        if v not in o: errors.append(case["id"]+": missing "+v)
    for v in case["must_avoid"]:
        if v in o: errors.append(case["id"]+": forbidden "+v)
if errors:
    print("FAIL: "+str(len(errors))+" golden-case issue(s)")
    for e in errors: print(" - "+e)
    sys.exit(1)
print("PASS:",len(cases),"golden-case text invariants.")
print("NOTICE: This checks examples, not Codex activation, generated responses, or image quality.")
