# 캐러셀 c11 · 사고 난 뒤 돈 노트 ① 교통사고 경상환자 8주룰, 7주 안에 낼 서류
# 커뮤니티 키워드: "8주 지나면 치료 끊기나요", "경상환자 합의금 없어졌다던데", "보험사가 8주 얘기하면서 합의하재요"
#   (보험 카페·자동차 커뮤니티의 8주룰 질문 글, 겨울 빙판길 사고철, 2026.11 조사)
#   총괄 지침 4장 '자동차 사고·과실·합의금' 아직 안 써 본 영역. 주간 plan week-2026-11-16 캐러셀 후보 1번(9점)과 같은 주제, 이번 주 plan 미배정이라 직접 선정
# 공식·교차 출처:
#  - 금융감독원 자동차보험 표준약관 개정 보도자료(KDI 경제정보센터 수록, 2026.9.3) / SBS Biz 2026.9.2 / 비즈워치 2026.9.2:
#      2026.9.10 이후 사고부터, 상해 12~14급 염좌·타박상, 1~11급 제외, 사고일부터 7주 안에 진단서·진료기록부 사본·영상CD·개인정보 동의서를 보험사에 제출,
#      보험사 → 자동차손해배상진흥원 전문의료인 검토, 요청일부터 7일 안 통보, 이의는 통보일부터 7일 안 국토부 공제분쟁조정분과위원회,
#      3~4주차·6~7주차 안내, 검토 지연 시 끝날 때까지 치료비 보험사 부담, 서류 발급비·심사 수수료 보험사 부담,
#      경상환자 향후치료비 원칙적 제외(치료 끝날 때까지 실제 치료비 보장), 9.10 이후 개정 약관 체결·보험기간 10.25 시작 계약부터
#  - 데일리메디 2026.8.4: 국무회의 의결, 9.10 시행, 임산부·영유아 제외, 지연 시 치료비 부담, 심사위원 200여 명
#  - 금융정보 콘텐츠(2026.9.17): 불인정이어도 심사 전 치료비 보상, 먼저 내고 청구, 임의 추가 자료는 본인 부담 (이의 14일·심사위원 경력은 출처 1곳이라 화면에서 뺌)
#  - SBS Biz 2026.10.8: 손해보험협회 경상환자 보상처리 피해 신고센터 10.12부터 운영
#  - 확인 안 된 것(불인정 뒤 치료비 부담 주체, 7주 놓쳤을 때 처리, 경상환자 수)은 쓰지 않음
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "사고 난 뒤 돈 노트 ①"
TOPIC = "교통사고 경상환자 8주룰: 대상 등급·7주 안 서류·자배원 7일 검토·이의 7일·향후치료비 변화·피해 신고센터"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=286235 (금융감독원 자동차보험 표준약관 개정, 2026.9.3 수록)",
           "https://biz.sbs.co.kr/amp/article/20000332265 (SBS Biz 2026.9.2: 8주룰 10일 시행, 서류·기한·이의)",
           "https://news.bizwatch.co.kr/article/finance/2026/09/02/0015 (비즈워치 2026.9.2)",
           "https://www.dailymedi.com/news/news_view.php?wr_id=939072 (데일리메디 2026.8.4: 국무회의 의결, 예외)",
           "https://kbthink.com/insurance/trend/auto-insurance-8week-rule.html (금융정보 콘텐츠 2026.9.17: 이의 14일, 비용 청구)",
           "https://biz.sbs.co.kr/amp/article/20000338974 (SBS Biz 2026.10.8: 손보협회 피해 신고센터)"]

S = []
# 1 표지 (A2: 사진 위 + 질문형 제목)
S.append(cover(layout_for(11),
               "가벼운 사고인데<br><span class=\"y\">8주</span> 지나면<br>치료 끊기나요?",
               chip="9월 10일 이후 교통사고라면",
               sub="목·허리 삐끗한 정도라면 7주차에 할 일이 있어요",
               photo="photos/car/pixabay_2942982.jpg", accent="y"))

