# 第 3 步:参考图(默认平铺搭配图)

默认出一张**平铺搭配图**的提示词:商品正面加整套搭配,平铺在浅灰底上,图里没有人;用户在 ChatGPT 生成、自己检查;交完停。第 4 步当即梦的 @图片1,身材靠身材曲线图(即梦 @图片3)和号卡的即梦身材句。
- **跳过这一步**:商家已经有搭配平铺图(商品加鞋包配饰),直接用;用户说"不用搭配图",直接进第 4 步,搭配在即梦【衣服】里写一两句。
- **背面**:平铺图不放背面。视频要转到背面、或背面是卖点时,用商家的背面照(只有衣服、没有模特的直接传;有模特的先裁到只剩衣服)。
- **改用同框图**(第二节起的写法:一张竖图里左边正面、右边背面,同一个人穿着,从下巴往下截,不露脸):结构复杂的款(裹身、系带、不对称、斜肩),或者用平铺图上身出错(长度、版型不对)时。

## 一、先定搭配(内部定,交付写一句)
按 `styling.md`:
- 按 `styling.md` 第一节定:风格、商品是唯一信号、第三件、签名线索、不经意、比例、质感、颜色回声;点缀色先从商品自己的颜色里挑,放的位置轮换,红色不当默认(`styling.md` 第二节);搭配单品的颜色从第 1 步定的色卡里取,衣服是 30、鞋包配饰指甲是 10,离商品最近的大块颜色不比商品更亮更艳(`colors.md` 第二、五节);不用商品图里模特穿的下装、鞋、包;季节和第 2 步的场景对得上。
- 挡卖点的配饰换位置,不删(`styling.md` 第七节);衣服最多三层,叠穿按 `styling.md` 第一节,商品的卖点不被别的层挡住。
- **普通测试**(内部):把商品遮住,剩下的搭配像卖家主图,或像"白 T 配牛仔""牛仔裤配短靴"这种默认组合,就重配;像一件商品配一身基础款,也重配。
- **画进图的**:下装、鞋、袜、腰带、首饰、不挡卖点的包;平铺图还可以把耳饰、墨镜、帽子摆进去。
- **不画进图的**:手里拿的东西(跟场景走)、发饰、唇色;同框图不露脸,头上的一切都不画;这些第 4 步用文字加;落在头上的颜色回声和签名线索这里就定好,写进搭配那句。

## 一之二、平铺搭配图提示词(默认)
- 上传商品正面图当 Image 1(只取衣服,商品图里模特身上别的单品不取)。商品的结构写到部件,有方向的写穿着者的左右(正面朝上平铺时,她的左边在画面右边)。
- 搭配按第一节定,每样写颜色 + 材质 + 款式;按穿在身上的上下位置摆,略微重叠,不压住商品。
- 细条纹、格子、密印花写"每条、每格都平直整齐"。
- 生完先对商品的结构细节(门襟方向、领型、口袋、下摆),对上了再进第 4 步。

**模板**(英文,`[ ]` 按本条填)
```
Flat lay product photo, top-down view, on a plain light grey background, vertical 3:4. The full outfit laid out as it would be worn, items slightly overlapping naturally, nothing covering the product:
- [the product, front side up, exactly as in Image 1: color, fabric, every structural detail, direction on the wearer's left / right]
- [bottom / third piece: color + material + style]
- [shoes][, socks][, belt]
- [bag, jewelry, sunglasses, hat — as in the styling line]
Soft even light, true-to-life color, sharp fabric texture[, every stripe / check straight and even]. No person, no hands, no hangers, no text, no labels, no logos, no other items.
```

