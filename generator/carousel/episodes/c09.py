# 캐러셀 c09 · 몰라서 못 받는 보험금 ③ 보험료 0원, 나도 모르게 가입된 동네 보험 (시민안전보험)
# 커뮤니티 키워드: "시민안전보험 이런 게 있는 줄 몰랐어요", "버스에서 넘어졌는데 구청 보험으로 치료비 받았대요"
#   (지역 카페·블로그 후기, 헤럴드경제 "개한테 물려도 보험금" 2026.1, 다음 짠테크 "대부분이 모르는 공짜 보험" 2026.7 화제)
#   총괄 지침 4장 '아직 안 써 본 영역: 지자체 시민안전보험' (11월 17일 추가), 주간 캐러셀 후보 2번(9점)
# 공식·교차 출처:
#  - 금융감독원 시민안전보험 안내 2026.11.2 (KDI 경제정보센터 수록) / 경향신문 2026.11.1 / 한국강사신문 2026.11.1:
#      주민등록하면 자동 가입, 자동 지급 아님·직접 청구, 사고일부터 3년, 사고 당시 주소지 기준, 광역·기초 모두 청구·일부 담보 중복,
#      다른 지역 사고도 보장 대상이면 지급, 보험기간 끝나도 청구기간 남으면 청구, 총 보상한도 소진 시 보장 종료, 재난보험24 조회
#  - 서울시 안전누리집(시민안전보험 Q&A·2026 개편, 2026.9.30 수정) / SBS Biz 2026.7.21 / 트윅24 2026.1.9:
#      보장 금액표, 지반침하 신설 최대 2,500만 원, 화재·폭발·붕괴 2,500만 원 상향, 2020~2025 598건 46억 원, 등록외국인 포함,
#      개인 보험과 관계없이 중복 지급, 자치구 보험(개물림·자전거·보행 중 사고 등) 중복, 청구 서류, 후유장해 진단일부터 3년
#  - 구리시 시민안전보험 안내: 상해의료비 최대 30만 원은 실손보험 가입자 제외 (실손형 담보는 중복이 안 될 수 있는 예)
#  - 프레시안 2026.10.19 (지급이 많은 항목: 상해의료비, 화상, 자전거, 개 물림) / 부천시 안내 보도(개 물림 응급실 치료비): 항목 예시로만 사용, 건수는 미사용
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "몰라서 못 받는 보험금 ③"
TOPIC = "보험료 0원, 주민등록만 하면 가입되는 시민안전보험 조회·청구 순서·3년 기한·광역 기초 중복"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=288882 (금융감독원 2026.11.2 시민안전보험 안내)",
           "https://khan.co.kr/article/202611011555001 (경향신문 2026.11.1)",
           "https://www.koreancenter.or.kr/news/articleView.html?idxno=1432916 (한국강사신문 2026.11.1, 중복보장 예시)",
           "https://news.seoul.go.kr/safe/insurance-qna (서울시 시민안전보험 Q&A: 금액표·서류·중복)",
           "https://news.seoul.go.kr/safe/archives/517277 (서울시 2026 개편: 지반침하 신설, 598건 46억 원)",
           "https://biz.sbs.co.kr/amp/article/20000323519 (SBS Biz 2026.7.21: 598건 46억 원, 자치구 보험 중복)",
           "https://www.twig24.com/news/local_govern/news_local/2026/01/09/20260109500135 (2026.1.9 지반침하 2,500만 원)",
           "https://www.guri.go.kr/www/contents.do?key=5342 (구리시: 상해의료비 실손 가입자 제외)",
           "https://www.pressian.com/pages/articles/2026101911435951073 (프레시안 2026.10.19, 지급 많은 항목 참고용)"]

S = []
# 1 표지 (A1: 사진 전면 + 하단 제목)
S.append(cover(layout_for(9),
               "보험료 0원인데<br>나도 모르게<br><span class=\"y\">가입된 보험</span>이 있대요",
               chip="우리 동네 시민안전보험",
               photo="photos/housing/pixabay_3671495.jpg", accent="y"))

