#!/usr/bin/env python3
"""seongjerry_ 캐러셀 s02 · 자는 동안 클로드가 해 놓는 일 3가지 (6장 mp4, 1080x1350, 무음)
규칙: 상단 문구·쪽번호·넘겨서 보기·이름표 없음. 연한 하늘색 톤. 표지는 밤→아침.
근거: support.claude.com 예약 작업(클라우드 실행, 유료 요금제, 시간별·매일·매주·평일)
실행: python3 generator/sj/s02.py → publish/media/sj02-01..06.mp4, /tmp/sj02-sheet.jpg, /tmp/sj02-mid.jpg
"""
import pathlib, sys, tempfile, shutil, subprocess
R = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / "generator/carousel"))
import kit

CSS = """
@import url("%s");
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Paperlogy,sans-serif;font-weight:500;letter-spacing:-.035em;word-break:keep-all;color:#0F1B2D}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;background:linear-gradient(180deg,#DCEEFF 0%%,#F3F9FF 50%%,#FFFFFF 100%%)}
.blob{position:absolute;border-radius:50%%;filter:blur(80px);opacity:.7}
.no{position:absolute;left:80px;top:90px;font-family:Kkakdugi,Paperlogy;font-size:150px;font-weight:700;line-height:1;color:#1F7FE0;letter-spacing:-.02em}
.when{position:absolute;right:80px;top:118px;background:#0F1B2D;color:#fff;border-radius:999px;padding:14px 30px;font-size:34px;font-weight:800}
h1{position:absolute;left:80px;right:80px;top:270px;font-size:84px;font-weight:900;line-height:1.18;letter-spacing:-.055em}
h1 b{color:#1F7FE0}
.card{position:absolute;left:80px;right:80px;background:#fff;border-radius:36px;box-shadow:0 24px 60px rgba(20,70,140,.18);padding:40px 44px}
.card .hd{display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:700;color:#7A8CA1;margin-bottom:22px}
.li{display:flex;gap:18px;align-items:flex-start;font-size:36px;font-weight:700;line-height:1.4;padding:8px 0}
.li:before{content:"";flex:none;width:16px;height:16px;border-radius:50%%;background:#1F7FE0;margin-top:17px}
.li small{display:block;font-size:28px;font-weight:500;color:#5B7088}
.say{position:absolute;left:80px;right:80px;background:#0F1B2D;color:#fff;border-radius:32px;padding:34px 40px}
.say .t{font-size:27px;font-weight:700;color:#8FC6FF}
.say .q{font-size:35px;font-weight:700;line-height:1.45;margin-top:10px}
.note{position:absolute;left:80px;right:80px;font-size:29px;font-weight:600;color:#55708C;line-height:1.5}
.chip{display:inline-block;background:#E4F1FF;color:#1F7FE0;border-radius:999px;padding:8px 22px;font-size:27px;font-weight:800}
.me{align-self:flex-end;background:#DCEEFF;border-radius:28px 28px 8px 28px;padding:22px 30px;font-size:35px;font-weight:700;line-height:1.4;max-width:760px}
.n{background:rgba(255,255,255,.94);border-radius:30px;padding:26px 30px;display:flex;gap:22px;align-items:center;box-shadow:0 16px 40px rgba(20,70,140,.2)}
.n i{flex:none;width:68px;height:68px;border-radius:18px;background:#1F7FE0;display:flex;align-items:center;justify-content:center;color:#fff;font-style:normal;font-weight:900;font-size:34px}
.n b{font-size:33px;font-weight:800;display:block}.n span{font-size:26px;color:#6B7F96;font-weight:600}
.n em{margin-left:auto;font-style:normal;font-size:24px;color:#9AA9BA;font-weight:600;align-self:flex-start}
""" % kit.FONTS