## 二、同框图提示词要点(备用)
- 衣服严格照商品图,只取衣服,不取模特和她身上别的东西;结构写到部件,有方向的写清哪一侧(正面里她的左边在画面右边,背面里在画面左边)。
- 长度按尺码表落在她身上的位置(`fit-body.md` 第四节),和模特图冲突时以尺码表为准。
- **身材按身材曲线图**:上传当 Image 1,商品图从 Image 2 开始。文字只当补充:身高、体重的数字留着;身材词从角色卡照抄(每个号自己的一句);不写"粗壮的大腿""力量型",会画墩;三围数字不写(生图模型不认,选码照样用三围),罩杯只在内衣、泳装时写;不画瘦。
- **肤色和头发按角色卡写**,不从 Image 1 取:肤色写深浅 + 冷暖调(如 `light skin with a warm golden undertone`、`deep brown skin with a cool undertone`),深肤色加 `not lightened, not ashy`;背面看得见的头发,写发色和长度,发色写"从发根到发尾同一个颜色"(角色本来就有深发根的照写)。
- **衣服被身材撑起来**,款式和版型不改;按品类挑一句写进模板的 Fit:
  - 上衣 + 下装:上衣顺着胸垂下或贴身,前面塞进高腰下装,露出腰线;下装在腰、胯、臀贴身,大腿往下才按它自己的版型放开;背面臀部把下装撑满。
  - 连衣裙、A 字裙、伞裙:腰贴合,往下按它自己的版型散开。
  - 外套:里面那身贴身,看得出胸型和腰线;下装贴臀,外套短于臀时背面看得出臀型;外套按自己的版型敞开或系上。
  - 内衣、泳装、塑身:只写合身、贴合,不写"臀部撑满"(不性感化)。
- **腿长按角色卡、脚完整**:正面微微侧一点,重心放在一条腿上;腿的长短按角色卡(不把长腿画短,也不把小个子画成长腿),两只脚完整在画面里。
- 细条纹、密印花写"每条都笔直、不弯不乱"。

**模板**(英文,`[ ]` 按本条填)
```
Use: one product reference image for an AI video. A single vertical image (3:4) showing the same woman twice, side by side: on the left a front view, on the right a back view. Both full length from the chin down to the feet; the head is cropped at the chin, no face visible. Plain very light grey background, almost white; the two figures not overlapping; both feet fully visible.
Images: Image 1: body reference — keep her body proportions, curves and leg length exactly as shown. Her skin tone and hair come from the text, not from Image 1.
Image 2–[N] (商品图建议 2–4 张): product photos — reproduce the garment exactly as shown ([key details]); do not copy the model or anything else she wears.
Subject: [height], [weight][, bra size — lingerie / swimwear only]; [身材词 from the character card]; [legs: 角色卡 168 cm 以上写 long legs;小个子写 petite proportions,不写 long legs]; her body exactly as in Image 1 — not slimmed, not retouched; [skin tone: depth + undertone], even and consistent on the neck, arms and legs; hair seen from the back: [color, the same from root to tip, and length]; [nails]; [tattoo, if any, with placement].
Outfit: [garment: color, fabric, fit, neckline front and back, sleeves, hem landing point, every structural detail, direction on the wearer's left / right].
Styled with: an intentional [the style in English, from trends-fw2026.md] look — [third piece: jacket / vest / cardigan / scarf / belt, how it is worn], [bottom: color + material + style + how it is worn], [the small undone detail: sleeve cuff rolled / front tuck], [socks], [shoes], [bag, which side, only if it does not cover the selling point], [jewelry on the body]. Nothing else: [what must NOT appear].
Fit: [按品类挑一句。上衣 + 下装:her curvy body fills out the clothes. The top [hugs / drapes over] her bust and is [front-tucked / tucked] into the high-waisted bottoms to show her narrow waist. The bottoms fit snugly through her waist, hips and seat, then fall into their own cut below the thighs. In the back view, her glutes clearly fill out the seat. Keep each garment's original design and cut.]
Pose: front view turned slightly to one side, weight on one leg, relaxed, [one arm slightly away so the side is visible]; both feet fully in frame. Back view: the same woman facing away, same framing and lighting; [back detail] clearly visible.
Details: the front and back views show the SAME garment and must match exactly — [color, print, neckline, sleeve length, hem length].
Style: clean e-commerce reference, soft light from the front-left with gentle shadows that show her curves, true-to-life color, realistic fabric texture and natural folds, visible skin texture, no color grading.
Avoid: no face, no text, no watermark, no logos other than the product's own, no extra accessories, no body slimming, no plastic skin, no differences between the front and back views, no change to her body shape, [no short legs — 角色卡 168 cm 以上才写], no cut-off feet[, no bent or wavy stripes].
```

