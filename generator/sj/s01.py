#!/usr/bin/env python3
"""seongjerry_ 캐러셀 s01 · 설계사 10명 중 9명이 모르는 클로드 설정 3가지 (6장 전부 mp4, 1080x1350, 무음)
톤: 연한 하늘색(계정 피드 색) + 표지만 짙은 남색. 실명 계정이라 보험 상품·수입 언급 없음.
근거: support.claude.com 메모리(채팅에서 메모리 생성) / 프로젝트(지식·지침, 무료 5개) / 스킬(사용자 정의 > 스킬)
실행: python3 generator/sj/s01.py  → publish/media/sj01-01..06.mp4
"""
import pathlib, sys, tempfile, shutil
R = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / "generator/carousel"))
import kit

CSS = """
@import url("%s");
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Paperlogy,sans-serif;font-weight:500;letter-spacing:-.03em;word-break:keep-all;color:#0F1B2D;background:#EEF6FD}
.s{position:relative;width:1080px;height:1350px;overflow:hidden}
.blob{position:absolute;border-radius:50%%;filter:blur(70px);opacity:.75}
.tag{position:absolute;top:44px;left:0;right:0;text-align:center;font-size:24px;font-weight:600;color:#6B7F96}
h1{position:absolute;left:72px;right:72px;top:118px;text-align:center;font-size:72px;font-weight:900;line-height:1.2;letter-spacing:-.05em}
h1 b{color:#1F7FE0}
.stage{position:absolute;left:0;right:0;top:330px;height:560px;background:rgba(255,255,255,.55);display:flex;align-items:center;justify-content:center}
.card{background:#fff;border-radius:28px;box-shadow:0 20px 50px rgba(31,90,160,.16);padding:34px 38px}
.box{position:absolute;left:72px;right:72px;top:940px;background:#fff;border:3px solid #0F1B2D;border-radius:22px;padding:34px 40px}
.box h3{font-size:36px;font-weight:900}
.box h3 i{font-style:normal;color:#1F7FE0}
.box p{font-size:31px;line-height:1.5;color:#33465C;margin-top:10px}
.foot{position:absolute;left:72px;right:72px;bottom:40px;display:flex;justify-content:space-between;font-size:24px;font-weight:600;color:#8496AB}
.me{align-self:flex-end;background:#DCEEFF;border-radius:24px 24px 6px 24px;padding:18px 26px;font-size:30px;font-weight:600;max-width:640px}
.ai{font-size:31px;line-height:1.5;color:#1B2B40;margin-top:22px}
.chip{display:inline-flex;align-items:center;gap:10px;background:#E4F1FF;color:#1F7FE0;border-radius:999px;padding:8px 20px;font-size:25px;font-weight:700;margin-top:20px}
.chip:before{content:"";width:16px;height:16px;border-radius:50%%;background:#1F7FE0}
.file{display:flex;align-items:center;gap:18px;background:#F4F8FC;border-radius:16px;padding:16px 22px;font-size:28px;font-weight:600}
.file:before{content:"";width:34px;height:42px;border-radius:6px;background:#9CCBFA;flex:none}
.tg{width:84px;height:48px;border-radius:999px;background:#C9D5E2;position:relative;flex:none}
.tg i{position:absolute;top:5px;left:5px;width:38px;height:38px;border-radius:50%%;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.2)}
.row{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:20px 0;border-bottom:2px solid #EEF2F6}
.row b{font-size:30px}.row span{display:block;font-size:23px;color:#7A8CA1;margin-top:4px;font-weight:500}
.dark{background:#0A1322;color:#fff}
.dark .tag{color:#7F93AB}
.pill{display:inline-block;background:#fff;color:#0A1322;font-weight:900;font-size:34px;border-radius:999px;padding:10px 28px;letter-spacing:-.02em}
""" % kit.FONTS

