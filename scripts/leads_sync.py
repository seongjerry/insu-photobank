#!/usr/bin/env python3
"""보험비밀노트 상담 신청 동기화
Supabase bsn_leads 에서 아직 처리 안 된 신청을 읽어
1) 텔레그램(@Jerryblogbot)으로 알림  2) 구글 스프레드시트에 한 줄 추가  후 처리 시각을 기록한다.

필요한 저장소 Secrets
  SUPABASE_URL           예: https://xxxx.supabase.co
  SUPABASE_SERVICE_KEY   Supabase > Project Settings > API Keys 의 service_role(secret) 키
  TELEGRAM_TOKEN / TELEGRAM_CHAT_ID   (기존 insu_magazine 알림과 같은 값)
  SHEET_WEBHOOK_URL      구글 Apps Script 웹앱 주소 (?key=비밀값 포함). 없으면 시트 단계는 건너뜀
공개 저장소라 로그에는 개인정보를 남기지 않고 건수만 출력한다.
"""
import os, sys, json, datetime
import requests

SB = os.environ.get("SUPABASE_URL", "").strip().rstrip("/")
KEY = os.environ.get("SUPABASE_SERVICE_KEY", "").strip()
TG_TOKEN = os.environ.get("TELEGRAM_TOKEN", "").strip()
TG_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
SHEET = os.environ.get("SHEET_WEBHOOK_URL", "").strip()
TABLE = "bsn_leads"

if not (SB and KEY):
    print("SUPABASE_URL / SUPABASE_SERVICE_KEY 미설정: 건너뜀"); sys.exit(0)

if not KEY.isascii() or any(c.isspace() for c in KEY) or "•" in KEY:
    print("SUPABASE_SERVICE_KEY 형식 오류: 가려진 값(•)이나 공백·한글이 섞여 있음. 복사 버튼으로 다시 복사해 등록하세요. "
          f"(길이 {len(KEY)}, sb_secret_ 시작 {KEY.startswith('sb_secret_')})"); sys.exit(1)
H = {"apikey": KEY, "Content-Type": "application/json"}
if not KEY.startswith("sb_"):  # 예전 JWT 형식 키일 때만 Bearer 필요
    H["Authorization"] = f"Bearer {KEY}"
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()


def rows(filt):
    r = requests.get(f"{SB}/rest/v1/{TABLE}?{filt}&order=id.asc&limit=50", headers=H, timeout=30)
    r.raise_for_status(); return r.json()


def mark(ids, col):
    if not ids: return
    r = requests.patch(f"{SB}/rest/v1/{TABLE}?id=in.({','.join(map(str, ids))})", headers=H,
                       data=json.dumps({col: now()}), timeout=30)
    r.raise_for_status()


def kst(ts):
    try:
        d = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")) + datetime.timedelta(hours=9)
        return d.strftime("%m/%d %H:%M")
    except Exception:
        return ts or ""


# 1) 텔레그램
sent = []
if TG_TOKEN and TG_CHAT:
    for x in rows("notified_at=is.null"):
        src = " / ".join(v for v in [x.get("utm_source"), x.get("utm_campaign"), x.get("page_topic")] if v)
        msg = (f"📒 보험비밀노트 새 상담 신청\n"
               f"이름: {x.get('name','')}\n연락처: {x.get('phone','')}\n"
               f"주제: {x.get('topic','')}\n연락 시간: {x.get('call_time','')}\n"
               f"마케팅 동의: {x.get('marketing_agree','')}\n"
               f"유입: {src or '직접 방문'}\n접수: {kst(x.get('created_at',''))}")
        r = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                          data={"chat_id": TG_CHAT, "text": msg}, timeout=30)
        if r.ok and r.json().get("ok"):
            sent.append(x["id"])
    mark(sent, "notified_at")
print(f"telegram sent: {len(sent)}")

# 2) 구글 시트
synced = []
if SHEET:
    todo = rows("sheet_synced_at=is.null")
    if todo:
        payload = [{k: x.get(k, "") for k in ["id", "created_at", "name", "phone", "topic", "call_time",
                    "marketing_agree", "page_topic", "utm_source", "utm_medium", "utm_campaign",
                    "utm_content", "utm_term", "referrer"]} for x in todo]
        for p in payload: p["created_at"] = kst(p["created_at"])
        r = requests.post(SHEET, data=json.dumps({"rows": payload}), headers={"Content-Type": "application/json"},
                          timeout=60, allow_redirects=True)
        if r.ok and '"ok":true' in r.text.replace(" ", ""):
            synced = [x["id"] for x in todo]
            mark(synced, "sheet_synced_at")
        else:
            print("sheet webhook failed:", r.status_code)
print(f"sheet synced: {len(synced)}")