# 2 이런 일 있었나요 (상황 카드)
def _case(tag, h, p, col="#FFE45C"):
    return f"""<div class="box" style="padding:20px 28px;display:flex;gap:22px;align-items:center">
   <div style="flex:none;width:150px;font-size:25px;font-weight:800;color:{col};line-height:1.3">{tag}</div>
   <div><h3 style="font-size:33px;font-weight:800;color:#fff;line-height:1.3">{h}</h3><p style="font-size:27px;color:#BDBDBD;line-height:1.4;margin-top:4px">{p}</p></div>
  </div>"""

S.append(f"""
 <h2>이런 일 겪었다면<br><span class="y">동네 보험</span>부터 보세요</h2>
 <div style="display:flex;flex-direction:column;gap:13px;margin-top:28px">
  {_case("대중교통", "퇴근길 버스에서 내리다 넘어졌어요", "버스·지하철 이용 중 다쳤을 때 보장하는 곳이 많아요")}
  {_case("화재·폭발", "옆집 불이 번져 다쳤어요", "사망·후유장해를 보장해요. 서울은 최대 2,500만 원")}
  {_case("개 물림", "산책길에 개에 물렸어요", "응급실 치료비를 주는 시·구가 있어요", "#7FB2FF")}
  {_case("스쿨존", "아이가 학교 앞에서 차에 부딪혔어요", "부상 등급에 따라 치료비를 줘요", "#7FB2FF")}
  {_case("자전거", "자전거 타다 넘어져 크게 다쳤어요", "자전거 사고를 따로 보장하는 곳도 있어요", "#7FB2FF")}
 </div>
 <div class="box" style="margin-top:18px;padding:20px 30px;border-color:#FF6B6B"><p style="font-size:30px;color:#fff;font-weight:700;line-height:1.45">보험료는 시·군·구가 내요. 그런데 <span class="r">알아서 주지는 않아요.</span></p></div>
 <div class="src">출처: 금융감독원(2026.11.2), 서울시 시민안전보험 안내, SBS Biz(2026.7.21), 프레시안(2026.10.19). 보장 항목은 지역마다 달라요.</div>""")

# 3 핵심 숫자 (움직이는 장)
S.append(f"""
 <h2>시민안전보험,<br><span class="y">이 세 가지</span>만 기억하세요</h2>
 <div class="stat" style="margin-top:32px">
  <div class="box" id="k1" style="opacity:0"><div class="k">내는 보험료</div><div class="v y"><span id="v1">0</span>원</div><div class="d">시·군·구가<br>전액 부담</div></div>
  <div class="box" id="k2" style="opacity:0"><div class="k">가입 방법</div><div class="v b" style="font-size:72px">자동</div><div class="d">주민등록만<br>돼 있으면 끝</div></div>
  <div class="box" id="k3" style="opacity:0"><div class="k">청구 기한</div><div class="v r"><span id="v3">0</span>년</div><div class="d">사고일 또는<br>장해 진단일부터</div></div>
 </div>
 <div class="box" id="warn" style="margin-top:26px;padding:24px 32px;border-color:#FF6B6B;opacity:0">
  <p style="font-size:34px;color:#fff;font-weight:800;line-height:1.4">가입은 자동, <span class="r">지급은 자동이 아니에요</span></p>
  <p style="font-size:28px;color:#BDBDBD;line-height:1.45;margin-top:8px">다친 사람이나 유가족이 보험사에 직접 청구해야 받아요. 몰라서 3년이 지나면 받을 길이 없어요.</p>
 </div>
 <div class="box" id="seoul" style="margin-top:16px;padding:24px 32px;opacity:0">
  <p style="font-size:27px;color:#9E9E9E;font-weight:700">서울시가 2020년부터 지난해까지 지급한 돈</p>
  <p style="margin-top:6px;line-height:1.1"><span style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:76px;color:#FFE45C"><span id="v4">0</span>억 원</span><span style="font-size:32px;color:#E0E0E0;margin-left:16px">· <span id="v5">0</span>건</span></p>
  <p style="font-size:26px;color:#BDBDBD;margin-top:8px">서울에 사는 사람 수를 생각하면 적은 숫자예요.</p>
 </div>
 <p style="font-size:28px;color:#BDBDBD;margin-top:20px;line-height:1.45">이사하면 전 지역 보험은 자동으로 끝나고, 새 주소지에 보험이 있으면 그쪽으로 바뀌어요. 그래서 <b style="color:#fff">다친 날 주소</b>가 중요해요.</p>
 <div class="src">출처: 금융감독원(2026.11.2), 경향신문(2026.11.1), 서울시 안전누리집(2026 개편)·Q&A, 구리시 안내, SBS Biz(2026.7.21)</div>""")

