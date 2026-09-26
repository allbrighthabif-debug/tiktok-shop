# 本项目视频策划入口

本仓库的 skill 位于 `.agents/skills/tiktok-shop-video-planner/`（Claude Code 通过 `.claude/skills/` 软链接读取同一份）。

处理 TikTok Shop 产品拆解、钩子、文案、分镜、生图或即梦提示词时，使用 tiktok-shop-video-planner skill：先读取其 SKILL.md，再按当前阶段读取对应文件。skill 只维护这一份，不另建第二份规则。
用户已选定的阶段和授权优先；新产品默认先完整展示商品分析并停止，用户看过并要求继续后才定方向、出钩子；再确认钩子、确认完整文案，然后做分镜。整套授权也不得省略分析展示，仅上传商品图不算已完成分析。不得建设素材资产库；现有 voice-samples.md、verbal-hooks.md、scenes.md 保留供按需参考。

钩子阶段只展示编号、目标语言文案和中文对照，可加简短方向标题；不附开场画面、观看预期或正文兑现说明。画面设计留到第5步，内部仍检查事实与可兑现性。
