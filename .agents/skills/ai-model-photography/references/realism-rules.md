# Photography realism reference (secondary knowledge)

This file is **not** a prompt template. Use it only when diagnosing a relevant phrase in an **existing** user prompt. For the optimization workflow, start with [vague-to-visual.md](vague-to-visual.md), not this file. If a user asked for local skin correction, do not also rewrite camera, pose, garment and light.

## Choose observable cues conditionally

| Dimension | Observable features | When to use |
| --- | --- | --- |
| Skin | local fine texture, appropriate pore distribution, natural hue variation, subtle specular highlights | skin plasticity or beauty-retouch issue |
| Expression | gaze target, eyebrow/eye and mouth-muscle magnitude, facial asymmetry | empty/stiff face |
| Standing | balance, support foot, shoulder tension, limb angle | stiff posture |
| Sitting | pelvis support, weight distribution, hand support, foot placement, seat depression | floating or unstable seated model |
| Walking | stride phase, load-bearing foot, opposite arm swing, clothing inertia | unnatural walking freeze |
| Apparel | actual fiber/weave, drape, seam, cut, print, fold tension | garment appearance or fidelity |
| Camera | viewpoint, scene coverage, focus region, natural perspective and crop | wrong frame/focus |
| Light | existing source direction, affected surfaces, highlight, shadow edge and reflections | light mismatch |

## Non-default safeguards

- Protect exact clothing and faces when reference images control them.
- Child faces require child-appropriate skin. Do not turn them into small adults.
- Do not invent a ribbed garment when the garment image indicates plain fabric.
- Do not invent new scene objects for body support.
- Do not use universal 85mm, f/2.8, 8K, 1:2, smile or silhouette rules.
- One edit is one variable whenever the user asks for a targeted repair.