# 2 무엇이 달라졌나 (전·후 비교표)
S.append(f"""
 <h2>뒤에서 살짝 받혔어요<br>예전과 <span class="y">뭐가 달라졌죠?</span></h2>
 <p class="lead" style="margin-top:14px">혹시 9월 10일 뒤에 난 사고인가요? 그럼 아래 오른쪽 칸이 내 이야기예요.</p>
 <table style="margin-top:26px;font-size:29px">
  <thead><tr><th style="width:24%"></th><th>예전</th><th class="new">9월 10일 사고부터</th></tr></thead>
  <tbody>
   <tr><th>치료 기간</th><td>기간 심사 없이 계속</td><td><b style="color:#fff">8주 넘기려면 심사</b></td></tr>
   <tr><th>할 일</th><td>따로 없음</td><td>사고일부터 <b style="color:#FFE45C">7주 안에</b> 서류를 보험사에 제출</td></tr>
   <tr><th>판단</th><td>보험사와 협의</td><td>자동차손해배상진흥원 전문의료인이 검토</td></tr>
   <tr><th>합의금 속<br>향후치료비</th><td>합의를 빨리 하려고 관행처럼 지급</td><td>경상환자는 원칙적으로 빠지고, 치료 끝날 때까지 <b style="color:#fff">실제 치료비</b>를 받아요</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:22px;padding:20px 30px;border-color:#FFE45C"><p style="font-size:28px;color:#E0E0E0;line-height:1.45">치료를 막는 제도는 아니에요. <b style="color:#fff">8주보다 길게 받으려면 필요하다는 걸 서류로 보여 주는</b> 절차가 생긴 거예요.</p></div>
 <div class="src">출처: 금융감독원 표준약관 개정(2026.9), SBS Biz·비즈워치(2026.9.2), 데일리메디(2026.8.4)</div>""")

# 3 나도 대상일까
S.append(f"""
 <h2>내 진단서로<br><span class="b">대상인지</span> 먼저 봐요</h2>
 <p class="lead" style="margin-top:14px">진단서에 적힌 <b>상해등급</b>과 병명이 기준이에요.</p>
 <div class="rows" style="gap:16px;margin-top:26px">
  <div class="row box" style="padding:22px 28px;border-color:#FFE45C"><div class="num">O</div><div><h3>심사 대상</h3><p>상해등급 12~14급 경상환자 중 <b style="color:#fff">염좌(삠)나 단순 타박상</b>. 목·허리를 삐끗한 흔한 사고가 여기에 들어가요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#7FB2FF">X</div><div><h3>심사 없이 계속 치료</h3><p>상해등급 1~11급 중상환자. 골절, 장기 손상처럼 더 큰 부상이에요. 예: 뇌진탕 11급, 추간판탈출증 9급.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#7FB2FF">X</div><div><h3>원칙적으로 제외</h3><p>임산부와 영유아.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#9E9E9E">-</div><div><h3>9월 10일 전에 난 사고</h3><p>예전 절차 그대로예요. 기준은 치료 시작일이 아니라 <b style="color:#fff">사고 난 날</b>이에요.</p></div></div>
 </div>
 <div class="src">출처: 금융감독원(2026.9), SBS Biz·비즈워치(2026.9.2), 데일리메디(2026.8.4). 등급은 진단 내용에 따라 달라져요.</div>""")

# 4 날짜별 타임라인 (움직이는 장)
def _t(i, wk, head, body, col="#FFE45C"):
    return f"""<div id="t{i}" style="display:flex;gap:22px;align-items:flex-start;opacity:0">
   <div style="flex:none;width:150px;text-align:right;font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:42px;color:{col};line-height:1.15;padding-top:4px">{wk}</div>
   <div style="flex:none;width:22px;height:22px;border-radius:50%;background:{col};margin-top:16px"></div>
   <div><p style="font-size:37px;color:#fff;font-weight:800;line-height:1.3">{head}</p><p style="font-size:29px;color:#BDBDBD;line-height:1.4;margin-top:4px">{body}</p></div>
  </div>"""

