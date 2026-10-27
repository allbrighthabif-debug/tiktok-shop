# 第 3 步:生图提示词

卖鞋时先读 `shoes.md`,和这里冲突以它为准。

在 ChatGPT 生图,用户自己生成、自己检查;交完停。
- **两条路都先定白底锚点图**(第三节):商家有干净的正面图直接用,没有就出白底重绘提示词。
- **只拍手和包**:再出一张 9:16 场景图(第二节)。这张图就是视频的第一帧和配色基准,图不好看视频不可能好看,所以配色、光、质感、时刻四样都要到位。
- **真人出镜**:只要锚点图,不出别的图;身材、衣服、背法、场景、配色第 4 步全写成文字(第一节照样内部定好)。
- 建号时做一次人脸四视图(第四节)。

## 一、先定配色和布景(内部定,交付写一句)
按 `palettes.md` 和 `styling.md`:
1. 用第 1 步定的色卡,把五个颜色分给画面里的东西:座椅、墙、车门这类大面积是"60";只拍手和包时包本身是"30",真人出镜时衣服是"30";袖子、指甲、杯子、围巾这些小物件是"10",点缀色放在两样小东西上做呼应。天空、窗外也写死颜色。
2. 深浅齐全:至少一样东西在最深那层、一样在最浅那层。
3. 冷暖七三或八二;饱和度只有点缀高,或者全部都低。
4. 包和紧挨着它的背景明暗拉开;包是画面里唯一的花纹;背景质感和包反着来(亮面包配哑光,软包配硬朗的底)。
5. 光:白天,阳光从侧前方照进来,柔和偏暖,在包和周围落出柔和的光斑;包的一侧略亮,另一侧有柔和的明暗;不逆光,不用斜阳、阴天(用户要才用)。阴天调子的色卡(比如晚秋林间铁路)照样写成晴天的光。
6. 生活感:包旁边 1-2 样随手扔的东西(搭着的开衫、对折的围巾、一串钥匙)加一样点出时刻的东西(饮料只在场景本来该有时放);不放垃圾、杂物。
7. 首饰的金属颜色跟着包的五金走;包没有金属五金,手上不戴首饰。
8. 衣服(袖子、裤子、真人出镜的整身)按色卡配纯色,质感和包反着来,不出现别的花纹;有穿搭感,不是一身基础款陪衬(`styling.md` 第一节)。

## 二、场景图(只拍手和包)
- **第一句先定这是一张什么照片**:随手拍的 iPhone 照片、第一视角还是别人拍、哪个季节的什么氛围、不是产品图。
- **包两种样子,二选一**:
  - 拎着(爆款常用,实测有效):手臂从画面左上角伸进来,手拎着提带,包垂直挂着、包底悬在座垫或桌面上方一点点;不是手臂横着从半空伸过来、把包举得很高。
  - 放着:靠在座椅上、立在桌上、放在腿上,手指刚勾住提带;写成"包底贴着座位"。
