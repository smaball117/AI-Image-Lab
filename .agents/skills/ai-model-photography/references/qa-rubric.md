# Quality gate and single-variable repair

Use this rubric before delivery as a **prompt consistency check**, and after generation as a **visual inspection**. Do not present prompt-only checks as proof of output success.

## Score each 0, 1, 2 after inspecting an actual output

| Criterion | 0 = fails | 1 = partial | 2 = clear pass |
| --- | --- | --- | --- |
| Identity/age | wrong person or age | similar but drifting | correct anchor |
| Wardrobe fidelity | wrong item, color or print | minor drift | construction/material/print intact |
| Pose/anatomy | impossible joints/contact | slight stiffness | balanced and coherent |
| Lighting coherence | contradicts source/shadow | plausible but uneven | consistent across subject and scene |
| Material realism | plastic or pasted texture | some unnatural patches | convincing skin, hair, fabric |
| Camera/composition | wrong angle/crop or lost product | slight framing drift | focal priority and crop correct |
| Constraint compliance | forbidden elements or unintended grid | minor extra details | all hard constraints respected |

Maximum 14. **Provisional acceptance rule**: no 0 on identity/age, wardrobe or hard-constraint compliance; overall >= 12/14. This is a working team threshold, not an externally validated score.

## Before generation: prompt preflight

- Are reference-image role assignments explicit and non-overlapping?
- Is there any explicit contradiction (lock original light vs request a radically different light)?
- Does a body actually touch a valid existing support surface?
- Is the garment reference allowed to determine the exact fabric and pattern?
- Will the camera preserve the intended garment/head/hand region?
- Have unnecessary props, default ornaments and redundant negatives been excluded?

## After generation: minimum-change loop

1. Inspect the output and record **one primary failure** with visible evidence.
2. Map it to an editable dimension: identity, wardrobe, pose, lighting, materials, camera, constraints.
3. Write a patch instruction: "Keep [all verified correct invariants]; only change [one dimension] in [location] to [observable result]."
4. Regenerate with unchanged references and controlled settings where the tool permits.
5. Compare against the same criteria. Record model, prompt version, image references, pass/fail and the changed variable.
6. If the edit reintroduces a severe failure, roll back and try a different isolated correction.

### Example

Observed failure: child sits partly suspended beside sofa; garment print correct.

Patch: Keep the same child, face, clothing print, scene and light; move pelvis fully onto the existing sofa cushion, align thighs with cushion surface, feet resting naturally, and add soft cushion compression/contact shadows. Change no wardrobe detail.

Do **not** also change camera angle, hair, color grade and background.
