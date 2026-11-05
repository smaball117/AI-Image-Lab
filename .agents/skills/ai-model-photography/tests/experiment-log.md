# Experiment log: AI Model Photography v0.2 Prompt Optimizer

Status: **remote static checks passed; Codex behavior and model A/B NOT YET VERIFIED**.

| Date | Stage | Test | Status | Evidence |
| --- | --- | --- | --- | --- |
| 2026-11-05 | Source audit | Supplied ZCOOL article: vague adjectives, 5 realism axes, long case studies | Done | `references/case-library.md` and `references/vague-to-visual.md` |
| 2026-11-05 | Remote static | Fetched skill files from GitHub, checked YAML meta, 12 internal links, optimizer mission terms | **PASS** | Independent JS verification: 14 required files |
| 2026-11-05 | Golden examples | 12 curated input-to-rewrite examples checked against must-keep/must-include/must-avoid strings | **PASS (static only)** | Independent JS checks after correcting G09; does not run a model |
| 2026-11-05 | CI setup | GitHub Actions workflow for Python structural + authored case checks | **CREATED, run not verified** | `.github/workflows/validate-ai-model.yml` |
| | Local Python | `scripts/validate_skill.py` and `scripts/test_optimization_cases.py` | Not run in this session | GitHub Actions / user Windows runner needed |
| | Codex activation | Explicit skill + implicit positive + non-target negative | Not run | User local Codex unavailable here |
| | Codex rewrite quality | At least 5 independent prompt rewrites | Not run | Need real Codex outputs |
| | Image model | 3 A/B original-versus-optimized comparisons | Not run | Need actual image model outputs |

Static test checks **our authored golden examples**, not the response of Codex to an arbitrary input prompt. Actual optimization efficacy, reference fidelity and generated image results are not established until user-side runtime tests.

## Main change from v0.1

**OLD**: generated new studio prompts from briefs. **NEW**: diagnose an existing prompt, protect user constraints, replace only vague/conflicting fragments, explain changes and design controlled A/B trials.