# 4 금액표 (서울 예시)
S.append(f"""
 <h2>얼마나 받나요?<br><span class="y">서울시 2026년</span> 예시</h2>
 <table style="font-size:28px;line-height:1.38;margin-top:24px">
  <thead><tr><th style="width:44%">사고</th><th class="new">사망 (원)</th><th>후유장해 (원)</th></tr></thead>
  <tbody>
   <tr><th style="color:#fff;width:auto">화재·폭발·붕괴<span class="tag">상향</span></th><td class="y" style="color:#FFE45C;font-weight:800">2,500만</td><td>최대 2,500만</td></tr>
   <tr><th style="color:#fff">지반침하(땅 꺼짐)<span class="tag">신설</span></th><td style="color:#FFE45C;font-weight:800">2,500만</td><td>최대 2,500만</td></tr>
   <tr><th style="color:#fff">대중교통 이용 중</th><td style="font-weight:800">2,000만</td><td>최대 2,000만</td></tr>
   <tr><th style="color:#fff">자연재해</th><td style="font-weight:800">2,000만</td><td>최대 1,000만</td></tr>
   <tr><th style="color:#fff">사회재난<br><span style="font-size:22px;color:#9E9E9E">감염병 제외</span></th><td style="font-weight:800">2,000만</td><td>최대 1,000만</td></tr>
   <tr><th style="color:#fff">스쿨존 교통사고<br><span style="font-size:22px;color:#9E9E9E">만 12세 이하</span></th><td colspan="2">부상 등급(1~14급)에 따라 최대 1,000만</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:22px;padding:20px 30px;border-color:#FFE45C"><p style="font-size:28px;color:#E0E0E0;line-height:1.45">여기에 <b class="y">구민안전보험</b>이 따로 있어요. 서울 자치구들은 개 물림, 자전거, 보행 중 사고 같은 항목을 더 보장해요.</p></div>
 <div class="src">출처: 서울시 시민안전보험 Q&A·2026 개편 안내, 트윅24(2026.1.9), SBS Biz(2026.7.21). 다른 지역은 항목·금액이 달라요.</div>""")

# 5 두 곳에서 받는다 (좌우 분할, 이번 주 디자인 실험 적용)
S.append(f"""
 <h2>한 번 다쳤는데<br><span class="b">두 곳</span>에 청구할 수 있어요</h2>
 <p class="lead" style="margin-top:14px">사고 당시 주소지의 <b>시·도</b>와 <b>시·군·구</b>가 각각 보험을 들어요.</p>
 <div style="display:flex;gap:18px;margin-top:28px;align-items:stretch">
  <div class="box" style="flex:1;text-align:center;padding:28px 18px;border-color:#FFE45C">
   <p style="font-size:28px;color:#9E9E9E;font-weight:700">광역</p>
   <p style="font-size:46px;color:#FFE45C;font-weight:900;margin-top:4px">A시 보험</p>
   <p style="font-size:27px;color:#BDBDBD;margin-top:10px;line-height:1.4">시청이 든 보험<br>사망보험금 청구</p>
  </div>
  <div style="flex:none;align-self:center;font-family:Kkakdugi,Paperlogy;font-size:72px;color:#fff;font-weight:700">+</div>
  <div class="box" style="flex:1;text-align:center;padding:28px 18px;border-color:#7FB2FF">
   <p style="font-size:28px;color:#9E9E9E;font-weight:700">기초</p>
   <p style="font-size:46px;color:#7FB2FF;font-weight:900;margin-top:4px">B구 보험</p>
   <p style="font-size:27px;color:#BDBDBD;margin-top:10px;line-height:1.4">구청이 든 보험<br>사망보험금 또 청구</p>
  </div>
 </div>
 <p style="font-size:27px;color:#BDBDBD;margin-top:14px;line-height:1.45">금감원 예시: A시 B구 주민이 화재로 사망하면 A시와 B구에 각각 사망보험금을 청구할 수 있어요.</p>
 <div class="box" style="margin-top:20px;padding:20px 30px">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">내 실손·상해보험과도 별개예요</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.45;margin-top:6px">정해진 금액을 주는 담보는 개인 보험과 상관없이 받을 수 있어요. 서울시도 개인 보험과 관계없이 중복 지급한다고 안내해요.</p>
 </div>
 <div class="box" style="margin-top:13px;padding:20px 30px;border-color:#FF6B6B">
  <p style="font-size:30px;color:#FF6B6B;font-weight:800">단, 치료비를 채워 주는 담보는 예외</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.45;margin-top:6px">예를 들어 상해의료비(최대 30만 원)를 실손보험 가입자에게는 주지 않는 시도 있어요.</p>
 </div>
 <div class="src">출처: 금융감독원(2026.11.2), 한국강사신문(2026.11.1), 서울시 Q&A, 구리시 안내. 일부 담보만 중복돼요.</div>""")

