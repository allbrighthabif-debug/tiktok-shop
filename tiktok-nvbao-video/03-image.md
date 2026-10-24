# 第 3 步:生图提示词

在 ChatGPT 生图,用户自己生成、自己检查;交完停。这张图就是视频的第一帧和配色基准,图不好看视频不可能好看,所以配色、光、质感、时刻四样都要到位。
- **只拍手和包**:出一张 9:16 场景图(第二节)。
- **真人出镜**:出一张同框图(第三节);布景要求高的条,再出一张场景图当 @图片3(第四节)。
- 建号时做一次人脸四视图和身材曲线图(第五节)。

## 一、先定配色和布景(内部定,交付写一句)
按 `palettes.md` 和 `styling.md`:
1. 用第 1 步定的色卡,把五个颜色分给画面里的东西:座椅、墙、车门这类大面积是"60";只拍手和包时包本身是"30",真人出镜时衣服是"30";袖子、指甲、杯子、围巾这些小物件是"10",点缀色放在两样小东西上做呼应。天空、窗外也写死颜色。
2. 深浅齐全:至少一样东西在最深那层、一样在最浅那层。
3. 冷暖七三或八二;饱和度只有点缀高,或者全部都低。
4. 包和紧挨着它的背景明暗拉开;包是画面里唯一的花纹;背景质感和包反着来(亮面包配哑光,软包配硬朗的底)。
5. 光:白天,阳光从侧前方照进来,柔和偏暖,在包和周围落出柔和的光斑;包的一侧略亮,另一侧有柔和的明暗;不逆光,不用斜阳、阴天(用户要才用)。阴天调子的色卡(比如晚秋林间铁路)照样写成晴天的光。
6. 生活感:包旁边 1-2 样随手扔的东西(搭着的开衫、对折的围巾、一串钥匙)加一杯饮料或一样点出时刻的东西;不放垃圾、杂物。
7. 首饰的金属颜色跟着包的五金走;包没有金属五金,手上不戴首饰。
8. 衣服(袖子、裤子、真人出镜的整身)按色卡配纯色,质感和包反着来,不出现别的花纹;有穿搭感,不是一身基础款陪衬(`styling.md` 第一节)。

## 二、场景图(只拍手和包)
- **第一句先定这是一张什么照片**:随手拍的 iPhone 照片、哪个季节的什么氛围、不是产品图。
- **包是随手放着的样子**:靠在座椅上、立在桌上、放在腿上,手正要去拿;不是悬在半空被两只手举着。
- **镜头退远一点**:看得出在哪里(车里看得到座椅、一角挡风玻璃和侧窗;床上看得到床头和窗);包在画面正中间,占画面宽度一半左右。
- **手**:从离镜头近的那一边伸进来(车里是画面左边);给镜头看小指那一侧;手指放松、微微错开;两三根手指勾着提带,另一只手轻扶或不入画;没有青筋,不按出指坑。肤色按号卡,指甲按这条定(`styling.md` 第三节)。
- **包照商品图**:Image 1 起上传商品图,写清"只照这只包,其余不照";花纹、颜色、提带、五金、口袋位置写进去;敞口或拉链拉开时,露出的东西按规格卡能装的、按她的身份,颜色和包拉开,不带 logo,不像赠品。
- **每个颜色写成"东西 + 材质 + 颜色名 + HEX"**,再写一句色卡取自的那个场景,让模型往那个氛围走。
- **构图有问题就整张重做**,不在失败的底图上用 Change only 改构图;Change only 只改小细节。

**模板**(英文,`[ ]` 按本条填)
```
A candid iPhone photo (vertical 9:16) [where: inside a parked car / on a bed / on a café table] on a [season and time: sunny autumn morning], taken from [camera position], [angle] — a casual phone shot, not a product photo. [Mood in a few words: cozy, lived-in fall mood, bright and airy.]
Image 1 is the product: reproduce this bag exactly — [bag type], [color and pattern, exact], [material and finish], [handle / strap], [hardware], [pockets and their positions]. Copy nothing else from the photo.
The bag: [how it rests: tossed casually on the passenger seat, slumped softly against the seat back], front facing the camera, in the center of the frame, about half of the frame width; [opening: the top zipper is open and the edge of a silver tablet peeks out].
Her hand: [which hand] reaches in from the [left], [what it does: fingertips just hooking under the handle as if about to grab it] — relaxed fingers with small gaps, pinky side toward the camera, no visible veins. [Skin: depth + undertone], [nails: length, shape, finish, color], [sleeve: color + material]. [No jewelry / one thin ring in the hardware's metal].
Around the bag: [60 surfaces: material + color name + HEX]; [1-2 tossed items: material + color]; [one item that marks the moment: an iced latte in the cup holder]; [what else is in frame].
Outside / background: [color-controlled background: golden-yellow autumn trees in the sun and a soft blue sky, slightly out of focus]; no signs, no text.
Light: bright [time] sunlight coming from [direction], warm, falling in soft light patches across [surfaces] and the bag so [the bag's color] glows; soft shadows, airy and bright, no blown highlights.
Colors: [palette name and its five colors] — the mood of [the palette's source scene]; [accent color] only on [two small items]. [Texture contrast: matte knit, smooth leather and the bag's fabric against each other.]
Style: real iPhone photo, natural, Pinterest-style [season] aesthetic, deep focus, true-to-life color, crisp [material] texture, natural skin texture.
Avoid: no studio product look, no bag floating in mid-air, no stiff posed hands, no grey overcast light, no other bags, no other patterns, no text or logos, [scene-specific: no steering wheel, no quilted seats], no extra fingers.
```

