# 第 3 步:生图提示词

卖鞋时先读 `shoes.md`,和这里冲突以它为准。

**这一步按需,默认跳过**(让用户少做图):锚点图在第 1 步从商家图里挑,场景写成文字,文案定了直接进第 4 步。只有下面几种情况才出图,在 ChatGPT 生成,用户自己检查;交完停。
- **白底重绘锚点图**(第三节):商家图全是模特图、背景乱到看不清包,挑不出一张能用的;或者生成过一次包画错了(比如亮面被画成塑料)。重绘时光线均匀、没有大块反光。
- **只拍手和包的场景图**(第二节):机位要求很死(车里副驾)或者文字生成出来不满意时才出。出的话这张图就是视频的第一帧和配色基准,配色、光、质感、时刻四样都要到位。
- **建号时做一次**(第四节):人脸四视图,以后每条复用。
- **身材曲线图**:建号时做一次、每条复用,只在 ChatGPT 出无头上身图时传,不传进即梦。
- **真人出镜每条做一张无头上身图**(第四节之二):正反两面、白底、穿着这条的衣服、不背包,锁住身材和衣服。
- 真人出镜不出场景图、同框图;身材、衣服、背法、场景、配色第 4 步全写成文字(第一节照样内部定好)。

## 一、先定配色和布景(内部定,交付写一句)
按 `palettes.md` 和 `style.md`:
1. 用第 1 步定的色卡,把五个颜色分给画面里的东西:座椅、墙、车门这类大面积是"60";只拍手和包时包本身是"30",真人出镜时衣服是"30";袖子、指甲、杯子、围巾这些小物件是"10",点缀色放在两样小东西上做呼应。天空、窗外也写死颜色。
2. 深浅齐全:至少一样东西在最深那层、一样在最浅那层。
3. 冷暖七三或八二;饱和度只有点缀高,或者全部都低。
4. 包和紧挨着它的背景明暗拉开;包是画面里唯一的花纹;背景质感和包反着来(亮面包配哑光,软包配硬朗的底)。
5. 光:白天,阳光从侧前方照进来,柔和偏暖,在包和周围落出柔和的光斑;包的一侧略亮,另一侧有柔和的明暗;不逆光;光按这张图要的现场来。阴天调子的色卡(比如晚秋林间铁路)照样写成晴天的光。
6. 生活感:包旁边 1-2 样随手扔的东西(搭着的开衫、对折的围巾、一串钥匙)加一样点出时刻的东西(饮料只在场景本来该有时放);不放垃圾、杂物。
7. 首饰的金属颜色跟着包的五金走;包没有金属五金,手上不戴首饰。有包饰时(`style.md` 第五节)只写一样:是什么、什么颜色(用点缀色)、挂在提手哪里,不挡包的正面和五金。
8. 衣服(袖子、裤子、真人出镜的整身)按色卡配纯色,质感和包反着来,不出现别的花纹;有穿搭感,不是一身基础款陪衬(`style.md` 第一节)。

## 二、场景图(只拍手和包)
- **第一句先定这是一张什么照片**:随手拍的 iPhone 照片、第一视角还是别人拍、哪个季节的什么氛围、不是产品图。
- **包两种样子,二选一**:
  - 拎着(爆款常用,实测有效):手臂从画面左上角伸进来,手拎着提带,包垂直挂着、包底悬在座垫或桌面上方一点点;不是手臂横着从半空伸过来、把包举得很高。
  - 放着:靠在座椅上、立在桌上、放在腿上,手指刚勾住提带;写成"包底贴着座位"。
