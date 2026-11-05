#!/usr/bin/env python3
"""Stdlib-only structural validator for text-to-image model prompt skill.
It does not invoke Codex or an image-generation model.
"""
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "agents/openai.yaml", "references/vague-to-visual.md",
    "references/case-library.md", "references/optimization-qa.md",
    "references/source-notes.md", "examples/briefs.md",
    "tests/README.md", "tests/optimization-cases.json",
    "tests/experiment-log.md", "scripts/validate_skill.py",
    "scripts/test_optimization_cases.py",
]
errors=[]
for relative in required:
    if not (root / relative).is_file():
        errors.append("Missing "+relative)
skill_path=root/"SKILL.md"
text=skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
m=re.match(r"\A---\s*\n(.*?)\n---\s*\n",text,re.S)
if not m:
    errors.append("Missing YAML front matter")
else:
    name=re.search(r"^name:\s*(.+)$",m.group(1),re.M)
    desc=re.search(r"^description:\s*(.+)$",m.group(1),re.M)
    if not name or name.group(1).strip()!="ai-model-photography":
        errors.append("Incorrect skill name")
    if not desc or not 40<=len(desc.group(1).strip())<=1024:
        errors.append("Invalid description")
for target in re.findall(r"\]\(([^)]+)\)",text):
    if target.startswith(("https://","http://","#")):continue
    path=(root/target).resolve()
    if root not in path.parents or not path.is_file():
        errors.append("Bad link: "+target)
for keyword in ["高清","模糊","皮肤","光影","姿态","服装","对焦","不需要参考图"]:
    if keyword not in text: errors.append("Mission/dimension missing: "+keyword)
if not (root/"tests/optimization-cases.json").exists():
    errors.append("No fixtures")
else:
    try:
        data=json.loads((root/"tests/optimization-cases.json").read_text(encoding="utf-8"))
        ids=[case["id"] for case in data["cases"]]
        if len(ids)<12 or len(ids)!=len(set(ids)):
            errors.append("Expected at least 12 unique cases")
    except (KeyError,ValueError,TypeError) as exc:
        errors.append("Bad JSON: "+str(exc))
if errors:
    print("FAIL",len(errors))
    for e in errors:print("-",e)
    sys.exit(1)
print("PASS structural",len(required),"files; metadata, links, dimensions, fixtures")
print("NOTE: Real Codex and image-generation behavior remain unverified")