JS = """<script>
const c=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-x,3);
const eb=x=>{const k=2.2;return 1+(k+1)*Math.pow(x-1,3)+k*Math.pow(x-1,2)};
window.setT=function(t){
 document.querySelectorAll('[data-in]').forEach(e=>{const p=eo(c((t-+e.dataset.in)/0.45));e.style.opacity=p;e.style.transform='translateY('+((1-p)*30)+'px)'});
 document.querySelectorAll('[data-pop]').forEach(e=>{const x=c((t-+e.dataset.pop)/0.5),p=x<=0?0:eb(x);e.style.opacity=c(x*3);e.style.transform=(e.dataset.tf||'')+' scale('+(0.6+0.4*p)+')'});
 document.querySelectorAll('[data-type]').forEach(e=>{if(!e.dataset.full)e.dataset.full=e.textContent;const f=e.dataset.full,n=Math.round(c((t-+e.dataset.type)/(+e.dataset.dur||1.2))*f.length);e.textContent=f.slice(0,n)});
 document.querySelectorAll('[data-pulse]').forEach(e=>{const s=+e.dataset.pulse;if(t<s)return;const p=0.5+0.5*Math.sin((t-s)*2*Math.PI/1.1);e.style.boxShadow='0 0 0 '+(6+14*p)+'px rgba(31,127,224,'+(0.28-0.2*p)+')'});
 document.querySelectorAll('.blob').forEach((e,i)=>{e.style.transform='translate('+(Math.sin(t*1.1+i*2)*30)+'px,'+(Math.cos(t*0.8+i)*24)+'px)'});
 document.querySelectorAll('.star').forEach((e,i)=>{e.style.opacity=0.35+0.6*Math.abs(Math.sin(t*1.6+i*1.3))});
 if(window.extra)window.extra(t);
};</script>"""

BLOBS = '<div class="blob" style="width:340px;height:340px;background:#A9D6FF;right:-120px;top:420px"></div><div class="blob" style="width:260px;height:260px;background:#C9F1E4;left:-90px;top:900px;opacity:.5"></div>'
noti = lambda t, s, h, at: f'<div class="n" data-pop="{at}"><i>✓</i><div><b>{t}</b><span>{s}</span></div><em>{h}</em></div>'

S = []
# 1 표지: 밤 → 아침
stars = "".join(f'<i class="star" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w}px;border-radius:50%;background:#fff"></i>' for x, y, w in [(300,120,6),(520,70,5),(760,150,7),(930,90,5),(640,236,6),(430,250,5),(880,300,6),(180,330,5),(990,420,5)])
S.append(f"""<div class="s" style="background:linear-gradient(180deg,#0B1830 0%,#1B4F8F 38%,#8CC8FF 62%,#EAF6FF 100%)">
 <div id="moon" style="position:absolute;left:90px;top:96px;width:110px;height:110px;border-radius:50%;background:#FFF3C4;box-shadow:0 0 60px rgba(255,243,196,.5)"></div>
 <div id="moon2" style="position:absolute;left:130px;top:80px;width:110px;height:110px;border-radius:50%;background:#0D1D38"></div>
 {stars}
 <div style="position:absolute;left:80px;right:80px;top:290px;font-size:112px;font-weight:900;line-height:1.14;color:#fff;letter-spacing:-.055em">
  <div data-in="0.1">자는 동안</div><div data-in="0.35">클로드가</div><div data-in="0.6"><span style="color:#FFE27A">해 놓는 일 3가지</span></div></div>
 <div style="position:absolute;left:80px;right:80px;top:770px;display:flex;flex-direction:column;gap:20px">
  {noti("오늘 보험 뉴스 브리핑","금감원 발표 포함 · 요약 완료","오전 6:10",1.3)}
  {noti("월요일 고객 안부 메시지","초안 3가지 준비됨","오전 6:30",1.9)}
  {noti("블로그 · 인스타 원고 초안","검토만 하면 돼요","오전 6:50",2.5)}
 </div>
 <div data-in="3.3" style="position:absolute;left:80px;top:1232px;font-size:38px;font-weight:800;color:#2B5480">출근 전에 이미 끝나 있어요</div></div>""")
