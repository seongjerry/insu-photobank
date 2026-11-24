# 캐러셀 c12 · 보험료 줄이는 노트 ① 옛날 실손(1·2세대) 계약자에게 생긴 두 가지 선택
# 배정: 주간 plan week-2026-11-23 캐러셀 1번(10점), 수요일(11/25) 배정. 총괄 지침 4장 '실손 세대 전환' 아직 안 써 본 영역(캐러셀 기준)
# 커뮤니티 키워드: "옛 실손 절대 깨지 마", "옛날 실손 갈아타야 하나요", "실손보험 유지 vs 갈아타기"
#   (보험 카페·블로그의 1세대 실손 유지 고민 글, 머니투데이 2026.5.5 제목 "옛 실손 절대 깨지마?", 2026.11 조사)
# 공식·교차 출처:
#  - 금융위원회 보도자료 2026.11.19 (정책브리핑 korea.kr 148976084): 11월 23일 시행, 2013년 3월 이전 재가입 조건 없는 실손,
#      선택형 할인 3가지(근골격계 물리치료·체외충격파·비급여 주사제 / 비급여 MRI·MRA / 자기부담률 20%),
#      전환 후 3년간 5세대 보험료 50% 할인, 대상기간 내년 5월 22일까지, 별도 심사 없음, 신청 채널(홈페이지·앱·콜센터·지점·설계사),
#      60대 여성 1세대 월 17만7천원 37.0%~87.8% 절감
#  - 금융위원회 보도자료 2026.5.6 (fsc.go.kr 86831): 대상 47.5%('24년말), 3개월 내 철회 조건 없음·3개월 이후 보험사고 없으면 6개월 내 철회,
#      철회 시 재가입 제한, 보장 확대·철회 후 재전환은 심사, 가입자 65% 보험금 수령 없음·상위 10%가 74%
#  - 비즈니스워치 2026.11.19: 대상 약 1630만명, 셋 다 선택 시 1세대 약 37%·2세대 약 27%, 신청 내년 5월 22일까지,
#      2영업일 숙려·최대 6개월 철회, 신청 6개월 전부터 같은 증권 일부 해지 시 할인 미적용·중단, 19일 이전 해지 예외
#  - 딜사이트 2026.11.19(173118·173134): 176,982원 → 21,620원(87.8%), 6개 대형 손보사 기준 예시, 선택형 철회·해지 1회,
#      모집인 먼저 연락하는 전환 권유 금지, 할인 중단 조건
#  - 연합뉴스 2026.11.19(서플 수록): 1천630만명, 약 17만7천원 → 2만1천620원, 선택형 철회·해지 1회 제한, 별도 심사 없음
#  - 확인이 1곳뿐인 숫자(항목별 할인율, 2세대 예시 12만7천원, 할인 중단 시 연 26만원, 할인율 조정 ±25%)는 화면에서 뺌
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "보험료 줄이는 노트 ①"
TOPIC = "옛날 실손 두 가지 선택: 대상·선택형 할인 3가지·5세대 전환 3년 50%·마감 2027.5.22·철회·할인 끊기는 경우"
SOURCES = ["https://www.korea.kr/news/policyNewsView.do?newsId=148976084 (금융위원회 2026.11.19, 정책브리핑)",
           "https://www.fsc.go.kr/no010101/86831 (금융위원회 2026.5.6 실손 개선방안)",
           "https://news.bizwatch.co.kr/article/finance/2026/11/19/0016 (비즈니스워치 2026.11.19)",
           "https://dealsite.co.kr/articles/173118 (딜사이트 2026.11.19)",
           "https://dealsite.co.kr/articles/173134 (딜사이트 2026.11.19 할인 중단 조건)",
           "https://supple.kr/news/cmwn3psdkghjt3msx0jaerl2m (연합뉴스 2026.11.19 수록)",
           "https://www.mt.co.kr/finance/2026/05/05/2026050416165434491 (머니투데이 2026.5.5, 커뮤니티 말투 참고)"]

