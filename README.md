# TikTok Shop 带货视频策划 skill

美区 TikTok Shop AI UGC 视频策划：商品分析 → 方向 → 钩子 → 完整文案 → 分镜 → OpenAI 生图提示词 → 即梦 Seedance 执行稿 → 成片检查与发布，以及数据复盘。

按 [Agent Skills 开放标准](https://github.com/agentskills/agentskills) 编写，同一份文件 **Claude Code 和 Codex 都能用**。

## 目录

```
tiktok-shop-video-planner/     ← skill 本体（整个文件夹就是一个 skill）
├── SKILL.md                   ← 唯一入口：流程、确认点、各阶段必读文件
├── agents/openai.yaml         ← Codex 界面显示名（Claude 会忽略）
├── video-state.md             ← 本片状态记录
├── perspective.md             ← 第2步 拍法方向
├── verbal-hooks.md            ← 第3步 钩子参考库
├── step5-script.md            ← 第4步 完整文案（文件名为历史兼容）
├── step7-storyboard.md        ← 第5步 分镜 / 第7步 即梦执行稿
├── visual-hook.md             ← 第5步 开场画面
├── model-capabilities.md      ← 即梦 / OpenAI 能力核验记录
├── image.md                   ← 第6步 生图与改图提示词
├── character.md / scenes.md   ← 人物与场景参考
├── delivery-check.md          ← 交付检查（证据制）
├── diagnose-iterate.md        ← 数据复盘与迭代
└── voice-samples.md           ← 108 条口播样本库（按标题检索，不整份读）
```

## 使用

直接说需求即可自动触发，例如“帮我给这个商品做一条美区带货视频”并附商品图。也可以显式调用：Claude Code 输入 `/tiktok-shop-video-planner`，Codex 输入 `$tiktok-shop-video-planner`。

默认每个确认点会停下：商品分析 → 等你说继续 → 钩子 → 等你选 → 全文 → 等你确认 → 分镜……

## 维护

- 只改 `.agents/skills/tiktok-shop-video-planner/` 这一份；仓库里的 `.claude/skills/` 是指向它的软链接。
- 打包与安装说明等最终版本确认后再补。
