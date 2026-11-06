# AI-Image-Lab

面向商业视觉生产的独立 AI Skills 实验室。每个 Skill **单独安装、单独使用**，不合并成大而全的总控 Skill。

## AI Model Photography · 模特提示词优化器

当前在 **`experiment/ai-model-photography-v0.3`** 分支，已把 Chat 中的研究方法与用户实测反馈整理为**候选正式版**。无须重新开始 A/B，先完成一次实际 Codex 调用验收即可。

| 资源 | 作用 |
| --- | --- |
| [📖 Markdown 使用手册](.agents/skills/ai-model-photography/docs/USAGE.md) | 安装、使用和常见问题 |
| [🖥️ HTML 图文使用手册](.agents/skills/ai-model-photography/docs/usage-manual.html) | 可下载浏览器离线打开，有复制指令按钮 |
| [技能主文件](.agents/skills/ai-model-photography/SKILL.md) | AI Agent 实际执行的提示词优化流程 |
| [完整提示词案例](.agents/skills/ai-model-photography/examples/briefs.md) | 18岁韩国卷发少女持唇釉、耳机青年模特、童装男孩 |
| [研究经验](.agents/skills/ai-model-photography/references/field-notes.md) | 四轮主要反馈与证据边界 |
| [一次性验收](.agents/skills/ai-model-photography/tests/README.md) | Codex 能否正确发现与调用 |

### 这个 Skill 做什么

**用户给一句模糊描述，输出一段能直接用于 AI 生图的中文提示词。** 按原文章的方法，从人物、镜头、光影、肤质、姿态、材质、高清画质等维度补充具体可见信息。

例如：

```text
$ai-model-photography
18岁韩国少女，卷发，手拿一支唇釉。
模特真实好看，高级美妆广告，光线柔和，高清。
帮我优化成一段完整、可以直接复制的中文生图提示词。
```

无需参考图。不默认生成图片、修复旧图、放大照片或不断要求 A/B 实验。优先整体画面与产品焦点，不堆微观毛孔词、固定百分比和复杂手指动作。

### 不同 Skill 的分工

| Skill | 功能 | 进度 |
| --- | --- | --- |
| [ai-model-photography](.agents/skills/ai-model-photography/SKILL.md) | **从模糊文字生图需求优化为高质感 AI 模特摄影提示词** | 候选正式版 |
| commercial-image-reverse-engineer | 商业图片解析与反推（独立技能，不混入本技能） | 后续整理 |
| lighting-and-shadow | 专项布光和光影分析（独立技能） | 后续开发 |

### 安装

参照 [使用手册](.agents/skills/ai-model-photography/docs/USAGE.md#3-windows-上仅安装一次)。Windows Codex 的用户级 Skills 目录按当前文档使用 `%USERPROFILE%\.agents\skills\ai-model-photography`。旧版如存在先备份并避免重复发现。

### 来源与状态

提示词转换结构来自用户提供的站酷《[AI模特的真实感如何做到](https://www.zcool.com.cn/work/ZNzQxMzAyODQ=.html)》，用户 Chat 测试经验详见 [field-notes.md](.agents/skills/ai-model-photography/references/field-notes.md)。GitHub 上的静态检查、Codex 实际调用和图片生成结果属于不同证据级别，不能互相代替。

**正式合并 `main` 前，保留一次 Codex 本地烟雾测试这一关。**