S = []
# 1 표지 (B2: 큰 숫자 + 비노 옆)
S.append(cover(layout_for(12),
               "\"옛 실손<br>절대 깨지 마\"<br>이제 <span class=\"y\">선택</span>이에요",
               big="87.8%", big_label="1세대 실손 월 17만7천원이 3년간 2만1,620원",
               pose="money", accent="y",
               source="11월 23일부터 옛날 실손에 두 갈래 길이 생겼어요"))

# 2 나도 대상일까
S.append(f"""
 <h2>내 실손이<br><span class="y">대상인지</span> 먼저 봐요</h2>
 <p class="lead" style="margin-top:14px">조건은 두 가지예요. 둘 다 맞아야 해요.</p>
 <div class="rows" style="gap:16px;margin-top:26px">
  <div class="row box" style="padding:24px 28px;border-color:#FFE45C"><div class="num">1</div><div><h3>2013년 3월 이전에 가입</h3><p>증권 첫 장의 계약일을 보세요. 흔히 1세대, 초기 2세대라고 부르는 실손이에요.</p></div></div>
  <div class="row box" style="padding:24px 28px;border-color:#FFE45C"><div class="num">2</div><div><h3>재가입 조건이 없는 계약</h3><p>몇 년마다 그때 파는 상품으로 바뀌는 조건(예: 5년마다 재가입)이 <b style="color:#fff">붙어 있지 않아야</b> 해요.</p></div></div>
 </div>
 <div class="stat" style="margin-top:26px">
  <div class="box"><div class="k">대상 가입자</div><div class="v y">약 1,630만</div><div class="d">명</div></div>
  <div class="box"><div class="k">전체 실손 중 비중</div><div class="v b">약 47.5%</div><div class="d">2024년 말 기준</div></div>
 </div>
 <div class="box" style="margin-top:20px;padding:20px 30px"><p style="font-size:28px;color:#E0E0E0;line-height:1.45">헷갈리면 가입한 보험사 콜센터에 <b style="color:#fff">"제 실손이 선택형 할인이나 전환 할인 대상인가요?"</b> 하고 물어보면 바로 알려 줘요.</p></div>
 <div class="src">출처: 금융위원회(2026.11.19 정책브리핑, 2026.5.6), 비즈니스워치·딜사이트·연합뉴스(2026.11.19)</div>""")

# 3 두 갈래 비교표
S.append(f"""
 <h2>두 갈래 길,<br><span class="y">한 장으로</span> 비교해요</h2>
 <table style="margin-top:26px;font-size:28px">
  <thead><tr><th style="width:22%"></th><th>A. 그대로 두고<br>보장 일부 빼기</th><th class="new">B. 5세대로<br>옮기고 할인</th></tr></thead>
  <tbody>
   <tr><th>이름</th><td>선택형 할인특약</td><td>계약전환 할인</td></tr>
   <tr><th>할인</th><td>세 가지 다 빼면<br>1세대 약 37%<br>2세대 약 27%</td><td><b style="color:#FFE45C">3년간</b> 5세대 보험료의 <b style="color:#FFE45C">50%</b></td></tr>
   <tr><th>옛 실손</th><td>그대로 유지</td><td>5세대로 바뀜</td></tr>
   <tr><th>심사</th><td>보험사에 확인</td><td>원칙적으로 없음</td></tr>
   <tr><th>신청 마감</th><td>마감일 안내 없음</td><td><b style="color:#fff">2027년 5월 22일</b>까지<br>(이후 연장 검토)</td></tr>
   <tr><th>되돌리기</th><td>철회·해지는 <b style="color:#fff">딱 1번</b></td><td>최대 6개월 안 철회<br>대신 할인은 다시 못 써요</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:26px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:29px;color:#E0E0E0;line-height:1.5">A는 <b style="color:#fff">옛 실손을 지키는 길</b>, B는 <b style="color:#fff">보험료를 크게 줄이는 대신 보장 구조가 바뀌는 길</b>이에요. 둘 다 안 하고 그대로 두는 것도 선택이에요.</p></div>
 <div class="src">출처: 금융위원회(2026.11.19, 2026.5.6), 비즈니스워치·딜사이트·연합뉴스(2026.11.19). 할인율은 보험사·상품마다 달라요.</div>""")

