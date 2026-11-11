# 캐러셀 c01 · 몰라서 못 받는 보험금 ① 지정대리청구인
# 출처: 금융감독원 보도자료(2026.6.30.) 대리청구인 지정 제도 개선 / 금융위원회 보도자료(2026.7.8.) 숨은보험금
from kit import bino

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "몰라서 못 받는 보험금 ①"
TOPIC = "부모님 치매보험, 지정대리청구인 안 하면 청구 못 함"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=283380",
           "https://www.heraldk.com/article/2026062819002181533",
           "https://eiec.kdi.re.kr/policy/materialView.do?num=283914"]

S = []
# 1 표지 (움직이는 장)
S.append(f"""
 <span class="chip" style="margin-top:34px">부모님 보험 있는 분 필독</span>
 {bino('wow', 560, 'position:absolute;right:40px;top:150px')}
 <div class="note" id="note" style="position:absolute;left:72px;top:410px;width:420px;font-size:40px">가입자 4명 중 3명이<br>안 해 둔 '이것'</div>
 <h1 style="position:absolute;left:72px;right:60px;top:760px">부모님 치매보험,<br><span class="r" style="position:relative;display:inline-block">치매 걸리면<i id="ul" style="position:absolute;left:0;right:0;bottom:4px;height:14px;background:#FF6B6B;opacity:.45;transform-origin:left;border-radius:8px"></i></span><br>청구를 못 합니다</h1>
 <p id="lead" style="position:absolute;left:72px;top:1150px;font-size:34px;color:#BDBDBD">보험료는 꼬박꼬박 냈는데, 정작 못 받는 이유</p>""")
# 2 왜 못 받나
S.append(f"""
 <h2>왜 <span class="r">못 받는</span> 걸까요?</h2>
 <p class="lead">치매보험은 대부분 가입한 본인이<br>직접 청구해야 하는 구조예요.</p>
 <div class="rows">
  <div class="row box"><div class="num">1</div><div><h3>가입한 사실을 잊어버려요</h3><p>치매가 오면 어떤 보험에 들었는지, 증권이 어디 있는지부터 기억하기 어려워져요.</p></div></div>
  <div class="row box"><div class="num">2</div><div><h3>청구 의사를 밝히기 어려워요</h3><p>보험금 청구는 본인 의사 확인이 원칙이라, 의사소통이 안 되면 절차가 멈춰요.</p></div></div>
  <div class="row box"><div class="num">3</div><div><h3>가족이 가도 거절될 수 있어요</h3><p>자녀라도 청구 권한이 없으면 보험사는 위임 서류를 요구해요. 못 받으면 법원에서 성년후견인으로 선임돼야 해요.</p></div></div>
 </div>
 <div class="src">참고: 금융감독원 치매보험 가입 시 유의사항</div>""")
# 3 해결책 + 통계 (움직이는 장)
S.append(f"""
 <h2>해결책은 딱 하나,<br><span class="y">지정대리청구인</span></h2>
 <p class="lead">내가 청구하기 어려워질 때를 대비해<br>대신 청구할 가족을 <b>미리 정해 두는</b> 제도예요.</p>
 <div class="stat">
  <div class="box" id="b1"><div class="k">대리청구인 지정률</div><div class="v r" id="v1">23.1%</div><div class="d">2026년 상반기<br>(2021년 26.0%에서 하락)</div></div>
  <div class="box" id="b2"><div class="k">치매보험 신규 가입</div><div class="v y" id="v2">66만 건</div><div class="d">2025년 한 해<br>(2021년 34만 건의 약 2배)</div></div>
 </div>
 <div class="box" id="b3" style="margin-top:22px"><p style="font-size:33px;color:#E0E0E0">가입은 4년 새 두 배 가까이 늘었는데, 정작 받을 준비를 해 둔 사람은 <b class="y">4명 중 1명</b>도 안 돼요.</p></div>
 <div class="rows" id="b4" style="margin-top:22px;gap:14px">
  <div class="row box" style="padding:22px 28px"><div class="num">✓</div><div><h3>지정해 두면 달라지는 것</h3><p>법원 절차 없이 가족이 서류를 갖춰 바로 청구할 수 있어요. 병원비와 간병비가 급할 때 시간을 아껴요.</p></div></div>
 </div>
 <div class="src">출처: 금융감독원 보도자료 (2026.6.30.)</div>""")
