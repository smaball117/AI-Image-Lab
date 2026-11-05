# Supplemental after-generation image QA (not the prompt optimization score)

**Primary optimizer acceptance lives in [optimization-qa.md](optimization-qa.md).** This file may be used only after the user runs a real image model and shares the images for visual review.

Record 0 / 1 / 2 for each:

- model identity/age retained
- outfit structure/color/print retained
- anatomy and contact plausible
- light consistent with original reference
- skin/fabric/hair physically convincing
- intended camera focus and framing retained
- forbidden additions absent

A good text rewrite may still produce a poor image. Do not mark this rubric as passed without inspecting the output. For a targeted edit, also check **regressions**: did the optimized result worsen any untouched dimension?

For ablations, compare original prompt A with optimized B using as nearly identical image-model settings and references as practical.