# 4 숫자로 보면 (움직이는 장)
def _bar(i, label, val, w, col, note):
    return f"""<div style="margin-top:30px">
   <div style="display:flex;justify-content:space-between;align-items:baseline"><p style="font-size:32px;color:#fff;font-weight:800">{label}</p><p id="v{i}" style="font-family:Kkakdugi,Paperlogy;font-size:50px;font-weight:700;color:{col};opacity:0">{val}</p></div>
   <div style="height:58px;background:#1C1C1C;border:2px solid #2E2E2E;border-radius:14px;margin-top:10px;overflow:hidden"><div id="b{i}" data-w="{w}" style="height:100%;width:0;background:{col};border-radius:12px"></div></div>
   <p style="font-size:26px;color:#BDBDBD;margin-top:8px">{note}</p>
  </div>"""

S.append(f"""
 <h2>60대 여성, 1세대라면<br><span class="y">이만큼</span> 달라져요</h2>
 <p class="lead" style="margin-top:14px">정부가 대형 손해보험사 6곳 기준으로 든 예시예요.</p>
 {_bar(1, "지금 옛 실손", "17만7천원", 100, "#9E9E9E", "월 176,982원. 그대로 유지할 때")}
 {_bar(2, "A. 선택형 세 가지 다", "약 37%↓", 63, "#7FB2FF", "옛 실손은 남기고 보장 세 가지를 빼는 대신")}
 {_bar(3, "B. 5세대 전환 할인", "2만1,620원", 12.2, "#FFE45C", "87.8% 줄어든 금액. 할인은 3년 동안만")}
 <div class="box" id="tb" style="margin-top:34px;padding:22px 30px;border-color:#FF6B6B;opacity:0"><p style="font-size:28px;color:#E0E0E0;line-height:1.45">3년이 지나면 그때의 <b style="color:#fff">5세대 보험료를 할인 없이</b> 내요. 그리고 B는 보장 내용 자체가 바뀌는 길이라, 금액만 보고 고르면 안 돼요.</p></div>
 <div class="src">출처: 금융위원회(2026.11.19 정책브리핑), 딜사이트·연합뉴스(2026.11.19). 내 보험료는 나이·상품·보험사마다 달라요.</div>""")

# 5 A 선택형 할인특약
S.append(f"""
 <h2>A. 옛 실손 그대로,<br><span class="b">빼는 보장 세 가지</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#7FB2FF">1</div><div><h3>도수치료 같은 근골격계 물리치료, 체외충격파, 비급여 주사</h3><p>허리·어깨로 병원 다니며 자주 받는 치료들이에요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#7FB2FF">2</div><div><h3>비급여 MRI·MRA</h3><p>건강보험이 안 되는 MRI 검사비 보장을 빼요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#7FB2FF">3</div><div><h3>자기부담률 20% 적용</h3><p>병원비 중 내가 내는 몫을 20%로 정하고 보험료를 줄여요.</p></div></div>
 </div>
 <div class="box" style="margin-top:20px;padding:22px 30px;border-color:#FFE45C">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">이런 분께 맞아요</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">옛 실손의 넓은 보장은 지키고 싶은데, 위 치료는 거의 안 받는 분. 하나만 골라도 되고, <b style="color:#fff">셋 다 고르면 할인이 가장 커요.</b></p>
 </div>
 <div class="box" style="margin-top:14px;padding:20px 30px;border-color:#FF6B6B"><p style="font-size:27px;color:#E0E0E0;line-height:1.45">철회·해지는 <b class="r">한 번만</b> 할 수 있고, 빼 둔 보장 중 일부만 되살릴 수는 없어요. 상품에 따라 고를 수 없는 경우도 있어요.</p></div>
 <div class="src">출처: 금융위원회(2026.11.19), 비즈니스워치·딜사이트·연합뉴스(2026.11.19). 보험사·상품에 따라 다를 수 있어요.</div>""")