JS = """<script>
const c=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-x,3);
window.setT=function(t){
 document.querySelectorAll('[data-in]').forEach(e=>{const p=eo(c((t-+e.dataset.in)/0.45));e.style.opacity=p;e.style.transform=(e.dataset.tf||'')+' translateY('+((1-p)*26)+'px)'});
 document.querySelectorAll('[data-tg]').forEach(e=>{const p=eo(c((t-+e.dataset.tg)/0.3));e.style.background='rgb('+Math.round(201-170*p)+','+Math.round(213-86*p)+','+Math.round(226-2*p)+')';e.firstElementChild.style.left=(5+36*p)+'px'});
 document.querySelectorAll('[data-type]').forEach(e=>{if(!e.dataset.full)e.dataset.full=e.textContent;const f=e.dataset.full,n=Math.round(c((t-+e.dataset.type)/(+e.dataset.dur||1.2))*f.length);e.textContent=f.slice(0,n)});
 document.querySelectorAll('.blob').forEach((e,i)=>{e.style.transform='translate('+(Math.sin(t*1.2+i*2)*26)+'px,'+(Math.cos(t*0.9+i)*22)+'px)'});
 document.querySelectorAll('[data-num]').forEach(e=>{const s=e.dataset.num.split(',');let v=1;s.forEach((x,i)=>{if(t>=+x)v=i+2});e.textContent=Math.min(v,3)});
 if(window.extra)window.extra(t);
};</script>"""

TAG = "AI로 일하는 설계사 · @seongjerry_"
BLOBS = '<div class="blob" style="width:300px;height:300px;background:#A9D6FF;left:-90px;top:520px"></div><div class="blob" style="width:260px;height:260px;background:#CFE3FF;right:-80px;top:300px"></div><div class="blob" style="width:200px;height:200px;background:#B8F0E0;right:40px;top:760px;opacity:.5"></div>'

def inner(title, stage, box, n):
    return f'<div class="s">{BLOBS}<div class="tag">{TAG}</div><h1>{title}</h1><div class="stage">{stage}</div><div class="box">{box}</div><div class="foot"><span>{n}/6</span><span>넘겨서 보기 →</span></div></div>'

S = []
# 1 표지
people = "".join(f'<i style="display:inline-block;width:44px;height:44px;margin:0 9px;border-radius:50% 50% 12px 12px;background:{"#3FA2FF" if i==6 else "#2A3A52"};{"box-shadow:0 0 0 8px rgba(63,162,255,.22)" if i==6 else ""}"></i>' for i in range(10))
S.append(f"""<div class="s dark">
 <div class="tag">{TAG}</div>
 <div style="position:absolute;top:120px;left:0;right:0;text-align:center">{people}</div>
 <div class="card" style="position:absolute;left:220px;top:250px;width:640px;height:760px;transform:perspective(1400px) rotateX(8deg) rotateZ(-3deg);color:#0F1B2D;padding:36px 40px">
  <div style="font-size:26px;color:#7A8CA1;font-weight:700">설정</div>
  <div class="row"><div><b>채팅에서 메모리 생성</b><span>내 상담 스타일을 기억해요</span></div><div class="tg" data-tg="0.6"><i></i></div></div>
  <div class="row"><div><b>프로젝트 지식</b><span>약관·자료를 한 번만 올려요</span></div><div class="tg" data-tg="1.3"><i></i></div></div>
  <div class="row" style="border:0"><div><b>스킬</b><span>내 말투와 양식을 저장해요</span></div><div class="tg" data-tg="2.0"><i></i></div></div>
 </div>
 <div style="position:absolute;left:0;right:0;top:560px;bottom:0;background:linear-gradient(rgba(10,19,34,0),#0A1322 46%)"></div>
 <div style="position:absolute;left:72px;right:72px;top:890px">
  <span class="pill">전성재</span>
  <div style="font-size:88px;font-weight:900;line-height:1.18;letter-spacing:-.05em;margin-top:26px">설계사 10명 중 9명이<br>모르는 <span style="color:#6DB8FF">클로드 설정 3가지</span></div>
 </div>
 <div class="foot" style="color:#62758C"><span>1/6</span><span>넘겨서 보기 →</span></div></div>""")