- **机位和空间写死**(车里,实测有效):她坐在驾驶座,镜头在肩膀高度,斜着看向副驾车门;包的身后是副驾车门和车窗,座椅靠背在画面右边,座垫在画面底部。**前景什么都不放**(方向盘、仪表台、中控、杯子都不入画);画面只要三层:包、身后的车门和座椅、更远的车窗。车窗在包的后上方,外面亮,车里整体明亮、没有死黑的角落。
- **离包最近的大色块不能是全画面最亮的**:袖子、开衫这类紧挨着包的大面积,用色卡里中深的颜色;最亮的应该是包上的高光和窗外一小块天。
- **道具最多两样**(一样点出时刻、一样随手扔的),不放带流苏、带明显纹理或花纹的东西;包后面要么是座椅,要么是素净的窗外,不是满窗的彩色树。
- **镜头退远一点**:看得出在哪里(车里看得到座椅、一角挡风玻璃和侧窗;床上看得到床头和窗);包在画面正中间,占画面宽度六成左右。
- **手**:从离镜头近的那一边伸进来(车里是画面左边);给镜头看小指那一侧;手指放松、微微错开;两三根手指勾着提带,另一只手轻扶或不入画;没有青筋,不按出指坑。肤色按号卡,指甲按这条定(`styling.md` 第三节)。
- **包照锚点图**:Image 1 上传第三节的正面锚点图(有副锚点可以当 Image 2),写清"只照这只包,其余不照";花纹、颜色、提带、五金、口袋位置写进去;敞口或拉链拉开时,露出的东西按规格卡能装的、按她的身份,颜色和包拉开,不带 logo,不像赠品。
- **每个颜色写成"东西 + 材质 + 颜色名 + HEX"**,再写一句色卡取自的那个场景,让模型往那个氛围走。
- **光写清从哪来,和窗户对得上**(窗在右边,就照亮包的右侧);不堆"glow、airy、golden、bright"这类词,堆了会过曝、发金、颜色被冲淡;写"rich, true-to-life color, gentle contrast, not golden, not overexposed"。
- **构图有问题就整张重做**,不在失败的底图上用 Change only 改构图;Change only 只改小细节。

**模板**(英文,`[ ]` 按本条填)
```
A candid iPhone photo (vertical 9:16) [where: inside a parked car / on a bed / on a café table] on a [season and time: sunny autumn morning], taken from [camera position], [angle] — a casual phone shot, not a product photo. [Mood in a few words: cozy, lived-in fall mood, bright and airy.]
Image 1 is the product: reproduce this bag exactly — [bag type], [color and pattern, exact], [material and finish], [handle / strap], [hardware], [pockets and their positions]. Copy nothing else from the photo.
The bag: [how it rests: tossed casually on the passenger seat, slumped softly against the seat back], front facing the camera, in the center of the frame, about half of the frame width; [opening: the top zipper is open and the edge of a silver tablet peeks out].
Her hand: [which hand] reaches in from the [left], [what it does: fingertips just hooking under the handle as if about to grab it] — relaxed fingers with small gaps, pinky side toward the camera, no visible veins. [Skin: depth + undertone], [nails: length, shape, finish, color], [sleeve: color + material]. [No jewelry / one thin ring in the hardware's metal].
Around the bag: [60 surfaces: material + color name + HEX]; [1-2 tossed items: material + color]; [one item that marks the moment]; [what else is in frame].
Outside / background: [color-controlled background: golden-yellow autumn trees in the sun and a soft blue sky, slightly out of focus]; no signs, no text.
Light: soft natural [time] daylight coming through [the window on which side], slightly warm, lighting [that side] of the bag, gentle natural shading on the other side; rich, true-to-life color with gentle contrast; not golden, not overexposed.
Colors: [palette name and its five colors] — the mood of [the palette's source scene]; [accent color] only on [two small items]. [Texture contrast: matte knit, smooth leather and the bag's fabric against each other.]
Style: real iPhone photo, natural, Pinterest-style [season] aesthetic, deep focus, true-to-life color, crisp [material] texture, natural skin texture.
Avoid: no studio product look, no bag held up in the air, no stiff posed hands, no bright sleeve next to the bag, no fringe, no busy background behind the bag, no grey overcast light, no golden haze, no other bags, no other patterns, no text or logos, [scene-specific: no steering wheel, no quilted seats, no arm coming from the right side], no extra fingers.
```

## 三、白底锚点图(两条路都要)
包的样子全靠这张图锁住;第 4 步当包的参考上传。不做人和包的同框图(包容易穿模)。
- **正面锚点(必须)**:商家图里有一张正面、包完整、没有人、没有手、背景干净、看得清花纹和五金的,直接用,本步不出提示词,交付写一句"用商品图第 N 张当锚点"。
- **没有这样的图**(都带模特、背景乱、只有侧面):出一条白底重绘提示词,上传商品图里包最清楚的 2-3 张,只把这只包重画在纯白底上,花纹、五金、提带、口袋一样不改。用户生完拿去和原图逐项对:颜色、花纹的大小和间距、五金的个数和位置、提带连在哪、口袋在哪、商品自己的字样;哪一处不对只改那一处。
- **副锚点(可选)**:要演包里、背面或包底时,再出一张背面或打开的白底图;商家有干净的就直接用。