- **机位和空间写死**(车里,实测有效):她坐在驾驶座,镜头在肩膀高度,斜着看向副驾车门;包的身后是副驾车门和车窗,座椅靠背在画面右边,座垫在画面底部。**前景什么都不放**(方向盘、仪表台、中控、杯子都不入画);画面只要三层:包、身后的车门和座椅、更远的车窗。车窗在包的后上方,外面亮,车里整体明亮、没有死黑的角落。
- **离包最近的大色块不能是全画面最亮的**:袖子、开衫这类紧挨着包的大面积,用色卡里中深的颜色;最亮的应该是包上的高光和窗外一小块天。
- **道具最多两样**(一样点出时刻、一样随手扔的),不放带流苏、带明显纹理或花纹的东西;包后面要么是座椅,要么是素净的窗外,不是满窗的彩色树。
- **镜头退远一点**:看得出在哪里(车里看得到座椅、一角挡风玻璃和侧窗;床上看得到床头和窗);包在画面正中间,占画面宽度六成左右。
- **手**:从离镜头近的那一边伸进来(车里是画面左边);给镜头看小指那一侧;手指放松、微微错开;两三根手指勾着提带,另一只手轻扶或不入画;没有青筋,不按出指坑。肤色按号卡,指甲按这条定(`style.md` 第三节)。
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
- **没有这样的图**(都带模特、背景乱、被手拿着):用下面的"提取整只包"通用提示词,直接复制进 ChatGPT,上传商品图里包最清楚的那一张,不用填空。
- **拍到了几面就提取几面**:商家图里拍到了侧面、背面、包里面、包底,就每一面各提取一张白底图,用同一条提示词,上传拍到那一面的图,第一句末尾加一句写清是哪一面(`This is the back view as shown in the photo.`);这几张就是副锚点,演到哪一面传哪一张。商家图里没拍到的面不提取、不演(提取不出来的那一面是 AI 编的,不能当参考)。
- **配件单独提取**:挂件、肩带、扣子、五金要单独锁住时,用"提取配件"那条,方括号里换成要提取的东西(`the beaded bag charm hanging on the left`)。
- **要拍的颜色没有图**:拿别的颜色那张最清楚的图提取,在提示词末尾加一句 `Change only the color of the bag to [颜色名] ([主色 HEX]); keep every detail, the material finish and the hardware color exactly the same.`;用户生完先核颜色(可以用 `tools/sample_color.py` 量一下跟商家写的颜色对不对)和细节,对了才当锚点。
- **出图后对一遍**:颜色、花纹的大小和间距、五金的个数和位置、提带连在哪、口袋在哪、商品自己的字样;哪一处不对只改那一处(`Change only: …`)。

**提取整只包**(直接复制,不用填空)
```
Extract only the bag from the uploaded photo and place it on a pure white background (#FFFFFF), as a clean e-commerce product photo, vertical 4:5, centered, about 70% of the frame height. Keep the bag exactly as it is in the photo: same shape, proportions, color, material and texture, hardware, straps, stitching and any lettering. Do not redesign, simplify, recolor or add anything. Remove everything else: the person, hands, props and background. Soft even light, a faint natural shadow under the bag, true-to-life color.
```

**提取配件**(只换方括号)
```
Extract only the [bag charm / shoulder strap / buckle] from the uploaded photo and place it alone on a pure white background (#FFFFFF), centered, filling about 60% of the frame. Keep it exactly as it is in the photo: same shape, colors, materials, number of parts and details. Do not redesign or add anything. Remove the bag, hands and background. Soft even light, true-to-life color.
```

## 四、建号时做一次:人脸四视图(真人出镜的号;身材曲线图可选)
用户发"做参考图",或者第一次建号还没有这张图时出。在 ChatGPT 生成,不传图,全按角色卡写;浅灰纯色背景,图上不放任何字(字会被即梦画进视频)。身材曲线图可选:默认不传即梦(图里的衣服会被当成她的衣服),身材用文字写;连着几条身材跑偏时再做、再传。身材不够好看时的备用办法:每条用 ChatGPT 出一张她穿着这条衣服的全身"穿搭图"(纯色背景、不拿包、写清身形),在即梦里传,写"只用于她的身材和这条的衣服",衣服和身材一起锁住。肤色一样的号可以共用一张;肤色不同,只改 Skin 那一句再出一张。
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