## 三、交付格式
平铺搭配图(默认):
```
当前:第 3 步 参考图|下一步:等你生完图、检查后发回来(或发 1 继续)
搭配:风格 ……|……(一句:第三件、下装、鞋袜、包、首饰)
上传:Image 1 商品正面图
(英文提示词,放在代码块里)
你检查时看:1. 商品的结构细节和商品图一样 2. 搭配的单品都在、没多东西 3. ……
```
同框图(备用):
```
当前:第 3 步 参考图|下一步:等你生完图、检查后发回来(或发 1 继续)
搭配:风格 ……|……(一句:第三件、下装、鞋袜、包、首饰、签名线索;头上的标"第 4 步加")
上传:Image 1 身材曲线图 / Image 2… 商品图
(英文提示词,放在代码块里)
没出好时发一句:露脸 → "Crop at the chin, no face visible, keep everything else the same." / 拼成两张或只有一面 → "Put both views in ONE image: front on the left, back on the right." / [按本条衣服再写一句,比如长度或印花]
你检查时看:1. …… 2. …… 3. ……(衣服对不对、正反面是同一件、不露脸、没画瘦;身材和身材曲线图一样、衣服被撑起来、腿不短、脚完整;不用对肤色)
```
- 用户说哪里不对:给一句改图提示词 `Change only: …… Keep everything else the same: the garment exactly as in the product photos, her body and skin tone, pose, framing, lighting, light grey background.` 一次只改一处。
- 身材没出来时发:`Change only: make her body match Image 1 — [only what differs from Image 1 and the character card: waist, bust, hips or leg length], the clothes filling out over her body. Keep everything else the same.`

## 四、建号时做一次:人脸四视图 + 身材曲线图
用户发"做参考图",或者第一次建号还没有这两张图时出。两张都在 ChatGPT 生成,不传图,全按角色卡写;都用浅灰纯色背景,图上不放任何字(字会被即梦画进视频)。
- **人脸四视图**(传即梦当 @图片2,管脸、发型、发色、妆容):田字格(2x2),正面、3/4、左侧脸、右侧脸,不要背面;只拍头和肩,每格一样大。
- **身材曲线图**(管身材:用平铺图时传即梦当 @图片3,用同框图时传 ChatGPT 当 Image 1):横排四张竖格(正面、45 度、侧面、背面),不用田字格(会把全身压扁、腿变短);从下巴截到脚,不露脸、看不见嘴,四格比例一样、像同一个身体,脚完整;头发盘到头顶的画面外,图里不出现头发;穿贴身白背心 + 厚实不透的浅灰高腰紧身骑行短裤,赤脚。肤色一样的号可以共用一张;肤色不同,只改 Skin 那一句再出一张。
- 发色写清"从发根到发尾同一个颜色"(角色本来就有深发根的除外),不然容易被画成挑染。
- 想要的颜色和参考图不一样时(比如有张喜欢的图是深发,要做金发),写"脸和妆容照参考图,只换发色",不写"头发跟参考图一样",不然两边打架。
- 用户发来真人照片当参考:只借发色、发量、妆感和气质,脸用文字另写,不把照片传上去照着做(肖像权,也会被当成冒充)。
- 出图后哪一处不对,只改那一处(`Change only: …`),整张重出容易跑掉。

