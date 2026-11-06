# AI 模特商业摄影提示词优化器 · 使用手册

> 一句话：**你说模糊需求，Skill 把它改成一段能直接用于 AI 生图的真实高清商业模特摄影提示词。**

[打开图文版 HTML 手册](usage-manual.html)（建议下载该 HTML 后用浏览器打开）。

## 1. 它解决什么问题？

输入：“18岁韩国少女，卷发，拿一支唇釉，真实、好看、高清。”

输出：一段完整中文生图提示词，按文章研究过的**人物与产品 → 镜头与构图 → 光影 → 皮肤 → 姿态 → 服装/产品材质 → 高清质量与反向约束**展开。既要人物漂亮，也要产品清楚、手势合理、光线连贯、背景不抢戏。

**不需要参考图**，这是新照片的**生图提示词优化**，不是上传旧图高清修复。它也不会自动替你运行 Nano Banana、即梦等生图工具。

## 2. 三步开始

1. 将本目录 `ai-model-photography` 放在 Codex 可识别的 Skills 目录。当前推荐的用户级目录是 `%USERPROFILE%\.agents\skills\ai-model-photography`（参见 [OpenAI Skills 文档](https://developers.openai.com/api/reference/cli)）。
2. 重新打开 Codex 对话。
3. 输入：`$ai-model-photography 18岁韩国少女，卷发，手里拿一支唇釉，写实高清美妆广告，帮我优化成完整生图提示词。`

对于已有一段很长的提示词，直接把全文粘贴进去，说“请优化，保留人物、产品、背景、服装”。如果你只希望修改某一部分，说“只改姿态”或“只把光影表达写具体，其他都别改”。

## 3. Windows 上仅安装一次

**如果从 GitHub 安装候选版**，在 PowerShell 执行（需要已安装 Git）：

```powershell
$repo = Join-Path $env:TEMP 'AI-Image-Lab-ready'
$dest = Join-Path $HOME '.agents\skills\ai-model-photography'
if (Test-Path $repo) { throw '临时目录已存在，请更换临时目录名称。' }
git clone --depth 1 --branch experiment/ai-model-photography-v0.3 https://github.com/smaball117/AI-Image-Lab.git $repo
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
if (Test-Path $dest) {
    $backup = "$dest.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    Move-Item -Path $dest -Destination $backup
    Write-Host "旧版已备份到 $backup"
}
Copy-Item -Path (Join-Path $repo '.agents\skills\ai-model-photography') -Destination $dest -Recurse
Write-Host "已安装至 $dest"
```

安装前检查是否有**其他位置的同名旧 Skill**。旧版本若仍存在于 Codex 可发现的位置，可能出现调用混淆；请确认只让一个最新副本参与发现。不要盲目删除其他目录。

安装后可选运行：
```powershell
python (Join-Path $dest 'scripts\validate_skill.py')
python (Join-Path $dest 'scripts\test_optimization_cases.py')
```
这些脚本**只验证文件和人工编写的测试用例格式**，不调用生图模型。建议完成一次下文的人工验收。

## 4. 三种日常使用指令

**一句模糊描述**
```text
$ai-model-photography
18岁韩国少女，卷发，手拿一支唇釉，妆容干净，有高级感，光影自然，高清。优化成可直接复制到 Nano Banana Pro 的完整中文生图提示词。
```

**把已有提示词变得更专业**
```text
$ai-model-photography
帮我优化以下提示词，保持年龄、发型、服装、商品和场景不变。只补足不明确的摄影描述，并输出最终提示词：
[粘贴你的原提示词]
```

**只优化一个点**
```text
$ai-model-photography
下面的提示词人物很好，但动作太假。只改姿态与持物接触，不动光影、人物外貌和背景：
[粘贴原提示词]
```

## 5. 怎样判断它工作正常？

第一次只验收一次，使用本手册的韩国少女+唇釉例子：

- 是否输出完整**可直接复制**的中文生图提示词？
- 是否保留**18岁、韩国少女、卷发、唇釉**？
- 是否有明确景别、光源方向、持物动作、商品可读性与焦点？
- 是否保持背景简洁且不过度堆砌毛孔？
- 有没有错误地要求参考图、发明品牌、擅自输出图片或把“高清”当旧图修复？

符合这些要求，证明 Skill 的**基本调用路径可用**；真实图片质感仍以用户实际生图为准。

## 6. 常见问题

**Q：必须上传模特图片吗？** 不用。直接打字就能优化。只有你主动指定参照关系时才处理。

**Q：会自动生成图吗？** 不会。本 Skill 交付一段提示词，再把它复制到你使用的生图工具。

**Q：为什么不写满毛孔、8K、85mm、f/2.8？** 之前的 Chat 观察表明，细化毛孔未见明显收益；具体镜头参数也应服从景别和商品是否清楚。数字不是高质感的保证。

**Q：我输入的商品包装会不会变？** 如果你没有写某款唇釉具体的形状、品牌和颜色，Skill 不会假装知道真实包装；要精准匹配特定产品，需要补充真实产品信息。

**Q：可以用在童装吗？** 可以。明确年龄和服装，Skill 会强调自然姿态、适龄肤质、版型、颜色、工艺和服装清晰度。

**Q：输出太长怎么办？** 加一句“精简到一段，突出人物、产品、光影、姿态和镜头，禁止堆重复词”。

## 7. 经验来源与适用边界

方法来自用户提供的站酷《AI模特的真实感如何做到》：模糊词分解为外貌、皮肤、光影、姿态、材质、镜头、画质与反向约束。

本对话的实际观察：背景控制改善了耳机广告的主体突出；人物50%/70%占比差不多；皮肤微观词差不多；唇釉持物细化差不多且效果都好。这些是**用户当前场景的定性反馈**，不是可普遍外推的科学测试。

更多见 [实测记录](../references/field-notes.md)、[案例库](../examples/briefs.md)、[测试协议](../tests/README.md)。
