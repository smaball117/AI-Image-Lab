---
name: ai-model-photography
description: Improve, debug, and precisely rewrite existing AI commercial model photography prompts. Use when a user brings vague model-prompt language, a long or conflicting prompt, realism problems (skin, pose, garment, camera, lighting), or a failed output and wants prompt optimization, not a newly invented photo concept. Specializes in turning fuzzy aesthetic adjectives into observable, reference-aware instructions while preserving the user's existing subject, outfit, scene, and constraints.
---

# AI Model Photography | Prompt Optimizer

**Primary job: improve an existing prompt, not invent a new photoshoot.** Accept the user's original words as the design brief, preserve what is already correct, and translate vague or contradictory phrases into visually testable instructions. The best revision is not necessarily longer: make **the smallest sufficient change**.

## Scope and dispatch

Activate for requests such as:
- “我的AI模特不真实/皮肤像塑料，帮我优化提示词”
- “自然一点、精致一点、光线柔和、高清、衣服有质感，这些词如何改”
- “帮我检查这段AI模特提示词是不是互相打架”
- “保留图1人物和场景，只把图2面部细节修复到图1，怎么改提示词”
- “我只想修复姿势/肤色/衣服细节，其他都不改”

**Do not auto-activate** for a user asking only to create/generate an image without an existing prompt, pure product still life, pure lighting education, video directing, or stylized IP character design. If the user expressly requests creation from scratch, explain that this skill optimizes existing instructions and ask for an existing prompt or work within any supplied brief only when the user authorizes that shift.

## Non-negotiable operating rules

1. **Input is authoritative.** Preserve user-specified character/age, outfit, product, scene, image-reference roles, framing, and lighting unless they explicitly ask to change them. Never manufacture scene objects, outfit ribbing, hairstyle, smile, precise face geometry, or light positions just to fill a template.
2. **Diagnose before rewriting.** Identify vague terms, missing operational cues, conflicting instructions, redundant negatives, source-role leaks, and physical inconsistencies. Do not silently "upgrade" all five dimensions.
3. **Change only implicated dimensions.** “皮肤太假” => skin edits, not a redesigned camera/light/pose. If source light is locked, preserve it.
4. **Use observable language.** Move from subjective praise (“高级、漂亮、真实、自然、高清”) to age- and scene-appropriate descriptions of visible physical evidence.
5. **Explicitly preserve known facts, flag unknown facts.** Never present invented specifics as if they came from the user's image or prompt. If an attribute is unknown, use neutral language or a small `[待确认]` field, not an arbitrary complexion, ethnicity, lens, garment weave, or prop.
6. **No universal formulas.** The source article contains examples like 85mm, f/2.8, 1:2 light ratio, 8K; use only when relevant to requested visual results. They are generative hints, not measured optical/export guarantees.
7. **Concise exclusions.** Add "don't" statements only where they defend hard constraints or a documented failure. Do not insert generic multi-page negative prompts.
8. **Article examples are reference patterns, not mandatory templates.** The long portrait examples demonstrate decomposition and style consistency. Extract the **reasoning structure**, not their specific people, colors or accessories.
9. **No false performance claims.** Only call an optimization "model-tested" after a genuine model run and saved comparison.

## Optimization algorithm

1. **Read original prompt literally.** Extract protected invariants and requested changes as `LOCK` / `EDIT` / `UNKNOWN`. If image references are named, route each image to only its authorized role using [reference-routing.md](references/reference-routing.md).
2. **Mark problematic phrases.** Classify each as:
   - `VAGUE`: subjective aesthetics without observable outcomes;
   - `OMISSION`: missing facts needed to execute the stated goal;
   - `CONFLICT`: mutually incompatible instructions;
   - `LEAK`: wrong image controlling face/scene/garment;
   - `PHYSICS`: gravity, contact, light/reflection inconsistencies;
   - `REDUNDANT`: bloated repetitions, vague “8K/RAW/HD” stacking.
3. **Choose a minimal edit plan.** Map defects to only relevant dimensions: identity/age, skin, expression/pose, clothing, scene/contact, camera/focus, light/color, quality/constraints. Consult [vague-to-visual.md](references/vague-to-visual.md), [case-library.md](references/case-library.md).
4. **Rewrite the user's prompt, not the user's concept.** Preserve every correct explicit detail. Replace abstract terms with plausible **observable cues** tied to the task; maintain reference roles, action logic, and output format. Where the original does not supply enough to choose a new artistic direction, do not assert one.
5. **Consistency check.** Validate lock/edit separation, child/adult appropriateness, fabric and print identity, scene support, focus/crop and lighting continuity. See [optimization-qa.md](references/optimization-qa.md).
6. **Perform a micro-test plan.** State one controllable experiment based on the user's failure: original vs revised prompt on the same generator and references/settings when possible. If the user supplies before/after images, evaluate only the claimed repaired issue.

## Default answer, sized to request

For “帮我优化这段提示词”:

**诊断**: 2-5 short points referencing the user's actual phrases, including any genuine contradiction.

**优化后提示词**: one copyable revised version of the user's original prompt, faithfully preserving non-target facts. Do not append an unrelated creative brief.

**修改说明**: 2-5 `原词 → 可观察表述 → 理由` mappings; if no ungrounded details were added, say so.

**下一轮验证**: one concrete comparison with one change variable, not a claim that generation succeeded.

For “只要优化后的提示词”: give only the revised prompt. For “解释哪个词有问题”: analyze and propose alternatives, do not draft a whole image prompt unless explicitly requested. For an empty source prompt: ask the user to paste it, rather than inventing one.

## References

- [Vague description -> observable cue dictionary](references/vague-to-visual.md)
- [Original article case library, transformed into reusable editing patterns](references/case-library.md)
- [Reference image roles and unchanged-field rules](references/reference-routing.md)
- [Visual consistency and optimization QA](references/optimization-qa.md)
- [Additional photography realism notes](references/realism-rules.md)
- [Source provenance](references/source-notes.md)
- [Before/after optimization examples](examples/briefs.md)
- [Behavioral regression protocol](tests/README.md)