# 4 기명 vs 무기명
S.append(f"""
 <h2>2026년 7월부터<br><span class="y">훨씬 쉬워졌어요</span></h2>
 <p class="lead" style="font-size:34px">이름을 적지 않아도 되는 방식이 새로 생겼어요.</p>
 <table>
  <thead><tr><th></th><th>기명 지정</th><th class="new">무기명 지정<span class="tag">NEW</span></th></tr></thead>
  <tbody>
   <tr><th>방식</th><td>특정 가족을<br>이름으로 등록</td><td>이름 없이<br>가족관계로 지정</td></tr>
   <tr><th>누가 청구</th><td>미리 지정해 둔<br>그 사람</td><td>배우자 또는<br>직계존비속</td></tr>
   <tr><th>준비할 것</th><td>지정될 사람의<br>이름·연락처 등</td><td>개인정보 동의<br>절차 없음</td></tr>
   <tr><th>보험금 입금</th><td>보험사에<br>확인 필요</td><td>가입자 본인<br>(수익자) 계좌</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:20px;border-color:#FFE45C;padding:22px 30px"><p style="font-size:29px;color:#E0E0E0;line-height:1.42"><b class="y">고르는 기준</b><br>청구할 사람을 한 명으로 정해 두고 싶으면 기명, 서류 없이 간편하게 해 두려면 무기명이 맞아요.</p></div>
 <div class="src">출처: 금융감독원 대리청구인 지정 제도 개선 (2026.6.30.)<br>보험사별로 시행 시기가 다를 수 있어요.</div>""")
# 5 확대
S.append(f"""
 <h2>치매보험만의<br>이야기가 <span class="r">아니에요</span></h2>
 <p class="lead">갑자기 쓰러져 의식이 없을 때도<br>본인은 청구할 수 없어요.</p>
 <div class="rows">
  <div class="row box"><div class="num">암</div><div><h3>암 보험</h3><p>치료 중 의사소통이 어려워지는 경우에 대비</p></div></div>
  <div class="row box"><div class="num">뇌</div><div><h3>뇌혈관 질환 보험</h3><p>뇌졸중처럼 갑자기 의식을 잃는 경우에 대비</p></div></div>
  <div class="row box"><div class="num">심</div><div><h3>심혈관 질환 보험</h3><p>중환자실 치료 중 청구가 필요한 경우에 대비</p></div></div>
 </div>
 <div class="box" style="margin-top:22px;border-color:#FFE45C"><p style="font-size:32px;color:#E0E0E0">2026년 하반기부터 이 보험들에도 대리청구인 지정 제도가 <b class="y">순차적으로 도입</b>되고 있어요.</p></div>
 <div class="src">출처: 금융감독원 (2026.6.30.) · 도입 일정은 보험사별로 달라요.</div>""")
# 6 순서
S.append(f"""
 {bino('search', 190, '')}
 <h2>지금 바로 하는<br><span class="y">확인 순서 5단계</span></h2>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>부모님 보험 목록 확인</h3><p>'내보험찾아줌'에서 부모님 본인 인증으로 전체 조회</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>대상 보험 체크</h3><p>치매·간병, 암, 뇌·심장 보험이 있는지 표시</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">3</div><div><h3>보험사에 물어보기</h3><p>"지정대리청구인 등록돼 있나요?" 고객센터·앱 문의</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">4</div><div><h3>없으면 등록 신청</h3><p>이미 가입한 보험도 나중에 지정할 수 있어요</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">5</div><div><h3>가족에게 꼭 알리기</h3><p>지정된 사람이 모르면 소용없어요. 금감원도 권고하는 단계</p></div></div>
 </div>
 <div class="src">내보험찾아줌: cont.insure.or.kr (생명·손해보험협회 운영, 무료)</div>""")