**模板**(英文,`[ ]` 按本条填)
```
Redraw only the bag from the uploaded photos as a clean e-commerce product photo on a pure white background (#FFFFFF), vertical 4:5. [Front view / back view / top open view], the bag standing upright, centered, about 70% of the frame height; [handles standing up / strap tucked neatly behind the bag].
Keep the bag exactly as in the photos: [bag type and shape], [color and pattern, exact — same spot size and spacing], [material and finish], [handles / strap: where they attach, how long], [hardware: color, shape, how many, where], [pockets, zipper, stitching], [the product's own lettering, unchanged]. Same proportions; do not redesign, simplify or add anything.
Nothing else in the image: no model, no hands, no props, none of the original background.
Light: soft, even light, a faint natural shadow under the bag, true-to-life color.
Avoid: changed or blurred pattern, extra or missing hardware, extra pockets, a different strap, warped shape, any extra text or logos.
```

## 四、建号时做一次:人脸四视图(真人出镜的号)
用户发"做参考图",或者第一次建号还没有这张图时出。在 ChatGPT 生成,不传图,全按角色卡写;浅灰纯色背景,图上不放任何字(字会被即梦画进视频)。身材不出图,第 4 步用文字写身高体重和一句身形词。
- **人脸四视图**(传即梦当 @图片2,管脸、发型、发色、妆容):田字格(2x2),正面、3/4、左侧脸、右侧脸,不要背面;只拍头和肩,每格一样大。
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

## 五、包特有的画错风险(提示词里写进 Avoid 或单独一句)
- 满格花纹、格纹:写 "the [pattern] stays exactly as in Image 1, same spot size and spacing, no bent or blurred lines"。
- 包上的字样:只保留商品自己的字样,写清"no other text";字多的包,构图别让字成为焦点。
- 透明涂层:写 "a natural, subtle sheen",不然会画成塑料袋。
- 提带、肩带:写清从哪里连到哪里、挂在哪个肩或手肘;"the strap does not pass through her body or hand"。
- 五金:写清颜色和形状,"hardware keeps its shape"。
- 包里露出的东西:一两样,颜色和包拉开,不带 logo。

## 六、交付格式
```
当前:第 3 步 [锚点图 + 场景图 / 锚点图]|下一步:等你生完图、检查后发回来(或发 1 继续)
配色:色卡 …|六成 …|三成 …|一成 …(点缀放在 … 和 …)|光 …|手:指甲 …、袖子 …、首饰 …
锚点:用商品图第 N 张 / 白底重绘(提示词在下面)
上传:Image 1 [锚点图 / 商品图 2-3 张] / Image 2 …
(英文提示词,放在代码块里)
没出好时发一句:(按本条写 2-3 句 Change only 改细节的句子,比如花纹不对、包没在中间)
你检查时看:1. …… 2. …… 3. ……
```
- 检查项按本条写三条,只看用户自己能看出来的:包和商品图是不是一样(颜色、花纹、形状、提带、五金);手指数对不对、看起来放松、指甲和首饰对不对;包在画面中间、整张图配色舒服、除了包没有别的花纹、没有字和 logo。白底重绘图另看:和原图逐项对(颜色、花纹大小和间距、五金个数和位置、提带连在哪、口袋、字样)。
- 用户说哪里不对:构图、姿势、光的大问题整张重做;小细节给一句 `Change only: …… Keep everything else exactly the same: …` 一次只改一处。
- 用户说"太素""没感觉":先查配色(深浅齐不齐、有没有辅色和点缀、冷暖比例)、再查光(有没有方向和光斑)、再查质感叠加和生活感,哪条没到位改哪条,整张重做。
