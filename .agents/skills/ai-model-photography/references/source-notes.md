# Source provenance and evidence limitations

## User-supplied article

- 《AIGC— AI模特的真实感如何做到》
- Author: 口木文化x何柳健
- Published in clipping: 2026-09-11
- URL: https://www.zcool.com.cn/work/ZNzQxMzAyODQ=.html

Primary educational principle from source: replace vague prompts (“漂亮”, “细腻”, “柔和”, “自然”, “真实”, “高清”) by decomposed visible properties. The article organizes photographic realism by skin, lighting, pose, clothing, camera, plus targeted exclusions and diverse scenario examples including headphone model, beauty cosmetics, standing/walking/sitting, high/low key studio portraits, eyewear and clothing/background variants.

**The article is third-party editorial advice.** Its statements that models cannot understand subjective words literally, exact 85mm/f stop/light ratio or 8K strings, and claimed workflow performance should be treated as heuristics, not deterministic facts. The original long prompts/images are not copied into this repository.

## Skill-specific design choices

- Prompt optimization as first-class job, **not** default photoshoot generation.
- LOCK / EDIT / UNKNOWN preservation.
- Minimal rewriting and single-variable A/B testing.
- Child-appropriate skin and clothing-sensitive commercial application.
- Reference-image role isolation and contradiction detection.
- Test fixtures, sample rewrites, and text-score rubric.

These are design decisions informed by the user's commercial workflow; they are not verbatim claims from the article.

Evidence labels: `source example` vs `editorial inference` vs `verified output`. Do not label text reasoning or a static checker as a generated-image test.
