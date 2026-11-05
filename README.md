# AI-Image-Lab

**A collection of independently installable AI-image skills for Codex.** This is **not** a single giant master skill.

> First skill status: `ai-model-photography` **v0.2 experimental** on branch `experiment/ai-model-photography-v0.1`. It has **not** been merged into `main` or passed real Codex/image-model testing yet.

## Independent skills

| Skill | Responsibility | State |
| --- | --- | --- |
| [ai-model-photography](.agents/skills/ai-model-photography/SKILL.md) | **Diagnose and optimize existing commercial model prompts**, convert vague words into observable instructions, retain identity/garment/scene/reference locks, minimize edits | v0.2 experimental |
| commercial-image-reverse-engineer | Commercial image analysis and reverse engineering | Planned import; separate existing repository untouched |
| lighting-and-shadow | Photography light/shadow analysis and prompt optimization | Planned |

## Why v0.2?

The initial draft incorrectly centered on **generating a new model-photography prompt**. The supplied article actually teaches a different primary job: **take an existing prompt and improve vague language**. The refactored skill now performs:

```text
原始提示词
 -> 标记模糊、遗漏、冲突、串图、物理问题、重复词
 -> 锁定原有主体/服装/场景/光影/图像职责
 -> 只替换需要改写的句子
 -> 输出优化后提示词 + 精简修改依据
 -> 用单变量 A/B 实验验证
```

See [vague-to-visual dictionary](.agents/skills/ai-model-photography/references/vague-to-visual.md) and [case library](.agents/skills/ai-model-photography/references/case-library.md).

## Install only this skill on Windows Codex (experimental branch)

In **PowerShell**:

```powershell
$repo = Join-Path $env:TEMP 'AI-Image-Lab-trial'
$dest = Join-Path $HOME '.agents\skills\ai-model-photography'
if (Test-Path $repo) { throw "Temp folder exists: $repo; choose a new path instead of deleting it blindly." }
if (Test-Path $dest) { throw "Skill already installed: $dest; back up and compare before upgrading." }
git clone --depth 1 --branch experiment/ai-model-photography-v0.1 https://github.com/smaball117/AI-Image-Lab.git $repo
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Copy-Item -Path (Join-Path $repo '.agents\skills\ai-model-photography') -Destination $dest -Recurse
python (Join-Path $dest 'scripts\validate_skill.py')
python (Join-Path $dest 'scripts\test_optimization_cases.py')
```

Requires Git and Python. This only copies **one** skill to `%USERPROFILE%\.agents\skills\ai-model-photography`. Reopen Codex if necessary.

## First Codex behavior test

Paste an existing prompt and call the skill explicitly:

```text
$ai-model-photography
只优化提示词，不要帮我策划新画面：
“图1是沙发场景，图2是男孩脸，图3是衣服，
男孩自然坐着，光线柔和，衣服有质感。
保留图1的光影，图2的脸和图3服装颜色、结构都不能改变。”
请指出模糊词与冲突，再输出最小改动版本，并标注修改点。
```

**Expected:** locks reference roles, replaces "自然/柔和/有质感" with observable, scene-compatible instructions, does **not** invent a bed, change the face, invent ribbed cloth or add a new lighting direction.

See [full test protocol](.agents/skills/ai-model-photography/tests/README.md). We must test Codex invocation separately from scripted static checks and actual image generation. Do not claim a successful model result from a golden-case example.

## Provenance

- [User-supplied ZCOOL article: AI模特的真实感如何做到](https://www.zcool.com.cn/work/ZNzQxMzAyODQ=.html), 口木文化x何柳健, 2026-09-11.
- Examples here extract ideas and patterns; no wholesale copying of the article's lengthy prompts.