# 6 조회·청구 순서
S.append(f"""
 <h2>찾고 청구하는<br><span class="y">순서 5단계</span></h2>
 <div class="rows" style="gap:11px;margin-top:22px">
  <div class="row box" style="padding:15px 26px"><div class="num">1</div><div><h3>사고 날 주소부터 확인</h3><p>지금 집이 아니라 다친 날 주민등록이 있던 시·구가 기준이에요.</p></div></div>
  <div class="row box" style="padding:15px 26px"><div class="num">2</div><div><h3>재난보험24에서 조회</h3><p>ins24.go.kr 시민안전보험 조회에서 지역·연도를 골라요.</p></div></div>
  <div class="row box" style="padding:15px 26px"><div class="num">3</div><div><h3>시·구청 누리집에서 보장 확인</h3><p>항목·금액·보험사 연락처가 있어요. 시·도와 시·구 둘 다요.</p></div></div>
  <div class="row box" style="padding:15px 26px"><div class="num">4</div><div><h3>서류 챙기기</h3><p>청구서, 주민등록등본, 통장·신분증 사본에 사고별 서류를 더해요.</p></div></div>
  <div class="row box" style="padding:15px 26px"><div class="num">5</div><div><h3>보험사에 직접 청구</h3><p>지자체와 계약한 보험사에 내요. 사고일부터 3년 안이에요.</p></div></div>
 </div>
 <div class="box" style="margin-top:20px;padding:20px 30px;border-color:#FFE45C"><p style="font-size:28px;color:#E0E0E0;line-height:1.45"><b class="y">작년·재작년 사고라면</b> 조회할 때 사고 난 해를 고르세요. 그해 보험기간이 끝났어도 3년이 안 지났으면 청구할 수 있어요.</p></div>
 <div class="src">출처: 금융감독원(2026.11.2), 경향신문(2026.11.1), 한국강사신문(2026.11.1), 서울시 Q&A</div>""")

# 7 사고별 서류 (서울 기준)
S.append(f"""
 <h2>사고별로 <span class="b">더 챙길 서류</span></h2>
 <p class="lead" style="margin-top:14px">서울시 안내 기준이에요. 다른 지역도 비슷하게 요구해요.</p>
 <div class="box" style="margin-top:24px;padding:22px 30px;border-color:#FFE45C">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">공통</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">보험금 청구서, 개인(신용)정보처리동의서, 주민등록등본(초본), 통장 사본, 신분증 사본</p>
 </div>
 <div class="box" style="margin-top:13px;padding:22px 30px">
  <p style="font-size:30px;color:#fff;font-weight:800">후유장해</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">장해율(%)이 적힌 후유장해 진단서, 요청 시 사고 사실 확인 서류</p>
 </div>
 <div class="box" style="margin-top:13px;padding:22px 30px">
  <p style="font-size:30px;color:#fff;font-weight:800">스쿨존 교통사고</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">경찰서 교통사고 사실 확인원, 부상 등급이 적힌 보험사 지급결의서 또는 진단서</p>
 </div>
 <div class="box" style="margin-top:13px;padding:22px 30px">
  <p style="font-size:30px;color:#fff;font-weight:800">사망</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">사망진단서(사체검안서), 경찰서·소방서 사고 사실 확인서, 가족관계·기본·혼인관계증명서</p>
 </div>
 <div class="box" style="margin-top:13px;padding:22px 30px;border-color:#7FB2FF">
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5"><b style="color:#7FB2FF">미성년 자녀가 다쳤다면</b> 가족관계증명서와 보호자 통장·신분증 사본을 더해요.</p>
 </div>
 <div class="src">출처: 서울시 시민안전보험 Q&A. 지역·보험사에 따라 추가 서류가 있을 수 있어요.</div>""")