**人脸四视图模板**
```
Make a face reference sheet: a square image split into a 2x2 grid with thin white lines, four equal panels of the same woman, same size and framing in every panel, head and shoulders only:
top-left front view, top-right 3/4 view, bottom-left left profile, bottom-right right profile. No back view.

Her: [age]-year-old woman, [skin: depth + undertone], [eye color], [brows], [face shape and features].
Hair: [length, texture, part], [color], the same color from root to tip[ / naturally darker roots — the same color placement in every panel].
Makeup: [照角色卡].
Expression: [照角色卡]. In the front and 3/4 views she looks into the camera.
Wearing: a white ribbed tank top (only the straps and neckline visible)[, her signature earrings].
Background: plain light grey in every panel. Soft, even, flattering light.
Style: photorealistic, natural skin texture with visible pores and fine peach fuzz, no smoothing, no beauty retouching, not oily, sharp focus on the face.
Avoid: any text, watermark, different hair or makeup between panels, a back view, cropped chin[, the hair color she should not have].
```

**身材曲线图模板**
```
Make a body reference sheet: four tall vertical panels in one row, wide landscape image (3:2), thin white gaps between panels: front view, 45° view, side view, back view.
Same crop in every panel: from just below the chin down to the feet — her mouth and lips are not visible — and both feet fully visible. Same scale in every panel. It is clearly the same body in all four panels.

Body: about [height], [legs: 角色卡 168 cm 以上写 long legs (legs clearly longer than half her height);小个子写 petite proportions], [身材词 from the character card]. Feminine, not muscular.
Waist: in the front view her waist curves in clearly between her bust and hips.
Glutes: [按角色卡写大小], high, round and lifted. In the side view they curve out clearly behind her; in the back view they are round and full in the shorts — natural-looking, not surgical.
Skin: [depth + undertone], even on the neck, arms and legs.
Hair: pulled up into a high bun on top of her head, above the crop and out of frame — no hair on her neck, shoulders or back in any panel.
Outfit: fitted white ribbed tank top; thick, opaque, smooth matte light-grey high-waisted compression bike shorts with a V-shaped back waistband, mid-thigh length, fully covering her glutes; barefoot.
Nails: short, plain nude nails.
Pose: relaxed and natural, both feet flat on the floor in every panel. Front view turned slightly to 3/4, weight on one leg. 45° and side views: chest up, a natural arch in her lower back. Back view: weight on one leg, the other knee slightly bent. Camera at hip height for the 45°, side and back views.
Background: plain very light grey (almost white). Soft light from the front-left plus a soft side light from behind, with gentle shadows that show her curves.
Style: photorealistic, natural skin texture, clean body-reference photo.
Avoid: showing the face or lips, any visible hair, tattoos, jewelry, visible muscle definition, muscular or broad shoulders, thick or bulky thighs, a boxy straight waist, exaggerated or surgical-looking glutes, a flat seat, [short legs — 角色卡 168 cm 以上才写], standing on tiptoe, loose shorts, the camera looking down from above, cutting off the feet, different crops or body sizes between panels, dark background, any text, watermark.
```

**身材曲线图常见问题**(一次只改一处,用 `Change only: …`)
- 屁股不翘、显平:侧面和背面两格写塌腰、骨盆微微前倾、重心在一条腿上、相机在髋部高度;短裤要贴身的紧身面料,不要厚棉宽松的。
- 屁股太大、像做过手术:写 in proportion with her hips, natural-looking, not surgical。
- 肌肉块太多、像运动员:删掉 toned、muscle 这类词,写 feminine, not muscular, no visible muscle definition。
- 太瘦、没有肉感:写 soft and full-figured at the bust, hips, glutes and thighs, not skinny。
- 四格不像同一个身体(胸或屁股一格大一格小):`Change only: make it clearly the same body in all four panels — …`,写清哪一格照哪一格。
- 踮脚:写 both feet flat on the floor in every panel。
- 露出嘴:写 her mouth and lips are not visible。
