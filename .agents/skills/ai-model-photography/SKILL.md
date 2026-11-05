---
name: ai-model-photography
description: Design, reverse-analyze, or repair AI-generated realistic commercial model photography prompts for apparel, kidswear, beauty, accessories, and lifestyle campaigns. Use when a person/model is a principal visual subject, especially for face/identity consistency, natural pose, garment fidelity, skin realism, scene interaction, and reference-image role control. Do not use for product-only still life, pure lighting consultation, video direction, or stylized character/IP development.
---

# AI Model Photography

Produce controllable prompts and targeted revisions for **realistic commercial photographs with human models**. This skill produces a brief, image-role map, execution-ready prompt, and quality checks; it does not itself guarantee an image or run an image model.

## Invoke / avoid

- Invoke for commercial model portraits, apparel model campaigns, multi-reference model composites, pose transfer, face fidelity, clothing fidelity, and diagnosis of unnatural AI people.
- Avoid for product-only photography, standalone lighting-design analysis, video/storyboard generation, cartoon character design, or generic beautification unrelated to commercial model photography. Do not swallow those tasks merely because an image contains a background person.
- If another specialized skill is present, route to the skill best matching the **primary requested change**, rather than silently running every installed skill.

## Input contract

Extract whatever the user actually supplied. Do not invent missing uploaded images or describe unseen details.

| Field | Capture |
| --- | --- |
| Task | new image / reference transfer / local repair / variant |
| Output | count, aspect ratio, crop, resolution if specified |
| Image roles | image 1..N: scene, face, body, garment, pose, product, lighting, style |
| Human | age group, appearance, identity lock, expression, hair |
| Garment/product | exact visual identity, colors, construction, print, fit, priority |
| Environment | physical furniture, location, available objects, forbidden objects |
| Camera | framing, viewpoint, lens intent, focus, depth of field |
| Light | existing-image lock or new lighting direction |
| Constraints | must preserve, may change, must exclude |
| Model | target generator if specified; otherwise use plain language |

Ask **one** clarification only if a missing input makes the requested identity or reference routing impossible to infer; otherwise state a conservative assumption and proceed.

## Workflow (mandatory)

1. **Route the job.** Determine the deliverable and whether this skill fits. For edits, write a one-sentence change boundary: what changes and what must not.
2. **Assign image roles.** Use explicit image indices. Only inherit attributes from references granted that role. For conflicts, user-written instructions outrank the default convention. Read [reference-routing.md](references/reference-routing.md).
3. **Lock invariants.** Identity (facial structure, age group), garment (pattern, fabric, seams, fit), product, composition, or lighting according to the user's actual requirements. Rank hard constraints above styling suggestions.
4. **Translate subjective direction into visible cues.** Choose only relevant features from [realism-rules.md](references/realism-rules.md). Specify physical skin, hair, pose mechanics, cloth-body contact, light behavior, framing, and scene placement. Do not force all dimensions into every edit.
5. **Write one coherent prompt.** Put task and reference priority first; then subject/wardrobe/action; then scene and camera; then light/material/focus; end with concise, **task-specific** exclusions. Prefer explicit positive descriptions over long repetitive negative lists.
6. **Run a preflight.** Check reference leakage, identity drift, incorrect garments, body/environment collisions, contradictory lighting, lens/crop mismatch, duplicate persons, and invented objects. Use [qa-rubric.md](references/qa-rubric.md).
7. **Repair through minimum changes.** If the user provides a failed output, identify the most likely faulty dimension and issue a revised prompt changing that dimension alone wherever possible. Preserve the user's original successful features.

## Hard constraints

- **Reference authority is scoped.** A pose-only reference never authorizes importing its face, outfit, age, scene, or gender. An outfit-only reference never authorizes swapping identity.
- **No unsupported physical promises.** Focal length, aperture, lighting ratios, "4K/8K", RAW, and weighted prompt syntax are hints, not guarantees that the generator physically simulates optics or exports that resolution. Favor their intended visible outcomes; only promise exact pixels if an actual output tool supports them.
- **Age-appropriate realism.** Preserve the subject's age. Do not apply mature facial lines to children or standardize all people into adult beauty faces. No sexualized presentation of minors.
- **Clothing is not generic.** Do not add ribbing, logos, ornaments, changes of color, or fabric structure merely because they are common in prompts. Refer to actual garment references.
- **World consistency.** Contact shadows, support surfaces, body weight, gaze direction, and occlusion must match the actual scene. Do not add beds or other objects absent from the supplied scene.
- **Edit discipline.** For face-only correction, maintain the original framing, pose, body, clothing, background, shadows, and facial illumination unless explicitly unlocked.
- **Truthful evaluation.** A textual checklist cannot prove visual quality. Report actual generation results only after images have been generated and inspected.

## Default output

When the user asks for a reusable prompt, return:

1. **Image-role map / locks:** short, explicit, include image indices; omit if no references.
2. **Final prompt:** one directly copyable Chinese natural-language prompt (or requested language), with no internal analysis inserted.
3. **Targeted exclusions:** only material risks, not a generic wall of negatives.
4. **Preflight & next test:** the 2-4 most failure-prone elements and the first single-variable test.

For requests explicitly asking **only the prompt**, output the final prompt and only essential image-role constraints. For criticism/diagnosis, provide failure -> cause hypothesis -> minimal correction; do not rewrite unrelated dimensions.

## Supporting material

- [Reference routing and locks](references/reference-routing.md)
- [Photography realism rules](references/realism-rules.md)
- [Image QA rubric and correction loop](references/qa-rubric.md)
- [Source provenance and limitations](references/source-notes.md)
- [Representative briefs and outputs](examples/briefs.md)
- [Test protocol](tests/README.md)