# 8 Q&A
S.append(f"""
 <h2>헷갈리는 질문<br><span class="y">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:22px;gap:12px">
  <div class="box"><div class="q">그 뒤에 이사했어요</div><div class="a">사고 날 주소지 보험으로 청구해요. 지금 사는 곳 보험이 아니에요.</div></div>
  <div class="box"><div class="q">여행 가서 다른 지역에서 다쳤어요</div><div class="a">보장 대상 사고라면 사고 장소와 상관없이 받을 수 있어요.</div></div>
  <div class="box"><div class="q">재작년 사고인데 보험기간이 끝났대요</div><div class="a">보험기간이 끝나도 3년 청구 기간이 남아 있으면 청구할 수 있어요.</div></div>
  <div class="box"><div class="q">천천히 해도 되죠?</div><div class="a">일부 담보는 그해 총 보상한도를 다 쓰면 보험기간 중에도 끝나요. 생각났을 때 바로 하세요.</div></div>
  <div class="box"><div class="q">외국인 배우자도 되나요?</div><div class="a">서울처럼 등록외국인을 포함하는 곳이 있어요. 사는 지역 안내를 확인해 보세요.</div></div>
 </div>
 <div class="src">출처: 금융감독원(2026.11.2), 경향신문(2026.11.1), 서울시 Q&A·SBS Biz(2026.7.21)</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:40px">최근 3년 안에 다친 가족에게<br><span class="y">먼저 보내 주세요</span></h2>
 <div class="note" style="margin-top:42px;padding:36px 40px 40px;margin-right:150px">
  <div style="font-size:32px;margin-bottom:10px">동네 보험 확인 체크</div>
  <div class="ck"><span>다친 날 주소지 확인</span><span>재난보험24에서 조회</span><span>시·도, 시·구 둘 다 보기</span><span>3년 안 지났는지</span><span>보험사에 직접 청구</span></div>
 </div>
 {bino('wow', 250, 'position:absolute;right:52px;top:560px;transform:rotate(6deg)')}
 <div class="box" style="margin-top:42px"><p style="font-size:34px;color:#fff;font-weight:700">"그런 보험이 있는 줄 몰랐어요"</p><p style="font-size:30px;margin-top:10px">보험료를 안 내니 모르고 지나가기 쉬워요. 부모님 사고도 같이 떠올려 보세요.</p></div>
 <p style="font-size:32px;margin-top:32px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 보장은 지자체 안내와 보험 약관을 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4.5, "still_t": 4.2, "js": """
window.setT=function(t){
 for(let i=1;i<=3;i++){const p=eb(c((t-0.2-i*0.35)/0.5)), o=c((t-0.2-i*0.35)/0.3);
  const k=$('#k'+i); k.style.opacity=o; k.style.transform='translateY('+((1-p)*40)+'px)';}
 $('#v3').textContent=Math.round(3*eo(c((t-1.2)/0.8)));
 const w=c((t-1.9)/0.4); $('#warn').style.opacity=w; $('#warn').style.transform='scale('+(0.96+0.04*eo(w))+')';
 const s=c((t-2.4)/0.4); $('#seoul').style.opacity=s;
 const q=eo(c((t-2.5)/1.2)); $('#v4').textContent=Math.round(46*q); $('#v5').textContent=Math.round(598*q);
};"""},
}

CAPTION = """보험료를 한 번도 안 냈는데
가입돼 있는 보험이 있어요

주민등록만 돼 있으면
시·군·구가 대신 들어 둔
시민안전보험이에요

👉 버스에서 넘어졌을 때
👉 화재·땅 꺼짐 사고
👉 개 물림, 스쿨존 사고
(지역마다 항목이 달라요)

자동 가입이지만
자동 지급은 아니에요
사고일부터 3년 안에
직접 청구해야 받아요

시·도와 시·구에
두 번 청구되는 경우도 있어요

최근 다친 가족에게
공유해 주세요

#시민안전보험 #숨은보험금
#재난보험24 #생활정보 #보험비밀노트"""