# 6 B 5세대 전환 할인
S.append(f"""
 <h2>B. 5세대로 옮기면<br><span class="y">달라지는 것</span></h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:26px">
  <div class="box" style="padding:24px 26px"><p style="font-size:25px;color:#9E9E9E;font-weight:700">할인</p><p style="font-size:34px;color:#FFE45C;font-weight:900;margin-top:4px">3년간 50%</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">5세대 보험료 기준</p></div>
  <div class="box" style="padding:24px 26px"><p style="font-size:25px;color:#9E9E9E;font-weight:700">심사</p><p style="font-size:34px;color:#fff;font-weight:900;margin-top:4px">원칙적으로 없음</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">보장을 넓히면 심사</p></div>
  <div class="box" style="padding:24px 26px"><p style="font-size:25px;color:#9E9E9E;font-weight:700">어디로</p><p style="font-size:34px;color:#fff;font-weight:900;margin-top:4px">지금 보험사의 5세대</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">앱·콜센터·지점에서 신청</p></div>
  <div class="box" style="padding:24px 26px"><p style="font-size:25px;color:#9E9E9E;font-weight:700">마감</p><p style="font-size:34px;color:#fff;font-weight:900;margin-top:4px">2027.5.22</p><p style="font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.4">이후 연장 여부 검토</p></div>
 </div>
 <div class="box" style="margin-top:18px;padding:22px 30px;border-color:#7FB2FF">
  <p style="font-size:30px;color:#7FB2FF;font-weight:800">보장은 이렇게 바뀌어요</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">중증 질환 치료비는 충분히 보장하는 쪽이고, <b style="color:#fff">중증이 아닌 비급여 치료</b>는 내가 내는 몫이 커지는 구조예요.</p>
 </div>
 <div class="box" style="margin-top:14px;padding:22px 30px;border-color:#FFE45C">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">후회되면 되돌릴 수 있나요?</p>
  <p style="font-size:27px;color:#E0E0E0;line-height:1.5;margin-top:6px">신청 뒤 2영업일 숙려기간이 있고, <b style="color:#fff">3개월 안에는 조건 없이</b>, 6개월까지는 그동안 보험금 받을 일이 없었다면 철회돼요. 철회하면 할인은 다시 못 써요.</p>
 </div>
 <div class="src">출처: 금융위원회(2026.11.19, 2026.5.6), 비즈니스워치·딜사이트·연합뉴스(2026.11.19)</div>""")

# 7 누구에게 맞을까
S.append(f"""
 <h2>그래서 나는<br><span class="y">어느 쪽일까요?</span></h2>
 {bino('check', 190, 'position:absolute;right:56px;top:150px;transform:rotate(6deg)')}
 <div class="stat" style="margin-top:26px;margin-right:0">
  <div class="box"><div class="k">실손 가입자 중</div><div class="v y">65%</div><div class="d">보험금 없이<br>보험료만 냈어요</div></div>
  <div class="box"><div class="k">보험금을 많이 받은 상위 10%가</div><div class="v r">74%</div><div class="d">전체 보험금 중<br>이만큼을 받았어요</div></div>
 </div>
 <div class="rows" style="gap:14px;margin-top:24px">
  <div class="row box" style="padding:20px 26px"><div class="num" style="background:#9E9E9E">0</div><div><h3>그대로 유지</h3><p>지병으로 병원을 자주 다니고, 지금 보험료가 크게 부담되지 않는 분</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num" style="background:#7FB2FF">A</div><div><h3>선택형 할인특약</h3><p>옛 보장은 지키되 도수치료·MRI는 거의 안 받는 분</p></div></div>
  <div class="row box" style="padding:20px 26px;border-color:#FFE45C"><div class="num">B</div><div><h3>5세대 전환 할인</h3><p>병원 갈 일이 적고 보험료 부담을 확 줄이고 싶은 분</p></div></div>
 </div>
 <div class="src">출처: 금융위원회(2026.5.6, 14개사 2025년 말 기준), 딜사이트(2026.11.19). 내 상황에 맞는지는 보험사 안내로 꼭 확인하세요.</div>""")

