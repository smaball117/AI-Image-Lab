# Worked briefs: desired output form

These are fabricated training briefs, not outputs proven by image generation. Replace role assignment and garments with the user's actual references.

## Example A: children’s apparel on an existing sofa

**User brief:** Image 1 is the living room and existing sofa. Image 2 controls a 12-year-old boy's face. Image 3 controls the exact cotton loungewear. Seat the boy naturally on the sofa, show front garment, 3:4, preserve image 1 light; one single finished image.

**Role map:** image 1 = scene + actual furniture + camera/light anchor; image 2 = face only; image 3 = garment identity only.

**Prompt:** 以图1为唯一客厅场景和现有沙发的依据，保持其空间陈设、原有光线方向、色温和背景；以图2为男孩面部身份参考，仅继承五官和发型，不继承图2的衣服与背景；图3是唯一服装依据，准确保留纯棉面料、颜色、领口、袖口和印花。生成一张真实童装商业摄影，约12岁男孩自然坐于图1沙发坐垫上，臀部有稳定承托，背部自然挺直并轻靠靠背，双腿放松且落点合理，肩膀下沉，一只手自然放在腿上，另一只手轻搭沙发，衣服正面完整可见，裤腿与坐垫接触形成真实的受力褶皱。镜头略高于坐姿视线，膝盖以上中景，主体占据足够画面，皮肤保持符合年龄的自然微观纹理，不做成人化精修；原场景主光、暗部和接触阴影连续一致。单张3:4竖幅，不添加新家具或人物，不改变图3服装结构，不生成九宫格。

**Preflight:** sofa support, correct outfit, no extra furniture, reference isolation.

## Example B: face-only restoration

**User brief:** Keep image 1 model composition, expression, outfit, and lighting. Use image 2 for face features. No collage.

**Role map:** image 1 = immutable scene/body/pose/lighting/crop; image 2 = face identity reference only.

**Prompt:** 对图1人物进行局部面部高清修复，仅按图2还原面部骨相、眼鼻唇比例和识别特征，完整保留图1原有头部朝向、表情、眼神方向、发型、身体姿态、服装、背景、构图、色温、光线方向、高光及阴影分布。面部皮肤纹理真实自然，与图1光线和环境反射相符，不出现贴脸边界、磨皮或肤色断层。输出一张与图1原比例一致的单幅照片，不继承图2背景或九宫格排版。

**Preflight:** only face identity may change, lighting preserved, no grid.

## Example C: no images, adult beauty model concept

**User brief:** A minimal beauty campaign, close portrait, model with realistic skin; no specific reference.

**Prompt:** 极简商业美妆人像摄影，一位成年东亚女性，深棕色自然眼睛，黑色中长发梳理整洁，表情平静自信，妆容克制，唇部与眼周肌理真实。采用正面头肩特写、平视机位，面部比例自然，双眼和唇部清晰，背景柔和虚化，发顶保留完整空间。画面左前上方的大面积柔光形成面部清晰而柔和的受光方向，颧骨和鼻梁出现克制高光，另一侧面颊有自然的渐变阴影；皮肤保留细微毛孔与自然色差，发丝分明，无蜡像感。背景极简，画面无品牌、无多余人物。根据成图效果检查面部光影一致性与皮肤纹理是否自然。

**Preflight:** no fabricated image roles; no promise of export resolution.

## Example D: single-variable pose fix

**User brief:** Generated model and garment look right but boy appears to float beside sofa.

**Output:** 保留上一版男孩的身份、面容、发型、衣服、印花、构图、镜头及环境光完全不变。仅修正坐姿：臀部完整落在已有沙发坐垫上，腿部与坐垫、地面的接触符合重力，靠背提供真实支撑，坐垫出现轻微压陷，接触处产生与原场景主光一致的柔和阴影。不要新增家具，不修改服装纹样和场景。