S.append(f"""
 <h2>사고 난 날부터<br><span class="y">달력에 적어 두세요</span></h2>
 <div style="position:relative;margin-top:30px">
  <div id="ln" style="position:absolute;left:182px;top:16px;width:4px;height:0;background:#3A3A3A"></div>
  <div style="display:flex;flex-direction:column;gap:30px">
   {_t(1, "사고일", "치료 시작", "염좌·타박상이면 8주까지는 그대로 치료", "#7FB2FF")}
   {_t(2, "3~4주", "보험사 1차 안내", "신청 시기를 놓치지 않게 알려 줘요", "#7FB2FF")}
   {_t(3, "6~7주", "보험사 2차 안내", "더 치료가 필요하면 지금 준비", "#7FB2FF")}
   {_t(4, "7주 안", "서류를 보험사에 제출", "진단서·진료기록부 사본 등 4가지", "#FFE45C")}
   {_t(5, "+7일", "검토 결과 통보", "검토 요청일부터 7일 안에 알려 줘요", "#FFE45C")}
   {_t(6, "+7일", "결과에 이의 제기", "통보받은 날부터 7일 안에 신청", "#FF6B6B")}
  </div>
 </div>
 <div class="box" id="tb" style="margin-top:34px;padding:22px 30px;border-color:#FFE45C;opacity:0"><p style="font-size:29px;color:#E0E0E0;line-height:1.45">7주는 <b style="color:#fff">병원에 처음 간 날이 아니라 사고 난 날</b>부터 세요. 병원을 늦게 갔어도 날짜는 사고일부터 흘러가요.</p></div>
 <div class="src">출처: 금융감독원(2026.9), SBS Biz·비즈워치(2026.9.2), 데일리메디(2026.8.4)</div>""")

# 5 7주 안에 낼 서류와 비용
S.append(f"""
 <h2>7주 안에 낼 서류<br><span class="y">딱 4가지</span></h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:28px">
  <div class="box" style="padding:24px 26px"><p style="font-size:24px;color:#9E9E9E;font-weight:700">1</p><p style="font-size:34px;color:#fff;font-weight:800">진단서</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">더 치료가 필요한 이유와 기간이 담겨요</p></div>
  <div class="box" style="padding:24px 26px"><p style="font-size:24px;color:#9E9E9E;font-weight:700">2</p><p style="font-size:34px;color:#fff;font-weight:800">진료기록부 사본</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">그동안 받은 치료 기록</p></div>
  <div class="box" style="padding:24px 26px"><p style="font-size:24px;color:#9E9E9E;font-weight:700">3</p><p style="font-size:34px;color:#fff;font-weight:800">영상 CD</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">엑스레이·MRI 등을 찍었다면</p></div>
  <div class="box" style="padding:24px 26px"><p style="font-size:24px;color:#9E9E9E;font-weight:700">4</p><p style="font-size:34px;color:#fff;font-weight:800">개인정보 동의서</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">수집·이용 동의</p></div>
 </div>
 <div class="box" style="margin-top:20px;padding:22px 30px;border-color:#FFE45C">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">발급비는 누가 내죠?</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">필수 서류 발급비와 심사 수수료는 <b style="color:#fff">보험사 부담</b>이에요. 병원에서 먼저 냈다면 영수증을 챙겨 보험사에 청구하면 돌려받아요.</p>
 </div>
 <div class="box" style="margin-top:14px;padding:22px 30px">
  <p style="font-size:29px;color:#fff;font-weight:800">6주차쯤 이렇게 준비해요</p>
  <p style="font-size:27px;color:#E0E0E0;line-height:1.5;margin-top:6px">① 병원에 진단서와 진료기록부 사본 요청 ② 영상 검사를 했다면 CD 발급 ③ 보상 담당자에게 내고 접수됐는지 확인</p>
 </div>
 <div class="box" style="margin-top:14px;padding:20px 30px;border-color:#FF6B6B"><p style="font-size:27px;color:#E0E0E0;line-height:1.45">필수가 아닌 자료를 스스로 더 떼서 내면 그 비용은 <b class="r">본인 부담</b>이에요.</p></div>
 <div class="src">출처: SBS Biz·비즈워치(2026.9.2), 금융정보 콘텐츠(2026.9.17). 서류는 보상을 맡은 보험사에 내요.</div>""")

