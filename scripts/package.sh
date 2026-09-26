#!/usr/bin/env bash
# 打包可分发的 zip：
#   dist/tiktok-shop-video-planner.zip             skill 文件夹 + install.sh + README
#   dist/tiktok-shop-video-planner-skill-only.zip  只含 skill 文件夹（网页版上传用）
set -euo pipefail

NAME=tiktok-shop-video-planner
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cp -R "$ROOT/.agents/skills/$NAME" "$STAGE/$NAME"
cp "$ROOT/scripts/install.sh" "$STAGE/install.sh"
cp "$ROOT/README.md" "$STAGE/README.md"

mkdir -p "$ROOT/dist"
rm -f "$ROOT/dist/$NAME.zip" "$ROOT/dist/$NAME-skill-only.zip"
(cd "$STAGE" && zip -qr -X "$ROOT/dist/$NAME.zip" "$NAME" install.sh README.md)
(cd "$STAGE" && zip -qr -X "$ROOT/dist/$NAME-skill-only.zip" "$NAME")
echo "已生成：dist/$NAME.zip 和 dist/$NAME-skill-only.zip"
