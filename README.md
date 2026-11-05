# AI-Image-Lab

**Modular AI image generation skills for Codex.** One public GitHub repository, independent skills; users choose which to install.

> **Experimental status:** First skill is on `experiment/ai-model-photography-v0.1` pending Windows Codex and real image-generation acceptance. The `main` branch is not changed.

## Skills

| Skill | Focus | Status |
| --- | --- | --- |
| [ai-model-photography](.agents/skills/ai-model-photography/SKILL.md) | Realistic commercial models, reference-image routing, apparel and skin realism, pose, targeted repair | v0.1 experimental |
| commercial-image-reverse-engineer | Commercial product/image reverse engineering and reference analysis | Planned migration from existing repository; not copied yet |
| lighting-and-shadow | Lighting design and shadow/material response | Planned; not created yet |

These are **three separately installable skills**, not a monolithic master skill. Each skill owns all files required for its operation.

## First experimental skill: AI Model Photography

### 1. Install independently on Windows

For the current experimental branch, open **PowerShell** and run:

```powershell
$repo = Join-Path $env:TEMP 'AI-Image-Lab-trial'
$dest = Join-Path $HOME '.agents\skills\ai-model-photography'
if (Test-Path $repo) { throw "Temporary folder already exists: $repo. Choose a new temporary folder; do not delete an unknown folder." }
if (Test-Path $dest) { throw "Skill already installed: $dest. Back up and compare before replacing it." }
git clone --depth 1 --branch experiment/ai-model-photography-v0.1 https://github.com/smaball117/AI-Image-Lab.git $repo
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Copy-Item -Path (Join-Path $repo '.agents\skills\ai-model-photography') -Destination $dest -Recurse
python (Join-Path $dest 'scripts\validate_skill.py')
```

The installed skill lives at `%USERPROFILE%\.agents\skills\ai-model-photography`. Requires Git and Python. This directory is supported for user-level skills by current Codex documentation. Restart Codex if it does not immediately show the new skill.

Alternatively, ask Codex's `$skill-installer` to install the **specific folder from this branch**; do not ask it to install the whole collection. The `$skill-installer` implementation and available options may vary by Codex version.

### 2. Test an explicit invocation

```text
$ai-model-photography 图1是客厅沙发场景，图2是男孩面部参考，图3是纯棉家居服。
请保持图1原有场景与光影，让男孩自然坐在沙发上，生成一段3:4单张商业摄影提示词。
给出参考图分工、最终提示词和3项最重要的检查点。
```

Attach the real reference images when testing. If images are unavailable, the agent should avoid inventing their actual contents.

### 3. Validate and log results

- `python scripts/validate_skill.py` inside the installed skill folder checks structure only.
- Run the routing and image-generation trials in [test protocol](.agents/skills/ai-model-photography/tests/README.md).
- Record actual outcomes in [experiment log](.agents/skills/ai-model-photography/tests/experiment-log.md).
- Merge only when tested; an uploaded file is not proof of successful Codex invocation or image quality.

## Design principles

- Independent skills, no cross-skill filesystem dependency.
- Only authorized references control face, scene, clothing, body, or light.
- Strong lock-and-repair behavior; do not change the successful parts of an image during one small correction.
- Photographic controls are **intent descriptions**, not guarantees that a generation model obeys actual camera physics or pixel export specs.
- Third-party research is cited as provenance; copyrighted source articles are not copied wholesale.

## Sources

- [AI 模特的真实感如何做到, 口木文化x何柳健](https://www.zcool.com.cn/work/ZNzQxMzAyODQ=.html)
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Agent Skills specification](https://agentskills.io/specification)
