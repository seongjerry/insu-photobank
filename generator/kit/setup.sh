#!/bin/bash
# 새 작업 공간에서 숏폼 제작 환경 준비: bash generator/kit/setup.sh  → 작업 폴더 $BUILD (기본 /home/claude/build)
set -e
BUILD=${BUILD:-/home/claude/build}; KIT=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$BUILD"; cd "$BUILD"
[ -f package.json ] || npm init -y >/dev/null
[ -d node_modules/pretendard ] || npm i --silent pretendard @fontsource/nanum-pen-script >/dev/null
python3 -c "import playwright, numpy, scipy" 2>/dev/null || pip install -q --break-system-packages playwright numpy scipy
python3 -c "from playwright.sync_api import sync_playwright as s; p=s().start(); p.chromium.launch().close(); p.stop()" 2>/dev/null || python3 -m playwright install chromium >/dev/null
command -v ffmpeg >/dev/null || (apt-get install -y -qq ffmpeg >/dev/null 2>&1 || echo "ffmpeg 설치 필요")
cp "$KIT"/templates/* "$BUILD"/
echo "kit ready: $BUILD"