## 四之二、无头上身图(真人出镜每条做一张:正面和背面两格,穿着这条的衣服,不背包)
样子照商品上身图那种:整张竖图 3:4,白色背景,左边正面、右边背面,两格贴着、不留空隙不画分割线;每格人撑满,上面截在嘴唇下方,下面鞋底贴近底边,不露脸;相机在腰的高度平视,不俯拍、不广角,腿的比例才对;她穿着这条视频的整套衣服,双手自然垂在身侧,不拿包;光均匀、柔和,像电商上身图。
**先给搜索词**:出这张图之前,按这条的包、颜色、风格、季节给 3-5 个英文搜索词,写清去哪搜(Pinterest、品牌官网、购物网站),比如 `chocolate brown cardigan olive wide leg pants outfit`、`cropped knit cardigan set women winter`;用户找到服装图发来,先一两句话说出看到的这身让她确认。
用 ChatGPT 出,传两类图:Image 1 身材曲线图(只用身材);Image 2 起是服装原图(只用衣服;有正面整体和细节图就都传,写清哪张看整体、哪张看细节)。服装图里的包、模特的身材脸和姿势、背景、吊牌和品牌商标都不用。没有服装图时才用文字写衣服(按 `style.md` 现搭),模板里 Image 2 那两句删掉、Outfit 写全。
即梦里写:"@图片N 只用于她的身材比例和这条的衣服;脸按人脸图,不用它的白色背景"。
```
Image 1 is a body reference: use it only for her body shape and proportions, ignore its clothing and background.
Image 2[ and Image 3] show the outfit: use them only for the clothes (colors, knit texture, cut, neckline, buttons, trims) and copy them exactly[; Image 2 for the whole outfit, Image 3 for the details]. Ignore the model's body, face, pose and background in these images, do not include the bag, and remove any labels, tags or brand logos.
Make an on-body outfit photo sheet of the same woman. Portrait canvas 3:4. Two equal panels side by side touching each other, no gap, no divider line: left panel front view, right panel back view. Pure white background, soft even studio-like light, photorealistic, no text.
In each panel her body fills the full height: cropped just below the lips at the top (no face visible), shoes almost touching the bottom edge, very little white space on the sides; same body, same scale, standing straight and relaxed with arms down at her sides.
Camera at her waist height, straight on, about 50mm lens, no high angle, no wide-angle distortion, so her legs keep their real length.
Keep the body proportions of Image 1 exactly; if the outer layer is open, her waistline is still visible.
Body: about [height], [weight], [shape: very defined small waist, rounded hips, long legs — from the character card]. Feminine, not muscular.
Outfit: [有服装图:一句话点名每件,"the brown cardigan, the olive top and the olive wide-leg trousers from Image 2",季节不对加一句冬天外套;没有服装图:每件写颜色 + 材质 + 款式 + 怎么穿;领口可以开低,露一点乳沟,不露内衣].
Shoes: [颜色 + 款式].
No bag, nothing in her hands.
Avoid: any text, a visible face, a bag, extra people, the outfit model's body shape, brand logos, visible underwear.
```
出图后哪一处不对,只改那一处(`Change only: …`)。

**身材曲线图模板(建号时做一次;只在 ChatGPT 出无头上身图时传)**
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

## 四之三、分镜图(可选,用户说"出分镜图"时出;文案和镜头定了以后、出即梦提示词之前)
主要给用户看:镜头、机位、走位对不对,先在图上看清楚,不对就先改文字,少抽卡。简单的条只给用户看;两个人走位、镜头多、动作复杂的条,也可以传进即梦当参考。
- 用 ChatGPT 出,只传包的锚点图(只用来画准包的轮廓);人脸图、无头上身图不传。
- 竖版宫格,3×3 或 2×4,一格一个镜头或一个时间段;黑白铅笔素描线稿,人物画简单的五官和表情(看得出在笑、看包还是看镜头)。
- 每格画清:景别(全身、半身、近景);机位(拍的人在哪、手机朝哪,用一个小手机图标和箭头);人物站位和走位(箭头);包在她身上的位置;手在干什么;左上角只写镜头号和秒数("3 | 4-6s")。
- 看完哪几格不对,只改那几格的文字,再出一次。

**模板**(`[ ]` 按本条填)
```
Image 1 is the bag: use it only to draw the bag's outline and shape correctly.
Draw a storyboard sheet for a [N]-second vertical phone video: a [3x3 / 2x4] grid of equal vertical panels, black-and-white pencil sketch, clean line art on white paper, no color, no shading fills.
People are simple line drawings with simple faces and clear expressions. In the top-left corner of each panel write only the shot number and seconds, like "1 | 0-2s". Show the phone camera position with a small phone icon and an arrow for where it points, and use arrows for where people walk or turn.
Panel 1 ([秒数]): [景别], [机位:拍的人在哪], [她在哪、在做什么、往哪走], [包在身上哪里], [手在干什么], [表情].
Panel 2 ([秒数]): …
(每格一句,按时间轴写)
No other text, no color, no photo realism.
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
- **每条提示词放进一个真正的代码块**(三个反引号开头结尾,开头写 text),一张图一个代码块,方便一键复制;块里只放要粘进 ChatGPT 的文字,说明写在块外;Change only 那几句也各放一个代码块。代码块里手动换行:只在一句话说完的地方换行,一句一行,不在句子中间断开。
- 检查项按本条写三条,只看用户自己能看出来的:包和商品图是不是一样(颜色、花纹、形状、提带、五金);手指数对不对、看起来放松、指甲和首饰对不对;包在画面中间、整张图配色舒服、除了包没有别的花纹、没有字和 logo。白底重绘图另看:和原图逐项对(颜色、花纹大小和间距、五金个数和位置、提带连在哪、口袋、字样)。
- 用户说哪里不对:构图、姿势、光的大问题整张重做;小细节给一句 `Change only: …… Keep everything else exactly the same: …` 一次只改一处。
- 用户说"太素""没感觉":先查配色(深浅齐不齐、有没有辅色和点缀、冷暖比例)、再查光(有没有方向和光斑)、再查质感叠加和生活感,哪条没到位改哪条,整张重做。