# 6 결과를 기다리는 동안 / 결과가 나온 뒤
S.append(f"""
 <h2>심사가 늦어지면<br><span class="b">치료비는요?</span></h2>
 <div style="display:flex;gap:18px;margin-top:28px;align-items:stretch">
  <div class="box" style="flex:1;padding:28px 26px;border-color:#7FB2FF">
   <p style="font-size:34px;font-weight:900;color:#7FB2FF">기다리는 동안</p>
   <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:14px">기한 안에 냈는데 검토가 늦어 8주를 넘겼다면, <b style="color:#fff">심사가 끝날 때까지 치료비는 보험사가</b> 내요.</p>
   <p style="font-size:26px;color:#BDBDBD;line-height:1.45;margin-top:14px">결과가 불인정이어도 그 전까지 받은 치료비는 보상돼요.</p>
  </div>
  <div class="box" style="flex:1;padding:28px 26px;border-color:#FF6B6B">
   <p style="font-size:34px;font-weight:900;color:#FF6B6B">결과가 아쉬우면</p>
   <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:14px">통보받은 날부터 <b style="color:#fff">7일 안에</b> 국토교통부 공제분쟁조정분과위원회에 이의를 낼 수 있어요.</p>
   <p style="font-size:26px;color:#BDBDBD;line-height:1.45;margin-top:14px">이의 결과가 나올 때까지 진단서·영수증은 버리지 말고 모아 두세요.</p>
  </div>
 </div>
 <div class="box" style="margin-top:22px;padding:24px 30px">
  <p style="font-size:30px;color:#fff;font-weight:800">누가 보나요?</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">보험사가 아니라 <b style="color:#FFE45C">자동차손해배상진흥원</b>의 전문의료인이 진단서와 진료 기록을 보고 판단해요. 보험사는 서류를 넘기는 역할이에요.</p>
 </div>
 <div class="box" style="margin-top:16px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:28px;color:#E0E0E0;line-height:1.5">검토는 요청일부터 7일 안에 끝나요. <b style="color:#fff">7주 안에 서류를 내면</b> 8주가 되기 전후로 결과를 받아 볼 수 있어요.</p></div>
 <div class="src">출처: 금융감독원(2026.9), SBS Biz·비즈워치(2026.9.2), 데일리메디(2026.8.4)</div>""")

# 7 합의금 속 향후치료비
S.append(f"""
 <h2>"합의금 줄었다"는 말,<br><span class="y">이 부분</span> 이야기예요</h2>
 {bino('think', 190, 'position:absolute;right:56px;top:300px;transform:rotate(5deg)')}
 <p class="lead" style="margin-top:14px;margin-right:200px">합의금 안에는 앞으로 받을 치료비를 미리 주는 <b>향후치료비</b>가 들어 있었어요.</p>
 <div class="stat" style="margin-top:30px">
  <div class="box"><div class="k">경상환자 12~14급</div><div class="v r" style="font-size:56px">원칙적 제외</div><div class="d">대신 치료가 끝날 때까지<br>실제 치료비를 보장</div></div>
  <div class="box"><div class="k">중상환자 1~11급</div><div class="v b" style="font-size:56px">입증 시 지급</div><div class="d">앞으로 치료가 필요하고<br>비용이 의학적으로 확인될 때</div></div>
 </div>
 <div class="box" style="margin-top:22px;padding:22px 30px;border-color:#FFE45C">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">적용 시점이 따로 있어요</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">사고 날짜가 아니라 <b style="color:#fff">보험 계약</b> 기준이에요. 9월 10일 이후 개정 약관으로 맺은 계약 중 보험기간이 10월 25일부터 시작하는 계약부터예요.</p>
 </div>
 <div class="box" style="margin-top:14px;padding:20px 30px"><p style="font-size:27px;color:#E0E0E0;line-height:1.45">그래서 같은 날 난 사고라도 상대 차 보험이 언제 시작됐느냐에 따라 합의 방식이 다를 수 있어요.</p></div>
 <div class="src">출처: 금융감독원(2026.9), SBS Biz·비즈워치(2026.9.2). 실제 합의 조건은 보험사·사고마다 달라요.</div>""")