# 8 헷갈리는 질문
S.append(f"""
 <h2>신청 전에 많이 묻는<br><span class="y">질문 5개</span></h2>
 <div class="qa" style="gap:14px;margin-top:24px">
  <div class="box"><p class="q">같은 증권의 다른 특약을 정리해도 되나요?</p><p class="a">전환 신청 6개월 전부터 할인 기간 동안 같은 증권의 보장을 해지·감액하면 할인이 안 되거나 끊길 수 있어요. 11월 19일 전에 정리한 건 괜찮아요.</p></div>
  <div class="box"><p class="q">설계사가 먼저 전화해서 갈아타래요</p><p class="a">먼저 연락해서 전환을 권하는 영업은 금지예요. 궁금하면 내가 가입한 보험사에 직접 물어보세요.</p></div>
  <div class="box"><p class="q">철회했다가 다시 전환할 수 있나요?</p><p class="a">할 수는 있지만 이때는 심사를 받고, 할인은 다시 못 받아요.</p></div>
  <div class="box"><p class="q">5월 22일이 지나면 끝인가요?</p><p class="a">신청은 2027년 5월 22일까지예요. 연장은 그 뒤에 검토해요.</p></div>
  <div class="box"><p class="q">3년 할인이 끝나면요?</p><p class="a">그때 적용되는 5세대 보험료를 할인 없이 내요.</p></div>
 </div>
 <div class="src">출처: 금융위원회(2026.11.19, 2026.5.6), 비즈니스워치·딜사이트·연합뉴스(2026.11.19)</div>""")

# 9 마무리 (이번 주 문장 흐름 실험: 표지 숫자의 답을 한 문장으로 다시 말하고 끝냄)
S.append(f"""
 <h2 style="margin-top:36px">87.8%는<br><span class="y">3년 동안, 보장이 바뀐 값</span>이에요</h2>
 <div class="note" style="margin-top:40px;padding:36px 40px 40px;margin-right:60px">
  <div style="font-size:32px;margin-bottom:10px">옛날 실손 점검 순서</div>
  <div class="ck"><span>계약일 2013년 3월 이전?</span><span>재가입 조건 없는지 확인</span><span>도수치료·MRI 자주 받나?</span><span>A·B 보험료 보험사에 문의</span><span>B 마감 2027.5.22</span></div>
 </div>
 <div class="box" style="margin-top:40px"><p style="font-size:34px;color:#fff;font-weight:700">"절대 깨지 마"도, "무조건 갈아타"도 아니에요</p><p style="font-size:30px;margin-top:10px">내 병원 이용과 보험료를 놓고 세 길 중 하나를 고르는 거예요.</p></div>
 <p style="font-size:32px;margin-top:30px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 조건과 보험료는 가입한 보험사 안내와 약관을 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "4": {"dur": 5, "still_t": 4.8, "js": """
window.setT=function(t){
 for(let i=1;i<=3;i++){const s=0.2+(i-1)*0.8, o=c((t-s)/1.0);
  const b=$('#b'+i); b.style.width=(eo(o)*parseFloat(b.dataset.w))+'%';
  $('#v'+i).style.opacity=c((t-s-0.6)/0.3);}
 $('#tb').style.opacity=c((t-3.0)/0.5);
};"""},
}

CAPTION = """옛 실손 절대 깨지 말라고요?
11월 23일부터 길이 두 개
더 생겼어요

A. 그대로 두고 보장 빼기
도수치료·MRI 등을 빼면
1세대 약 37% 할인

B. 5세대로 옮기고 할인
3년간 보험료 50% 할인
마감은 2027년 5월 22일

60대 여성 1세대 예시
월 17만7천원이 2만1,620원
단, 3년 동안만이고
보장도 바뀌어요

2013년 3월 전 실손이면
부모님 증권부터 봐 주세요

#실손보험 #1세대실손
#5세대실손 #보험료절약
#보험비밀노트"""
