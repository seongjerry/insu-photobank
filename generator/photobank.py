#!/usr/bin/env python3
"""포토뱅크 클라이언트: GitHub 저장소의 index.json을 읽어 키워드에 맞는 사진을 내려받는다.
설정: photobank.config.json  {"repo": "OWNER/REPO", "branch": "main"}
사용: python3 photobank.py 독감 걷기   → 매칭 사진 경로 출력
"""
import json, sys, random, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
CACHE = ROOT / "assets/photobank"; CACHE.mkdir(parents=True, exist_ok=True)
CFG = json.loads((ROOT / "photobank.config.json").read_text(encoding="utf-8"))
RAW = f"https://raw.githubusercontent.com/{CFG['repo']}/{CFG.get('branch','main')}/"

def _get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "insu/1.0"}), timeout=60) as r:
        return r.read()

def index():
    p = CACHE / "index.json"
    try:
        p.write_bytes(_get(RAW + "index.json"))
    except Exception as e:
        if not p.exists(): raise RuntimeError(f"포토뱅크 index.json 조회 실패: {e}")
    return json.loads(p.read_text(encoding="utf-8"))["photos"]

JUNK = ("teddy", "stuffed", "wallpaper", "carnival", "venetian", "fantasy", "surreal", "kermit", "frog", "toy", "doll",
        "cartoon", "illustration", "clipart", "halloween", "costume", "drawing", "3d", "render", "logo", "text")

def pick(keywords, orientation=None, exclude=(), seed=None, prefer=(), avoid=()):
    """keywords: 한글 태그/슬러그(후보군 선정). prefer: 영문 alt 가산 단어. avoid: 영문 alt 제외 단어.
    점수 = prefer 매칭 수. 동점이면 랜덤."""
    photos = [p for p in index() if p["id"] not in exclude]
    bad = tuple(JUNK) + tuple(a.lower() for a in avoid)
    photos = [p for p in photos if not any(b in p.get("alt", "").lower() for b in bad)] or photos
    if orientation == "portrait": photos = [p for p in photos if p["h"] >= p["w"]] or photos
    rnd = random.Random(seed)
    pool = []
    for kw in keywords:
        pool = [p for p in photos if kw in p.get("ko", []) or kw == p["slug"] or kw.lower() in p.get("alt", "").lower()]
        if pool: break
    pool = pool or photos
    if not pool: return None
    def score(p):
        alt = p.get("alt", "").lower()
        return sum(1 for w in prefer if w.lower() in alt)
    best = max(score(p) for p in pool)
    return rnd.choice([p for p in pool if score(p) == best])

def fetch(photo):
    """사진 로컬 경로 반환(캐시)."""
    local = CACHE / photo["path"]; local.parent.mkdir(parents=True, exist_ok=True)
    if not local.exists(): local.write_bytes(_get(RAW + photo["path"]))
    return local

if __name__ == "__main__":
    ph = pick(sys.argv[1:] or ["건강"])
    print(fetch(ph) if ph else "no photo")