# 2 원리
S.append(f"""<div class="s">{BLOBS}
 <h1 style="top:110px">딱 한 번만<br><b>말해 두면</b> 됩니다</h1>
 <div class="card" style="top:380px;display:flex;flex-direction:column;gap:26px">
  <div class="me" data-in="0.3"><span data-type="0.5" data-dur="1.5">매일 아침 6시에 보험 뉴스 정리해 줘</span></div>
  <div data-pop="2.3" data-pulse="2.9" style="align-self:flex-start;background:#0F1B2D;color:#fff;border-radius:26px;padding:26px 34px;transform-origin:left center">
   <div style="font-size:26px;font-weight:700;color:#8FC6FF">예약 작업이 만들어졌어요</div>
   <div style="font-size:42px;font-weight:900;margin-top:6px">매일 · 오전 6:00</div></div>
 </div>
 <div style="position:absolute;left:80px;right:80px;top:800px;display:flex;flex-direction:column;gap:20px">
  <div class="n" data-pop="3.0"><i>1</i><div><b>PC를 꺼 놔도 돌아가요</b><span>클라우드에서 실행되는 예약 작업</span></div></div>
  <div class="n" data-pop="3.3"><i>2</i><div><b>주기는 말로 정해요</b><span>매시간 · 매일 · 평일 · 매주</span></div></div>
  <div class="n" data-pop="3.6"><i>3</i><div><b>유료 요금제에서 쓸 수 있어요</b><span>대화창에서 그대로 요청하면 돼요</span></div></div>
 </div></div>""")
def item(no, when, title, hd, rows, say, note):
    lis = "".join(f'<div class="li" data-in="{0.9+i*0.45}"><div>{a}<small>{b}</small></div></div>' for i, (a, b) in enumerate(rows))
    return f"""<div class="s">{BLOBS}<div class="no" data-pop="0.1" data-tf="" style="transform-origin:left center">{no}</div><div class="when" data-pop="0.3">{when}</div>
 <h1>{title}</h1>
 <div class="card" style="top:500px" data-in="0.6"><div class="hd"><span>{hd}</span><span class="chip">자동 완료</span></div>{lis}</div>
 <div class="say" style="top:1000px" data-pop="2.6" data-pulse="3.3"><div class="t">이렇게 말해 두세요</div><div class="q">{say}</div></div>
 <div class="note" style="top:1232px" data-in="3.4">{note}</div></div>"""
S.append(item("01", "매일 아침", "오늘의 <b>보험 뉴스</b><br>브리핑", "오전 6:10 도착",
  [("금감원 · 금융위 발표", "어제 나온 보험 관련 보도자료 요약"), ("업계 주요 뉴스 5줄", "상담 때 꺼낼 이야깃거리"), ("오늘 고객에게 할 한마디", "뉴스에서 뽑은 안내 포인트")],
  "\"매일 아침 6시, 어제 나온 금감원 보험 발표와 업계 뉴스를 5줄로 정리해 줘\"", "요약은 출처 링크와 함께 받아서 원문을 확인하세요."))
S.append(item("02", "매주 월요일", "고객에게 보낼<br><b>안부 메시지</b> 초안", "월요일 오전 6:30 도착",
  [("이번 주 알아 두면 좋은 소식", "계절 · 제도 변경 · 건강 정보 중 하나"), ("말투가 다른 초안 3가지", "정중하게 · 친근하게 · 짧게"), ("가입 권유 없는 안부 중심", "읽고 부담 없는 내용으로")],
  "\"매주 월요일 아침, 고객에게 보낼 안부 메시지 초안을 3가지 말투로 써 줘\"", "초안까지만 맡기고, 발송은 직접 읽어 보고 하세요.<br>고객 이름과 연락처는 넣지 않아도 됩니다."))
S.append(item("03", "평일 아침", "<b>블로그 · 인스타</b><br>원고 초안", "오전 6:50 도착",
  [("블로그 원고 초안 1편", "제목 3개와 본문 뼈대까지"), ("인스타 캡션 1개", "짧은 줄바꿈과 해시태그 포함"), ("어제 쓴 주제와 겹치지 않게", "지난 초안을 보고 새 주제로")],
  "\"평일 아침마다 블로그 원고 초안 1편과 인스타 캡션 1개를 준비해 줘\"", "보험 광고가 되는 글은 올리기 전에 심의 기준을 확인하세요."))