# 7 Q&A
S.append(f"""
 <h2>많이 <span class="b">헷갈리는</span> 것들</h2>
 <div class="qa">
  <div class="box"><div class="q">오래전에 가입한 보험도 되나요?</div><div class="a">네. 기존 가입자도 보험사에 신청하면 지정할 수 있어요.</div></div>
  <div class="box"><div class="q">대리청구인이 보험금을 가져가나요?</div><div class="a">무기명 방식은 보험금이 가입자 본인(수익자) 계좌로 들어가요.</div></div>
  <div class="box"><div class="q">이미 치매 진단을 받았다면요?</div><div class="a">본인 의사 확인이 어려우면 지정이 힘들 수 있어요. 건강할 때 미리 해 두는 게 핵심이에요.</div></div>
  <div class="box"><div class="q">자녀가 여러 명이면 누가 청구하나요?</div><div class="a">기명은 지정된 한 사람, 무기명은 배우자나 직계존비속이 청구할 수 있어요.</div></div>
  <div class="box"><div class="q">추가로 돈이 드나요?</div><div class="a">지정 자체에 보험료가 더 붙는지는 상품마다 달라요. 신청 전에 보험사에 확인하세요.</div></div>
 </div>
 <div class="src">세부 절차와 서류는 보험사·상품에 따라 다를 수 있어요.</div>""")
# 8 보너스
S.append(f"""
 <h2>확인하는 김에<br><span class="y">이것도</span> 같이 보세요</h2>
 <p class="lead">주인이 안 찾아간 '숨은 보험금'이<br>이만큼 쌓여 있어요.</p>
 <div class="stat">
  <div class="box"><div class="k">숨은 보험금 규모</div><div class="v y" style="font-size:66px">10조 3천억</div><div class="d">2026년 금융위원회 안내 기준</div></div>
  <div class="box"><div class="k">찾아간 사람 평균</div><div class="v b" style="font-size:66px">404만 원</div><div class="d">2025년 청구 건당 환급액</div></div>
 </div>
 <div class="rows" style="margin-top:22px;gap:14px">
  <div class="row box" style="padding:22px 28px"><div class="num">✓</div><div><h3>부모님 보험 조회할 때 같이 떠요</h3><p>내보험찾아줌 한 번 조회로 가입 내역과 숨은 보험금을 함께 확인</p></div></div>
 </div>
 <div class="note" style="margin-top:34px;font-size:38px;align-self:flex-start">다음 노트 ②<br>숨은 보험금, 3분 만에 찾는 법</div>
 <div class="src">출처: 금융위원회 보도자료 (2026.7.8.)</div>""")
# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">이 노트,<br><span class="y">부모님께 보내 주세요</span></h2>
 <div style="display:flex;gap:28px;align-items:flex-end;margin-top:40px">
  <div class="note" style="flex:1;padding:36px 40px 40px">
   <div style="font-size:32px;margin-bottom:10px">오늘 확인할 것</div>
   <div class="ck"><span>부모님 보험 목록 조회</span><span>대리청구인 등록 여부</span><span>지정 사실 가족과 공유</span></div>
  </div>
  {bino('check', 330)}
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">저장해 두고 명절이나 부모님 댁에 갈 때 꺼내 보세요.</p><p style="font-size:30px;margin-top:10px">형제자매 단톡방에 공유하면 한 번에 정리돼요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">보장 내용과 절차는 보험사·상품·가입 시점에 따라 다를 수 있습니다.</div>""")

import pathlib as _p
_PH = (_p.Path(__file__).resolve().parents[3] / "photos/dementia/pixabay_3723548.jpg").as_uri()
COVERS = {
 "a": f"""
 <div style="position:absolute;inset:0;background:url('{_PH}') center 40%/cover;filter:grayscale(1) brightness(.62) contrast(1.15)"></div>
 <div style="position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.35),transparent 30%,transparent 45%,rgba(0,0,0,.92) 78%)"></div>
 <div style="position:absolute;left:72px;right:72px;top:860px;border-top:2px solid rgba(255,255,255,.45);padding-top:34px">
  <h1 style="font-size:84px;line-height:1.2">보험회사는 알고<br>자식들만 모르는 <span style="color:#FFB020">'이것'</span></h1>
  <p style="font-size:32px;color:#CFCFCF;margin-top:20px">부모님 치매보험, 이거 안 하면 못 받아요</p>
 </div>""",
 "b": f"""
 {bino('wow', 700, 'position:absolute;left:190px;top:90px')}
 <div style="position:absolute;left:72px;right:72px;top:840px">
  <span class="chip" style="font-size:28px;padding:8px 20px">부모님 보험 있는 분 필독</span>
  <h1 style="font-size:96px;margin-top:22px;line-height:1.14">치매보험 있는데<br><span class="r">청구를 못 한다고?</span></h1>
 </div>""",
}

# 작은 비노는 제목 오른쪽 위에 둔다
S = [s.replace('<div class="bino" style="width:190px;">', '<div class="bino mini" style="width:190px;">')
      .replace('<div class="bino" style="width:150px;top:112px">', '<div class="bino mini" style="width:150px;top:112px">') for s in S]
SLIDES = S

MOTION = {
    "1b": {"dur": 5, "still_t": 0, "js": """
window.setT=function(t){
 const bn=document.querySelector('.bino');
 bn.style.transform='translateY('+(Math.sin(t*2*Math.PI/2.5)*14)+'px) rotate('+(Math.sin(t*2*Math.PI/5)*3)+'deg)';
};"""},
    "3": {"dur": 5, "still_t": 4.5, "js": """
window.setT=function(t){
 const a=eo(c((t-0.3)/1.4)), b=eo(c((t-0.6)/1.4));
 $('#v1').textContent=(a*23.1).toFixed(1)+'%';
 $('#v2').textContent=Math.round(b*66)+'만 건';
 const p1=eb(c((t-0.1)/0.4)), p2=eb(c((t-0.4)/0.4));
 $('#b1').style.transform='scale('+(0.9+0.1*p1)+')'; $('#b2').style.transform='scale('+(0.9+0.1*p2)+')';
 const f3=eo(c((t-2.0)/0.5)), f4=eo(c((t-2.6)/0.5));
 $('#b3').style.opacity=f3; $('#b3').style.transform='translateY('+((1-f3)*30)+'px)';
 $('#b4').style.opacity=f4; $('#b4').style.transform='translateY('+((1-f4)*30)+'px)';
};"""},
}

CAPTION = """부모님 치매보험,
정작 치매에 걸리면
청구를 못 할 수 있어요 😥

치매보험은 가입한 본인이
직접 청구하는 구조라서
가입 사실을 잊으면 끝이에요

그래서 필요한 게
'지정대리청구인'
대신 청구할 가족을
미리 정해 두는 제도예요

📌 2026년 7월부터
이름 없이 가족관계만으로
지정하는 방식도 생겼어요

그런데 지정해 둔 사람은
4명 중 1명도 안 돼요
(금융감독원, 2026)

부모님 보험이 있다면
오늘 한 번만 확인해 보세요
형제자매 단톡방에 공유 👆

다음 노트 ②
숨은 보험금 3분 만에 찾는 법
팔로우하고 받아 보세요

#치매보험 #지정대리청구인 #부모님보험 #보험금청구 #보험비밀노트"""