# 2 메모리
S.append(inner("내 상담 스타일을<br><b>기억하게</b> 합니다", """
 <div class="card" style="width:860px;display:flex;flex-direction:column">
  <div class="me" data-in="0.4">지난번에 정한 톤으로 상담 안내문 써 줘</div>
  <div class="ai" data-in="1.3">네, <b>존댓말 · 짧은 문장 · 보험 용어는 풀어서</b><br>지난번에 정하신 그대로 쓸게요.</div>
  <div data-in="2.1"><span class="chip">메모리 참고 · 내 상담 스타일</span></div>
 </div>""", """<h3>설정 → <i>채팅에서 메모리 생성</i> 켜기</h3>
 <p>대화 중에 "이거 기억해 줘" 한마디면 다음 대화부터 적용돼요. 내 소개와 말투를 매번 다시 설명하지 않아도 됩니다.</p>""", 2))
# 3 프로젝트
S.append(inner("약관은 <b>한 번만</b><br>올려 둡니다", """
 <div class="card" style="width:860px">
  <div style="font-size:26px;color:#7A8CA1;font-weight:700;margin-bottom:14px">프로젝트 지식</div>
  <div style="display:flex;flex-direction:column;gap:12px">
   <div class="file" data-in="0.3">상품 약관.pdf</div><div class="file" data-in="0.7">상품 요약서.pdf</div><div class="file" data-in="1.1">광고 심의 기준.docx</div>
  </div>
  <div style="display:flex;flex-direction:column;margin-top:22px">
   <div class="me" data-in="1.9">이 특약, 면책기간이 어떻게 돼?</div>
   <div data-in="2.7"><span class="chip">상품 약관.pdf 에서 찾는 중</span></div>
  </div>
 </div>""", """<h3>프로젝트 → <i>파일 추가 + 지침 설정</i></h3>
 <p>그 프로젝트 안의 모든 채팅이 같은 자료를 봐요. 무료 계정도 5개까지 만들 수 있어요. 고객 개인정보가 담긴 서류는 올리지 마세요.</p>""", 3))
# 4 스킬
S.append(inner("내 말투와 양식을<br><b>저장</b>합니다", """
 <div style="display:flex;gap:26px;width:900px">
  <div class="card" style="flex:1;opacity:.75" data-in="0.3"><div style="font-size:24px;color:#9AA9BA;font-weight:700">그냥 시키면</div>
   <p style="font-size:27px;line-height:1.55;color:#9AA9BA;margin-top:14px;text-decoration:line-through">안녕하십니까 고객님. 금번 안내드릴 사항은 다음과 같사오니 참고하여 주시기 바랍니다.</p></div>
  <div class="card" style="flex:1" data-in="1.4"><div style="font-size:24px;color:#1F7FE0;font-weight:800">내 스킬을 쓰면</div>
   <p style="font-size:28px;line-height:1.55;margin-top:14px;font-weight:600">안녕하세요 고객님!<br>지난번 말씀드린 내용, 세 줄로 정리해 드릴게요.</p>
   <div data-in="2.3"><span class="chip" style="font-size:22px">안내문 스킬 읽는 중</span></div></div>
 </div>""", """<h3>사용자 정의 → <i>스킬</i></h3>
 <p>잘 썼던 글 하나를 붙여 넣고 "이걸로 스킬 만들어 줘"라고 하면 돼요. 비슷한 일을 시킬 때마다 알아서 꺼내 씁니다.</p>""", 4))
