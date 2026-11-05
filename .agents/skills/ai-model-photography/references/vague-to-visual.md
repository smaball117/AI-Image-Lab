# 模糊语言 -> 可观察描述：变量词典

**Usage:** Match user intent and input constraints before selecting a rewrite. The below is a menu of possible *observables*, not a global prompt template. Avoid choosing unsupported specifics.

| 模糊词 | 拆解的问题 | 可执行的视觉维度 | 为什么/风险 |
| --- | --- | --- | --- |
| 漂亮 / 高级脸 | 用户希望哪种特征？是否已有脸参考？ | 轮廓、发型、眉眼、眼神、表情，或直接锁定现有脸 | 绝不能凭空改动已锁定的面容或年龄 |
| 皮肤细腻 / 真实 | 是塑料感、油光、假毛孔、肤色单一中的哪一种？ | 年龄相符的微观肤理、毛孔分布、局部色差、自然高光、脸颈过渡 | 细节不意味着“满脸毛孔”；儿童不应添加成熟皱纹 |
| 光线柔和 | 原场景光源是否锁定？高光还是阴影需要柔和？ | 保留光源方向；受光部位、阴影边缘柔和过渡、暗部层次 | 无参考不可凭空宣称“左侧45°、光比1:2” |
| 自然站立 / 自然坐 | 重心如何承托？与物体哪里接触？ | 站姿脚部重心、放松肩线、手部位置；坐姿臀/背承托、腿足落点、坐垫压陷 | 必须依据图中真实存在的家具 |
| 衣服质感好 | 哪件衣服？什么工艺？是否要锁定图案？ | 实际面料织法、缝线、领口结构、版型、垂坠、受力褶皱 | 未说明/参考未显示罗纹时不得加“罗纹竖线” |
| 高清 / 8K | 哪里要清楚？是否是局部修复？ | 眼部/服装商标/印花/接缝的焦点与微细节、边缘自然不锐化 | 文字“8K”不保证实际输出像素 |
| 活泼 / 亲和 | 通过哪些身体信号表现情绪？ | 视线目标、嘴角幅度、眉眼表情、手势、姿态节奏 | 不默认大笑、跳跃、夸张摆拍 |
| 高级商业摄影 | 哪项视觉证据产生品质感？ | 主次层级、克制道具、材质准确、受光一致、焦点明确 | “国际大牌感”无法替代具体目标 |
| 像抓拍 | 动作瞬间在哪里？ | 步态相位、受重脚、衣摆惯性、面部注意力、非对称轻微状态 | 不应引入违背重力的悬浮脚 |

## Conversion method

```text
原句片段
  -> 识别主观或含糊目标
  -> 列出物理/视觉上能观察到的 2-4 个证据
  -> 检查是否被已知参考图/用户要求授权
  -> 将其替换回原句中的相应位置
  -> 只针对典型失败追加 1-3 个反向约束
```

### Precision without invention

- 用户写“女模特漂亮”但已有图2面部：优先“沿用图2面部身份与五官结构”，**不要**擅自写成“鹅蛋脸、浅金低发髻”。
- 用户写“皮肤真实”但未给出人物年龄：写“保留符合人物年龄的自然肤质微差”，不要添加“眼角皱纹”。
- 用户写“自然坐在沙发上”而场景图确认只有沙发：可补“臀部由坐垫承托、背与靠背的接触合理”，不可新增床或转椅。
- 用户写“光影高级”且要求保留图1：用“继承图1光源方向、色温、阴影位置和环境反射”，不要新设灯位。
- 用户写“衣服纹理真实”而给了服装参考：描述“严格对应参考服装的织法、颜色、结构”，避免在看不到细节时编造成分。

## Article-derived dimensions

Source article groups realism as `皮肤、光影、姿态、服装、镜头`; its “漂亮→具体五官”“高清→焦点/镜头/细节”等转换属于写作示例，不能被解释为“所有模型必须写某个数字”。

### Contextual branches

- Close portrait: facial proportions/skin texture/eyes and hair are primary; don't force entire body pose detail.
- Apparel e-commerce: garment silhouette, seams, print, fit and subject physical support come first; skin texture is subordinate to product fidelity.
- Outdoor walking: foot contact, stride phase, clothing inertia, daylight direction are primary.
- Product-in-hand model: grip contact, object orientation, hand anatomy and attention hierarchy.
- Local face restoration: retain global image/light/pose; change only face feature fidelity and its local blending.
