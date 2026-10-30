#!/usr/bin/env python3
"""Pexels(+Pixabay) 무료 사진을 받아 photos/<slug>/ 에 저장하고 index.json을 갱신한다.
GitHub Actions에서 실행. 환경변수: PEXELS_API_KEY (필수), PIXABAY_API_KEY (선택)

라이선스 메모
- Pexels License: 상업적 이용 가능, 출처 표기 불필요. 사진 속 인물을 특정 질병·상황의 당사자처럼 단정하는 표현은 피할 것.
- Pixabay Content License: 동일하게 무료·출처 불필요. 오해를 부르는 맥락 사용 금지.
"""
import json, os, sys, time, pathlib, hashlib, urllib.request, urllib.parse, io
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "keywords.json").read_text(encoding="utf-8"))
OUT = ROOT / "photos"; OUT.mkdir(exist_ok=True)
IDX = ROOT / "index.json"
index = json.loads(IDX.read_text(encoding="utf-8")) if IDX.exists() else {"photos": []}
have = {p["id"] for p in index["photos"]}
BLK = ROOT / "blocked.json"  # 주제와 무관해서 지운 사진은 다시 받지 않음
if BLK.exists():
    have |= set(json.loads(BLK.read_text(encoding="utf-8")).get("ids", []))
MAX_W = 1600

PEXELS = os.environ.get("PEXELS_API_KEY", "")
PIXABAY = os.environ.get("PIXABAY_API_KEY", "")
if not PEXELS and not PIXABAY:
    sys.exit("PEXELS_API_KEY 또는 PIXABAY_API_KEY 필요")

def get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "insu-photobank/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def save(img_bytes, slug, pid):
    im = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, int(im.height * MAX_W / im.width)), Image.LANCZOS)
    d = OUT / slug; d.mkdir(exist_ok=True)
    p = d / f"{pid}.jpg"; im.save(p, "JPEG", quality=86, optimize=True)
    return p, im.size

def pexels(query, n, orient):
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode({"query": query, "per_page": n, "orientation": orient})
    data = json.loads(get(url, {"Authorization": PEXELS}))
    for ph in data.get("photos", []):
        yield {"id": f"pexels_{ph['id']}", "src": ph["src"]["large2x"], "alt": ph.get("alt", ""),
               "credit": ph.get("photographer", ""), "page": ph.get("url", ""), "provider": "pexels"}

def pixabay(query, n, orient):
    url = "https://pixabay.com/api/?" + urllib.parse.urlencode({"key": PIXABAY, "q": query, "image_type": "photo", "per_page": max(3, n),
                                                                 "orientation": "horizontal" if orient == "landscape" else "vertical", "safesearch": "true"})
    data = json.loads(get(url))
    for ph in data.get("hits", []):
        yield {"id": f"pixabay_{ph['id']}", "src": ph.get("largeImageURL") or ph["webformatURL"], "alt": ph.get("tags", ""),
               "credit": ph.get("user", ""), "page": ph.get("pageURL", ""), "provider": "pixabay"}

added = 0
for topic in CFG["topics"]:
    slug, ko = topic["slug"], topic["ko"]
    for q in topic["queries"]:
        srcs = []
        if PEXELS: srcs.append(pexels)
        if PIXABAY: srcs.append(pixabay)
        for fn in srcs:
            try:
                for ph in fn(q, CFG.get("per_query", 8), CFG.get("orientation", "landscape")):
                    if ph["id"] in have: continue
                    try:
                        p, (w, h) = save(get(ph["src"]), slug, ph["id"])
                    except Exception as e:
                        print("skip", ph["id"], e); continue
                    index["photos"].append({"id": ph["id"], "slug": slug, "ko": ko, "query": q, "path": str(p.relative_to(ROOT)),
                                            "w": w, "h": h, "alt": ph["alt"], "credit": ph["credit"], "page": ph["page"], "provider": ph["provider"],
                                            "added": time.strftime("%Y-%m-%d")})
                    have.add(ph["id"]); added += 1
                time.sleep(0.6)  # rate limit 배려 (Pexels 200회/시간)
            except Exception as e:
                print("query fail", fn.__name__, q, e)

index["updated"] = time.strftime("%Y-%m-%d %H:%M")
index["count"] = len(index["photos"])
IDX.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"added {added}, total {index['count']}")
