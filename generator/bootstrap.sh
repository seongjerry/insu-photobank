#!/usr/bin/env bash
# insu_magazine 생성기 부트스트랩: 새 세션에서 한 번 실행하면 생성기·폰트·포토뱅크 인덱스가 준비된다.
# 사용: bash <(curl -sS https://raw.githubusercontent.com/seongjerry/insu-photobank/main/generator/bootstrap.sh)
set -e
REPO=seongjerry/insu-photobank
RAW=https://raw.githubusercontent.com/$REPO/main
D=${INSU_DIR:-$HOME/insu_magazine}
mkdir -p "$D"/{content,out,assets/fonts,assets/photobank,tts/out}
cd "$D"
for f in render.py photobank.py retime.py playbook.json log.json; do
  curl -sS -o "$f" "$RAW/generator/$f"
done
echo "{\"repo\": \"$REPO\", \"branch\": \"main\"}" > photobank.config.json
# 폰트 (npm 레지스트리는 항상 열려 있음)
if [ ! -f assets/fonts/Pretendard-Black.otf ]; then
  T=$(mktemp -d); cd "$T"
  npm pack pretendard@1.3.9 @fontsource/nanum-myeongjo @fontsource/nanum-pen-script >/dev/null 2>&1
  for t in *.tgz; do mkdir -p "${t%.tgz}" && tar xzf "$t" -C "${t%.tgz}"; done
  cp pretendard-*/package/dist/public/static/Pretendard-{Regular,Medium,SemiBold,Bold,ExtraBold,Black}.otf "$D/assets/fonts/"
  cp fontsource-nanum-myeongjo-*/package/files/nanum-myeongjo-korean-{400,700}-normal.woff2 "$D/assets/fonts/"
  cp fontsource-nanum-pen-script-*/package/files/nanum-pen-script-korean-400-normal.woff2 "$D/assets/fonts/"
  cd "$D"; rm -rf "$T"
fi
python3 -c "import playwright, PIL" 2>/dev/null || pip install -q --break-system-packages playwright pillow
curl -sS -o assets/photobank/index.json "$RAW/index.json"
echo "ready: $D  (photos: $(python3 -c "import json;print(json.load(open('assets/photobank/index.json'))['count'])"))"
