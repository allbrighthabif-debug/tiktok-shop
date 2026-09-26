#!/usr/bin/env bash
# 把 tiktok-shop-video-planner 安装到 Codex 与 Claude Code 的个人 skill 目录。
# 用法：bash install.sh            安装到 ~/.agents/skills 和 ~/.claude/skills
#       bash install.sh <项目目录>  安装到该项目的 .agents/skills 和 .claude/skills
set -euo pipefail

NAME=tiktok-shop-video-planner
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 兼容两种位置：压缩包根目录，或仓库 scripts/ 目录
if [ -f "$HERE/$NAME/SKILL.md" ]; then
  SRC="$HERE/$NAME"
elif [ -f "$HERE/../.agents/skills/$NAME/SKILL.md" ]; then
  SRC="$(cd "$HERE/../.agents/skills/$NAME" && pwd)"
else
  echo "找不到 $NAME/SKILL.md，请在解压后的目录里运行本脚本。" >&2
  exit 1
fi

BASE="${1:-$HOME}"
for dir in "$BASE/.agents/skills" "$BASE/.claude/skills"; do
  mkdir -p "$dir"
  if [ -e "$dir/$NAME" ] || [ -L "$dir/$NAME" ]; then
    backup="$dir/$NAME.bak.$(date +%Y%m%d%H%M%S)"
    mv "$dir/$NAME" "$backup"
    echo "已备份旧版本：$backup"
  fi
  cp -R "$SRC" "$dir/$NAME"
  echo "已安装：$dir/$NAME"
done
echo "完成。重启 Codex / Claude Code 后生效。"