## 三、同框图(真人出镜)
一张竖图(3:4),她背着、挎着或拎着这只包的全身生活照,从下巴截到脚,不露脸;场景和配色就画在这张图里。上传身材曲线图当 Image 1、商品图从 Image 2 起;第 4 步当即梦的 @图片1。
- **包是画面里最显眼的东西,也是唯一的花纹**;衣服做配角、用色卡里的纯色,但要有穿搭感(第三件、质感对比、颜色呼应,`styling.md` 第一节)。
- **包怎么背按规格卡**(手拎、挎在手肘、单肩、腋下、斜挎),落点按"背上落在她身上哪里";包的正面朝镜头;装东西的包,上口露出一两样按身份装的东西。
- **身材按身材曲线图**,文字只补身高体重和角色卡里的身材词;肤色、发色按角色卡写;不画瘦;腿长、两只脚完整。
- **姿势**:站着准备出门,重心在一条腿上,身体微微侧过去让包正对镜头;一只手空着或轻扶包,不拿饮料。
- **布景**按 `scenes/` 里挑的场景文件和 `scenes/rules.md`:底子、物件 6-10 样成组放在画面一侧、生活痕迹 2-3 处加 1 处房子的旧,颜色全按色卡;不要太干净、不要像杂志。

**模板**(英文,`[ ]` 按本条填)
```
Use: one lifestyle reference photo for an AI video. A single vertical photo (3:4), cropped from the chin down to the feet, no face visible.
Images: Image 1: body reference — keep her body proportions, curves and leg length exactly as shown; her skin tone and hair come from the text. Image 2[–N]: product photo — reproduce the bag exactly: [color, pattern, material and finish, handles / strap, hardware, the product's own lettering if any], same size and shape; do not copy anything else from the photo.
Subject: [height], [weight]; [body words from the character card]; [skin: depth + undertone]; [hair color, the same from root to tip, and length]; [nails].
Outfit: [palette-based solid colors: top, bottom, outer layer, shoes, socks, belt — each with color + material + style]; [jewelry in the hardware's metal].
The bag: [how it is carried, which side], front side facing the camera; the bag is the most eye-catching and the only patterned thing in the frame; [what peeks out of the top]. [Her other hand: empty / lightly holding the edge of her coat.]
Pose: [standing at …, about to head out], weight on one leg, body turned slightly so the bag faces the camera; long legs, both feet fully in frame.
Scene: [place type]; [base: walls, floor, door — color + material]; [6-10 props grouped to one side, each with color]; [2-3 lived-in traces + 1 sign of age]; [what must NOT appear: other patterns, objects the same color as the bag, holiday decor if it clashes].
Light: soft [time] daylight from the front-[left / right], slightly warm, gentle soft shadows, her body and the bag evenly lit; bright, clean, true-to-life color.
Colors: [palette name and five colors] — the mood of [the palette's source scene].
Style: real iPhone photo, natural and lived-in, not editorial; [texture contrast]; realistic [material] reflections.
Avoid: no face, no text other than the bag's own lettering, no other logos, no [bent / wavy pattern lines], no extra bags, no drinks, no clutter, no harsh shadows, no color grading, no short legs, no cut-off feet.
```

## 四、场景图(真人出镜、布景要求高时)
只画场景、不画人,9:16,构图和光照同框图那个场景;颜色按色卡。写法用 `iphone17.md` 的生图写法,第一句先定"随手拍的照片";画面里不出现人、不出现包。第 4 步当 @图片3。

## 五、建号时做一次:人脸四视图 + 身材曲线图(真人出镜的号)
用户发"做参考图",或者第一次建号还没有这两张图时出。两张都在 ChatGPT 生成,不传图,全按角色卡写;都用浅灰纯色背景,图上不放任何字(字会被即梦画进视频)。
- **人脸四视图**(传即梦当 @图片2,管脸、发型、发色、妆容):田字格(2x2),正面、3/4、左侧脸、右侧脸,不要背面;只拍头和肩,每格一样大。
- **身材曲线图**(生同框图时传 ChatGPT 当 Image 1,管身材):横排四张竖格(正面、45 度、侧面、背面),不用田字格(会把全身压扁、腿变短);从下巴截到脚,不露脸、看不见嘴,四格比例一样、像同一个身体,脚完整;头发盘到头顶的画面外,图里不出现头发;穿贴身白背心 + 厚实不透的浅灰高腰紧身骑行短裤,赤脚。肤色一样的号可以共用一张;肤色不同,只改 Skin 那一句再出一张。
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
Style: photorealistic, natural skin texture, sharp focus on the face.
Avoid: any text, watermark, different hair or makeup between panels, a back view, cropped chin[, the hair color she should not have].
```

**身材曲线图模板**
```
Make a body reference sheet: four tall vertical panels in one row, wide landscape image (3:2), thin white gaps between panels: front view, 45° view, side view, back view.
Same crop in every panel: from just below the chin down to the feet — her mouth and lips are not visible — and both feet fully visible. Same scale in every panel. It is clearly the same body in all four panels.

