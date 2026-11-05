# Experiment log: AI Model Photography v0.1

Status: **REMOTE STATIC CHECK PASS, CODEX AND IMAGE MODEL NOT YET TESTED**.

| Date | Probe | Tool/model | Result | Evidence or notes |
| --- | --- | --- | --- | --- |
| 2026-11-05 | Remote file presence, frontmatter, relative links, JSON cases | GitHub connector + independent JS checks | **PASS** | 11 files fetched; 9 relative links resolved; 6 positive and 4 negative test cases; description length 482 |
| | Local Python structure validator | Windows/Python | Not run | Run `python scripts/validate_skill.py` after installation |
| | Explicit skill invocation | Codex | Not run | |
| | Implicit scope positive | Codex | Not run | |
| | Implicit scope negative | Codex | Not run | |
| | Sofa apparel output | Image model | Not run | |
| | Face-only output | Image model | Not run | |
| | Adult beauty portrait | Image model | Not run | |

Remote static check is **not equivalent** to executing the Python validator or testing skill recognition in Codex. The current remote environment has no Codex CLI and cannot inspect the user's Windows installation.

Rubric: `../references/qa-rubric.md`. Do not mark an output as passed without inspected images.
