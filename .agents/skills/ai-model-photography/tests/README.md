# v0.2: Prompt optimizer evaluation protocol

**Primary goal:** preserve supplied prompts and change vague/contradictory parts, not invent complete new shoots.

## Level 1: deterministic checks (Python, no dependencies)

From the `ai-model-photography` directory:

```powershell
python scripts/validate_skill.py
python scripts/test_optimization_cases.py
```

The first verifies files/frontmatter/links and fixture shape. The second checks **curated golden rewrite examples** for preserved phrases, required details, and forbidden additions. It **does not** generate AI rewrites and cannot prove model quality.

## Level 2: test actual Codex behavior

Explicit invocation:

```text
$ai-model-photography
这是我已有的提示词，请你只帮我优化，不要设计新画面：
"图1是沙发场景，图2是男孩脸，图3是衣服，男孩自然坐着，光线柔和，衣服要有质感。保留图1光影，服装结构和颜色不变。"
请标注模糊处，再输出最小改写版，最后说明你究竟改了哪些词。
```

Further prompts (run in separate Codex turns; compare with [golden examples](optimization-cases.json)):

1. **Skin only**: "保留图1人物、衣服、光线和构图。只有皮肤太塑料，请只优化这一小段提示词。"
2. **Specificity**: "把漂亮、细腻、柔和、自然、高清五个词拆为不同视觉变量，并解释选择条件，不要写整张照片的完整提示词。"
3. **Conflict**: "我的原文写了保持图1光影不变又写了新增左侧硬光，帮我指出冲突并给出最小修改。"
4. **No invention**: "场景图只有沙发，没有床。我的衣服是平针纯棉，不是坑条。不要增加床和罗纹。"
5. **Non-target**: "我只想从零生成一瓶玻璃精华液商业静物，没有人物。" -> Skill should not auto-trigger.
6. **Non-target**: "帮我设计20秒TVC动态分镜。" -> Skill should not auto-trigger.

Record whether it found the existing prompt, recognized the intended edit, avoided adding new faces/props/clothing and yielded a **minimal change**.

## Level 3: A/B model generation

After Codex rewrites have been approved, use the original and optimized prompts on the **same image tool** with same references/settings where possible. First test:
- age-appropriate skin texture without other changes
- sofa support/pose without changing outfit
- face-only restoration keeping background and original lighting

Record original and optimized prompts, model name/version, image files, visible success/failure, and rollback decisions in `experiment-log.md`. **No run, no PASS**.

## Acceptance criteria

- Static checks pass
- Codex explicit invocation and both positive/negative trigger checks pass
- For at least five distinct user prompts, optimized output preserves all hard locks and edits only target dimensions
- Three A/B image trials demonstrate intended improvement without losing correct details
- Test notes saved; keep branch experimental until all gates passed