# 5 요약
S.append(inner("세 가지가 하는 일은<br><b>서로 달라요</b>", """
 <div class="card" style="width:860px;padding:22px 40px">
  <div class="row" data-in="0.3"><div><b>메모리</b><span>나를 기억해요 (역할, 말투, 선호)</span></div><div class="tg" data-tg="0.8"><i></i></div></div>
  <div class="row" data-in="1.1"><div><b>프로젝트</b><span>자료를 기억해요 (약관, 기준, 지침)</span></div><div class="tg" data-tg="1.6"><i></i></div></div>
  <div class="row" style="border:0" data-in="1.9"><div><b>스킬</b><span>방식을 기억해요 (양식, 순서, 예시)</span></div><div class="tg" data-tg="2.4"><i></i></div></div>
  <div style="text-align:center;margin-top:18px;font-family:Kkakdugi,Paperlogy;font-size:74px;font-weight:700;color:#1F7FE0"><span data-num="0.8,1.6,2.4" id="n">0</span><span style="color:#B7C6D6">/3</span></div>
 </div>""", """<h3>저는 이렇게 나눠 써요</h3>
 <p>블로그 원고, 유튜브 대본, 리크루팅 글을 프로젝트로 따로 두고, 자주 쓰는 양식은 스킬로 저장해 뒀어요. AI 답은 원문으로 한 번 더 확인합니다.</p>""", 5))
# 6 마무리
S.append(f"""<div class="s">{BLOBS}<div class="tag">{TAG}</div>
 <h1 style="top:150px">오늘 <b>하나만</b><br>켜 보세요</h1>
 <div class="card" style="position:absolute;left:110px;right:110px;top:400px;padding:44px 50px">
  <div style="font-size:28px;color:#7A8CA1;font-weight:700">5분이면 끝나는 순서</div>
  <div style="display:flex;flex-direction:column;gap:26px;margin-top:26px;font-size:36px;font-weight:800">
   <div data-in="0.4">① 메모리 켜고 내 소개 한 번 말하기</div>
   <div data-in="1.0">② 프로젝트 하나 만들고 자료 올리기</div>
   <div data-in="1.6">③ 잘 쓴 글로 스킬 하나 만들기</div>
  </div>
 </div>
 <div class="box" style="top:850px" data-in="2.4"><h3>저장해 두고 하나씩 따라 해 보세요</h3>
 <p>같이 일하는 설계사님께 공유해 주세요. 설계사가 실제로 쓰는 AI 세팅을 계속 올릴게요.</p></div>
 <div style="position:absolute;left:0;right:0;top:1130px;text-align:center" data-in="3.0"><span class="pill" style="background:#0F1B2D;color:#fff">@seongjerry_ 팔로우</span></div>
 <div class="foot"><span>6/6</span><span>저장 · 공유</span></div></div>""")

CAPTION = """클로드 깔고 그냥
대화만 하고 계셨다면
설정부터 한 번 열어 보세요

1. 메모리 켜기
내 상담 스타일을 기억해요
매번 다시 설명 안 해도 돼요

2. 프로젝트에 약관 올리기
한 번 올리면 그 안의
모든 채팅이 같은 자료를 봐요

3. 스킬로 내 말투 저장
잘 쓴 글 하나만 있으면
그다음부터 알아서 맞춰 써요

고객 개인정보가 담긴 서류는
올리지 마시고, AI 답은
원문으로 한 번 더 확인하세요

저장해 두고 하나씩 켜 보세요
같이 일하는 설계사님께 공유!

#클로드 #보험설계사 #AI활용 #업무자동화 #설계사일상"""

def build():
    from playwright.sync_api import sync_playwright
    work = pathlib.Path(tempfile.mkdtemp(prefix="sj01_")); outs = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=kit.CHROME, args=["--no-sandbox"]); pg = b.new_page(viewport={"width":1080,"height":1350})
        for i, body in enumerate(S, 1):
            h = work / f"{i}.html"; h.write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}{JS}</body></html>', encoding="utf-8")
            pg.goto(h.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            out = kit.MEDIA / f"sj01-{i:02d}.mp4"; kit.motion(pg, {"dur": 5}, out, work); outs.append(out)
        b.close()
    kit.sheet(outs, work, pathlib.Path("/tmp/sj01-sheet.jpg")); shutil.rmtree(work); print("ok", [o.name for o in outs])

if __name__ == "__main__":
    build()
