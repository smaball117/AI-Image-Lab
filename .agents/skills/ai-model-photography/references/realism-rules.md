# Translating model-photo adjectives into observable cues

Use only the dimensions relevant to the user's specific problem. These are photographic intentions, not measured guarantees.

| Vague word | Observable controls | Common failure to check |
| --- | --- | --- |
| Beautiful / suitable | age group, facial contour, eye shape, hairstyle, expression that fits the brief | unrelated faces across variants |
| Realistic skin | subtle natural pores where appropriate, small hue variation, fine hair, age-appropriate texture, restrained retouch | plastic/waxy skin or exaggerated uniform pores |
| Natural pose | support points, balance, weight distribution, shoulder relaxation, joint angles, hands, gaze target | hands without contact, rigid limbs, unstable seated pose |
| Authentic clothing | fabric weave, garment construction, stitching, seam direction, correct fold tension and drape | added ribs, changed print, melted seams, weightless drape |
| Directional light | source location, approximate softness, affected planes, highlight/shadow falloff, dark-area treatment | conflicting catchlights, duplicated shadows, pasted-on illumination |
| Photographic | framing and perspective intention, readable focal plane, realistic depth transition | wide-angle facial distortion, unintentionally cropped garment |

## Decision sequence

1. **Commercial purpose**: identify what must be legible: child's garment, makeup, eyewear, skin, or a product in use.
2. **Subject identity**: retain the exact face/body attributes provided. Do not invent demographic detail when a visual reference already defines it.
3. **Pose mechanics**: position pelvis, feet/hands, back support and gaze. Standing poses need balance; seated poses need a real seat and fabric contact.
4. **Garment mechanics**: visible silhouette -> neckline/sleeves/hem -> stitching and actual textile -> folds caused by the action. Avoid contradicting the referenced material.
5. **Skin and hair**: preserve a photographic distribution of microtextures. For children, avoid adult wrinkles and adult fashion retouching.
6. **Light and material**: derive source direction from the scene; show which planes are bright, where shadows fall, how fabric and hair respond.
7. **Lens and crop**: specify medium/close-up/full shot, eye level/high angle, perspective without distortion, exact region to remain in frame. Numeric focal lengths/apertures are optional cinematic shorthand, not an export or renderer contract.
8. **Finish**: retain natural color variation, clean focus on intended subject, remove unwanted artifacts without erasing physical cues.

## Pose templates: conditional, not universal

- Standing apparel: balanced center of gravity, relaxed shoulder line, clear garment front, arms apart enough to reveal sleeves and fit.
- Sofa seated: pelvis supported by sofa cushion, feet/resting legs anatomically coherent, gentle shoulder settling, hands rest on knee/cushion, garment visible.
- Walking moment: plausible stride and weight transfer, opposite arm swing, gravity-consistent hair and hem motion, no frozen floating foot.
- Head-and-shoulders portrait: head/neck alignment, natural eye line and expression, hair edges separate from background.
- Product interaction: anatomically correct fingers grasp actual object surfaces; face and product both readable.

## Common anti-patterns

- "85mm, f/2.8, 8K, RAW" as a substitute for subject, lighting, and composition.
- A universal 1:2 ratio or universally forbidden shadows. Contrast must serve the intended mood.
- Always adding skin wrinkles, freckles, pores, or a stronger jaw, regardless of the person.
- Automatically inventing furniture, garments, logos, props, windows, and product parts.
- Long negative prompt lists that override the requested positive scene or conflict with model behavior.
- Taking outfit/facial attributes from a pose-only reference.
- Overly detailed anatomy instructions that create contradictions in a simple pose.

## Model adaptation

Default to plain Chinese natural language with clear references and priorities. Only introduce platform-specific prompt syntax or weighting if the target model supports it and the user requests it. Prefer 1-2 well-motivated physical descriptions over a list of magic style words.
