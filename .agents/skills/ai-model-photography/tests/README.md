# AI Model Photography: acceptance protocol

**Status: unverified for Codex discovery or image quality until a real user-side run is logged.** Static validation is not a substitute for inference tests.

## Level 1: deterministic structural inspection

From the `ai-model-photography` folder:

```bash
python scripts/validate_skill.py
```

Checks metadata, required file dependencies, local Markdown links, fixture ids, positive/negative scope and content placeholders. No third-party Python dependencies.

## Level 2: Codex routing and prompt output

Install this skill independently in a supported Codex skills directory, restart Codex if not recognized, and run these exact explicit and implicit probes:

1. Explicit: `$ai-model-photography 图1是客厅沙发，图2是男孩面部，图3是纯棉家居服。保持图1光影，让男孩自然坐在沙发上。给我一段用于 Nano Banana 的3:4中文提示词。`
2. Implicit: `我想修复参考图人物的塑料皮肤，只改皮肤质感不改衣服和构图。`
3. Implicit negative: `一瓶精华液的纯产品静物，分析玻璃反射并生成布光提示词。` (this skill should not auto-activate)
4. Implicit negative: `做一个3D卡通水母头人物IP设计。` (this skill should not auto-activate)

For image-specific cases, attach real images when available. Text-only probes cannot establish image-reference parsing ability.

Observe and save:
- Is the skill visible by name?
- Was it activated for each positive but not unrelated negative task?
- Did it map the actual image indices without inheriting attributes from the wrong source?
- Did it honor hard locks, avoid invented props and output only the requested number of images/prompts?
- Did it include a targeted preflight rather than a wall of redundant negative instructions?

## Level 3: actual generated-image evaluation

Pick at least **three** real-user briefs: garment-on-sofa, face-only restoration, and one adult model portrait. Use the intended image model and preserve prompt/image/settings versions where possible. Score with `references/qa-rubric.md`.

Run one controlled single-variable repair per failing result, and compare before/after for that dimension. Do not count non-run cases as passed.

## Acceptance gates

- Structural checker passes.
- Manual Codex discovery/explicit invoke passes.
- All four routing probes behave as intended.
- At least 3 evaluated image outputs, no severe identity, wardrobe, or reference-scope failures, and at least 12/14 per output on provisional rubric.
- Results and failures documented in `tests/experiment-log.md`.

If any gate fails, keep the skill on experimental branch and edit only the failed design part. Merge to main only after actual trial evidence.