Body: about [height], long legs (legs clearly longer than half her height), [身材词 from the character card]. Feminine, not muscular.
Waist: in the front view her waist curves in clearly between her bust and hips.
Glutes: [按角色卡写大小], high, round and lifted. In the side view they curve out clearly behind her; in the back view they are round and full in the shorts — natural-looking, not surgical.
Skin: [depth + undertone], even on the neck, arms and legs.
Hair: pulled up into a high bun on top of her head, above the crop and out of frame — no hair on her neck, shoulders or back in any panel.
Outfit: fitted white ribbed tank top; thick, opaque, smooth matte light-grey high-waisted compression bike shorts with a V-shaped back waistband, mid-thigh length, fully covering her glutes; barefoot.
Nails: short, plain nude nails.
Pose: relaxed and natural, both feet flat on the floor in every panel. Front view turned slightly to 3/4, weight on one leg. 45° and side views: chest up, a natural arch in her lower back. Back view: weight on one leg, the other knee slightly bent. Camera at hip height for the 45°, side and back views.
Background: plain very light grey (almost white). Soft light from the front-left plus a soft side light from behind, with gentle shadows that show her curves.
Style: photorealistic, natural skin texture, clean body-reference photo.
Avoid: showing the face or lips, any visible hair, tattoos, jewelry, visible muscle definition, muscular or broad shoulders, thick or bulky thighs, a boxy straight waist, exaggerated or surgical-looking glutes, a flat seat, short legs, standing on tiptoe, loose shorts, the camera looking down from above, cutting off the feet, different crops or body sizes between panels, dark background, any text, watermark.
```

**身材曲线图常见问题**(一次只改一处,用 `Change only: …`)
- 屁股不翘、显平:侧面和背面两格写塌腰、骨盆微微前倾、重心在一条腿上、相机在髋部高度;短裤要贴身的紧身面料,不要厚棉宽松的。
- 屁股太大、像做过手术:写 in proportion with her hips, natural-looking, not surgical。
- 肌肉块太多、像运动员:删掉 toned、muscle 这类词,写 feminine, not muscular, no visible muscle definition。
- 太瘦、没有肉感:写 soft and full-figured at the bust, hips, glutes and thighs, not skinny。
- 四格不像同一个身体(胸或屁股一格大一格小):`Change only: make it clearly the same body in all four panels — …`,写清哪一格照哪一格。
- 踮脚:写 both feet flat on the floor in every panel。
- 露出嘴:写 her mouth and lips are not visible。

## 六、包特有的画错风险(提示词里写进 Avoid 或单独一句)
- 满格花纹、格纹:写 "the [pattern] stays exactly as in Image 1, same spot size and spacing, no bent or blurred lines"。
- 包上的字样:只保留商品自己的字样,写清"no other text";字多的包,构图别让字成为焦点。
- 透明涂层:写 "a natural, subtle sheen",不然会画成塑料袋。
- 提带、肩带:写清从哪里连到哪里、挂在哪个肩或手肘;"the strap does not pass through her body or hand"。
- 五金:写清颜色和形状,"hardware keeps its shape"。
- 包里露出的东西:一两样,颜色和包拉开,不带 logo。

## 七、交付格式
```
当前:第 3 步 [场景图 / 同框图]|下一步:等你生完图、检查后发回来(或发 1 继续)
配色:色卡 …|六成 …|三成 …|一成 …(点缀放在 … 和 …)|光 …|手:指甲 …、袖子 …、首饰 …
上传:Image 1 [商品图 / 身材曲线图] / Image 2… [商品图]
(英文提示词,放在代码块里)
没出好时发一句:(按本条写 2-3 句 Change only 改细节的句子,比如花纹不对、包没在中间)
你检查时看:1. …… 2. …… 3. ……
```
- 检查项按本条写三条,只看用户自己能看出来的:包和商品图是不是一样(颜色、花纹、形状、提带、五金);手指数对不对、看起来放松、指甲和首饰对不对;包在画面中间、整张图配色舒服、除了包没有别的花纹、没有字和 logo。真人出镜再加:不露脸、身材和身材曲线图一样、腿不短、脚完整。
- 用户说哪里不对:构图、姿势、光的大问题整张重做;小细节给一句 `Change only: …… Keep everything else exactly the same: …` 一次只改一处。
- 用户说"太素""没感觉":先查配色(深浅齐不齐、有没有辅色和点缀、冷暖比例)、再查光(有没有方向和光斑)、再查质感叠加和生活感,哪条没到位改哪条,整张重做。