# 6 마무리
S.append(f"""<div class="s">{BLOBS}
 <h1 style="top:120px">내일 아침부터<br><b>하나만</b> 맡겨 보세요</h1>
 <div style="position:absolute;left:80px;right:80px;top:420px;display:flex;gap:24px">
  {''.join(f'<div data-pop="{0.5+i*0.35}" style="flex:1;background:#fff;border-radius:34px;padding:40px 20px;text-align:center;box-shadow:0 20px 50px rgba(20,70,140,.16)"><div style="font-size:78px;line-height:1">{ic}</div><div style="font-size:40px;font-weight:900;margin-top:18px">{a}</div><div style="font-size:27px;color:#5B7088;font-weight:600;margin-top:8px;line-height:1.4">{b}</div></div>' for i,(ic,a,b) in enumerate([("🔖","저장","나중에 따라<br>해 보려면"),("📨","공유","같이 일하는<br>설계사님께"),("➕","팔로우","설계사의 AI<br>활용법 더 보기")]))}
 </div>
 <div class="say" style="top:800px" data-pop="2.0" data-pulse="2.8"><div class="t">자료가 필요하신 분은</div><div class="q">댓글 남겨 주세요.<br>따라 하기 자료는 아직 만드는 중이라,<br>완성되면 보내 드릴게요.</div></div>
 <div data-in="3.2" style="position:absolute;left:0;right:0;top:1160px;text-align:center;font-size:44px;font-weight:900;color:#1F7FE0">@seongjerry_</div></div>""")

CAPTION = """자는 동안 클로드한테
일 시켜 본 적 있으세요?

한 번만 말해 두면
매일, 매주 알아서 해 놓는
'예약 작업' 3가지예요

1. 매일 아침
보험 뉴스 브리핑

2. 매주 월요일
고객 안부 메시지 초안

3. 평일 아침
블로그 · 인스타 원고 초안

PC를 꺼 놔도 돌아가고
출근하면 이미 끝나 있어요
(유료 요금제 기능이에요)

고객 메시지는 초안까지만,
보내는 건 꼭 직접 읽고 하세요

따라 하기 자료가 필요하시면
댓글 남겨 주세요
만드는 중이라 완성되면
보내 드릴게요

저장해 두고 하나만 맡겨 보세요

#클로드 #보험설계사 #AI활용 #업무자동화 #예약작업"""

def build():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    work = pathlib.Path(tempfile.mkdtemp(prefix="sj02_")); outs = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=kit.CHROME, args=["--no-sandbox"]); pg = b.new_page(viewport={"width":1080,"height":1350})
        for i, body in enumerate(S, 1):
            h = work / f"{i}.html"; h.write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}{JS}</body></html>', encoding="utf-8")
            pg.goto(h.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            out = kit.MEDIA / f"sj02-{i:02d}.mp4"; kit.motion(pg, {"dur": 5}, out, work); outs.append(out)
        b.close()
    kit.sheet(outs, work, pathlib.Path("/tmp/sj02-sheet.jpg"))
    ims = []
    for o in outs:
        f = work / (o.stem + "_m.jpg"); subprocess.run(["ffmpeg","-loglevel","error","-y","-ss","2.0","-i",str(o),"-frames:v","1",str(f)],check=True); ims.append(Image.open(f))
    s = Image.new("RGB", (432*6, 540)); [s.paste(im.convert("RGB").resize((432,540)), (i*432,0)) for i, im in enumerate(ims)]; s.save("/tmp/sj02-mid.jpg", quality=88)
    for i,o in enumerate(outs,1): subprocess.run(["ffmpeg","-loglevel","error","-y","-sseof","-0.2","-i",str(o),"-frames:v","1",f"/tmp/sj02-f{i}.jpg"],check=True)
    shutil.rmtree(work); print("ok", [o.name for o in outs])

if __name__ == "__main__":
    build()
