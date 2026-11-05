# Reference routing and constraint hierarchy

## First construct an image-role map

| Image | Authorized information | Explicitly forbidden transfer |
| --- | --- | --- |
| Image 1 (example) | scene, camera, pose, existing light | face and clothing if other references own them |
| Image 2 (example) | face identity and hair if specified | scene, clothing, pose |
| Image 3 (example) | body proportions only | face, age, clothing |
| Image 4 (example) | actual garment construction, print and color | identity, environment |

**This is an example, not a fixed universal upload order.** Always use the user's assigned order, including any custom ordering. If the scene image is specified as the only anchor, do not add extra furniture, doors, props, or competing colors.

## Priority order

1. Current user request and explicit image-to-role assignment.
2. Hard invariants: identity, exact garment/product construction, original framing/light for local edits.
3. Real-world coherence: anatomical plausibility, gravity, contact, perspective, shadows.
4. Requested stylistic choices: mood, camera language, finish.
5. Optional decorative details. Drop these first if they compete with higher-priority requirements.

### Conflicts

- If the user says "match reference 1 lighting exactly" and a pose reference shows a different light, keep reference 1 lighting.
- If the user wants a new camera angle yet also says "same composition exactly", identify the contradiction; default to preserving the anchor for a local edit, or explain the necessary change for a new viewpoint.
- If a reference image has a bed but the actual scene anchor has only a sofa, translate the action to a feasible sofa pose, without inventing a bed.
- If a face reference is a contact sheet or nine-grid, use it solely for identity recognition; **never** accidentally render the contact-sheet grid.

## Repair modes

| User's requested repair | Can change | Preserve unless explicitly changed |
| --- | --- | --- |
| Face repair | facial geometry and microtexture to match designated face reference | pose, outfit, scene, light direction, crop |
| Garment correction | garment seams, neckline, fabric, colors, print, fit | identity, body, camera, scene |
| Pose transfer | body joint angles and physically compatible contact | identity, outfit, anchoring objects and lighting |
| Lighting correction | motivated light direction, highlights, shadows, material response | identity, clothing, action, geometry |
| Camera variant | viewpoint, crop, perspective; re-evaluate visible background | subject and apparel identity, plausible scene |

**Do not promise perfectly identical pixels** after an image model edit. State which features are locked and inspect the result.
