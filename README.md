# AI-Image-Lab

**三个独立的 Codex Skills，将分别开发、测试与发布；本仓库不是单个巨大 Skill。**

## 当前 Skill 合集

| Skill | 功能 | 状态 |
| --- | --- | --- |
| [ai-model-photography](.agents/skills/ai-model-photography/SKILL.md) | **从一句模糊文字生图需求/初稿，拆成外貌、皮肤、光影、姿态、服装、镜头及高清质量，组合成完整的 AI 模特商业摄影提示词。** | v0.3 实验中 |
| commercial-image-reverse-engineer | 商业图片反推与分析（独立技能） | 后续迁移 |
| lighting-and-shadow | 光影分析及设计（独立技能） | 后续开发 |

> **无需上传参考图。** 第一个 Skill 的默认用法是“文字短提示词 → 更具体的文字生图提示词”。它不要求修复输入图片。“高清”明确指**最终新生成的模特照片**的目标画质、焦点与细节。

## 第一个 Skill 的能力

1. **漂亮** → 年龄/脸型/轮廓/发型/眉眼/唇形，匹配产品定位。
2. **细腻** → 适龄毛孔/肤理/细微色差/面部绒毛，避免蜡像磨皮。
3. **柔和** → 光源方向/明暗关系/高光位置/阴影过渡。
4. **自然** → 重心/肩膀/头部/视线/嘴角/手指和身体支撑。
5. **真实** → 皮肤+光影+姿态+服装材质+镜头相互统一。
6. **高清** → 目标生成分辨率意图/焦段/景深/对焦部位/画质细节及负面约束。

依据：[用户提供的站酷研究文章](https://www.zcool.com.cn/work/ZNzQxMzAyODQ=.html)。已按方法重新撰写 Skill，不直接复制作者长提示词。

## 在 Windows Codex 独立安装 v0.3 实验 Skill

PowerShell（需 Git 与 Python）：

```powershell
$repo = Join-Path $env:TEMP 'AI-Image-Lab-v03'
$dest = Join-Path $HOME '.agents\skills\ai-model-photography'
if (Test-Path $repo) { throw "Temporary clone directory exists; choose a new path." }
if (Test-Path $dest) { throw "Existing skill found. Back up and compare versions before replacing." }
git clone --depth 1 --branch experiment/ai-model-photography-v0.3 https://github.com/smaball117/AI-Image-Lab.git $repo
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Copy-Item -Recurse -Path (Join-Path $repo '.agents\skills\ai-model-photography') -Destination $dest
python (Join-Path $dest 'scripts\validate_skill.py')
python (Join-Path $dest 'scripts\test_optimization_cases.py')
```

仅安装 `ai-model-photography`，不会安装其他两个 Skill。若已有 v0.1/v0.2，请先备份，再按版本更新。重新启动 Codex 确保发现新 Skill。

## 首个必须通过的 Codex 测试

```text
$ai-model-photography
请按“漂亮→人物五官、细腻→肤理、柔和→光影、
自然→身体姿态、真实→皮肤光影服装镜头、
高清→生成照片的焦点与细节”逐项拆解，并将这句文字扩写成
能直接用来生成高清商业人像的完整提示词：

“一个年轻漂亮的欧美女孩，戴着白色耳机，皮肤细腻，
光线柔和，自然站立，真实一点，高清。”

不要让我上传参考图。高清指新生成的照片，不是修复原图。
```

请对照 [三个完整文字案例](.agents/skills/ai-model-photography/examples/briefs.md)、[测试协议](.agents/skills/ai-model-photography/tests/README.md) 验收。**文件结构检查通过不代表 Codex 已调用、也不代表生成照片达到高清。**

## 版本保护

- `main` 保持不变。
- 当前 v0.3 实验分支为 `experiment/ai-model-photography-v0.3`。
- 只有完成 Codex 实际调用和生图 A/B 测试后才考虑合并正式版。