# 8 헷갈리는 질문
S.append(f"""
 <h2>많이 묻는 질문<br><span class="y">5개</span></h2>
 <div class="qa" style="gap:14px;margin-top:24px">
  <div class="box"><p class="q">8주가 되면 치료가 바로 끊기나요?</p><p class="a">심사 대상이 아니면 계속 받아요. 대상이어도 7주 안에 서류를 내면 검토 결과를 보고 정해져요.</p></div>
  <div class="box"><p class="q">8월에 난 사고인데 해당되나요?</p><p class="a">아니요. 9월 10일 이후에 발생한 사고부터 적용돼요.</p></div>
  <div class="box"><p class="q">서류는 어디에 내요?</p><p class="a">보상을 맡은 보험사에 내면, 보험사가 자동차손해배상진흥원에 넘겨요.</p></div>
  <div class="box"><p class="q">언제 내야 할지 깜빡하면요?</p><p class="a">보험사가 3~4주차, 6~7주차에 안내를 보내요. 문자와 전화를 흘려듣지 마세요.</p></div>
  <div class="box"><p class="q">보상 처리가 부당하다고 느끼면요?</p><p class="a">손해보험협회가 10월 12일부터 경상환자 보상처리 피해 신고센터를 운영하고 있어요.</p></div>
 </div>
 <div class="src">출처: 금융감독원(2026.9), SBS Biz(2026.9.2·10.8), 비즈워치(2026.9.2)</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:40px">이번 겨울 운전하는 가족에게<br><span class="y">먼저 보내 주세요</span></h2>
 <div class="note" style="margin-top:42px;padding:36px 40px 40px;margin-right:60px">
  <div style="font-size:32px;margin-bottom:10px">가벼운 교통사고 뒤 체크</div>
  <div class="ck"><span>사고 날짜 9월 10일 이후?</span><span>진단서 상해등급 확인</span><span>7주 안에 서류 4가지</span><span>결과 통보 7일 안 이의</span><span>발급비 영수증 보관</span></div>
 </div>
 <div class="box" style="margin-top:42px"><p style="font-size:34px;color:#fff;font-weight:700">"8주면 끝이래요"는 반만 맞아요</p><p style="font-size:30px;margin-top:10px">더 필요한 치료라면 기한 안에 서류로 보여 주면 돼요. 날짜만 놓치지 마세요.</p></div>
 <p style="font-size:32px;margin-top:32px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 적용 여부는 보험사 안내와 약관, 관계기관 공지를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "4": {"dur": 5, "still_t": 4.8, "js": """
window.setT=function(t){
 $('#ln').style.height=(eo(c(t/3.6))*640)+'px';
 for(let i=1;i<=6;i++){const s=0.15+(i-1)*0.45, o=c((t-s)/0.35);
  const e=$('#t'+i); e.style.opacity=o; e.style.transform='translateX('+((1-eo(o))*30)+'px)';}
 const q=c((t-3.1)/0.4); $('#tb').style.opacity=q;
};"""},
}

CAPTION = """8주 지나면 치료 끊기냐고요?
반만 맞는 이야기예요

9월 10일 이후 사고부터
염좌·타박상 경상환자는
8주 넘게 치료하려면
심사를 받아요

사고일부터 7주 안에
진단서, 진료기록부 사본
영상 CD, 동의서를
보험사에 내면 돼요

결과는 7일 안에 오고
아쉬우면 7일 안에 이의

발급비는 보험사 부담
영수증은 꼭 챙기세요

운전하는 가족에게
공유해 주세요

#교통사고 #경상환자 #8주룰
#자동차보험 #보험비밀노트"""
