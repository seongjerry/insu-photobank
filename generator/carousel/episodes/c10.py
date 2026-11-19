# 캐러셀 c10 · 사회초년생 돈 노트 ① 첫 차 보험료, 엄마 보험에 이름 올려 둔 3년이 경력이 된다
# 커뮤니티 키워드: "첫 차 보험료 200만원 넘게 나왔어요", "사회초년생 자동차보험 왜 이렇게 비싸요", "군 운전병 경력 보험 할인 되나요"
#   (자동차 커뮤니티·지식iN형 질문, 첫 차 보험료 블로그 글 반복, 2026.11 조사)
#   주간 plan week-2026-11-16 캐러셀 후보 3번(9점, 본부장님 선택, 금요일 배정). 총괄 지침 4장 '사회초년생 첫 차 보험료(11월 17일 추가)' 새 영역
# 공식·교차 출처:
#  - 금융감독원 청년 자동차보험 가입 절차 개선 2026.11 (KDI 경제정보센터 수록 2026.11.3) / SBS Biz 2026.11.2 / 연합뉴스(한민족센터) 2026.11.2 /
#    시대 2026.11.2 / 스마트투데이 2026.11.2 / 비즈워치 2026.11.7 / 위키트리 2026.11.3:
#      28세·아반떼 차량가액 2,000만원 예시, 엄마 보험 종피보험자 3년 무사고 → 133만497원에서 71만6,582원(약 61만원, 46.1%),
#      군 운전병 1년6개월+장기렌터카 1년6개월 → 94만6,300원(28.9%), 경력 없이 본인·연령 한정 특약 → 247만3,489원에서 133만497원(46.2%, 약 114만원),
#      경력 최대 3년, 최근 3년 사고 있으면 무사고 경력은 불인정·가입경력은 인정, 1년 단위·1년 미만 합산·겹치는 기간은 하나만,
#      보험기간 중이나 끝난 뒤에도 신청해 사후 환급, 특약은 직접 골라야 함, 한정 범위 밖 운전자 사고는 보상 못 받을 수 있음,
#      CM 팝업·청년 특약 별도 안내(이달부터), 청년 만 19~34세, 종피보험자 계약당 최대 2명 사전 등록(비즈워치·위키트리)
#  - 금융위원회 2024.4.2 자동차보험 경력인정기준 개선: 경력별 서류·발급처, 장기렌터카 인정(일·시간 단위 제외, 2024.6.1 책임개시부터),
#      보험가입경력요율 최초 138.1%·1년 115.3%·2년 110.3%·3년 100%(참조순보험요율, 회사별 다를 수 있음)
#  - 환급 신청 기한은 출처에서 확인되지 않아 쓰지 않음. 발표일은 기사 2일·KDI 3일로 달라 '11월'로만 표기
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "사회초년생 돈 노트 ①"
TOPIC = "첫 차 보험료 줄이는 경력 인정 5가지(부모 보험·군 운전병·장기렌터카·법인 운전직·해외)와 뒤늦은 환급 신청"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=288893 (금융감독원 청년 자동차보험 가입절차 개선, 2026.11.3 수록)",
           "https://biz.sbs.co.kr/amp/article/20000343562 (SBS Biz 2026.11.2: 예시 금액 3가지)",
           "https://www.koreancenter.or.kr/news/articleView.html?idxno=1433339 (연합뉴스 2026.11.2)",
           "https://www.sidae.com/article/2026110214312893452 (시대 2026.11.2: 사후 환급, 1년 단위·합산·중복)",
           "https://www.smarttoday.co.kr/ko-kr/articles/113359 (스마트투데이 2026.11.2)",
           "https://news.bizwatch.co.kr/article/finance/2026/11/06/0020 (비즈워치 2026.11.7: 최대 2명 사전 등록, 사후 환급)",
           "https://www.wikitree.co.kr/articles/1171449 (위키트리 2026.11.3: 예시 금액 교차 확인)",
           "https://www.fsc.go.kr/no010101/82029 (금융위원회 2024.4.2 경력인정기준 개선: 서류·발급처, 가입경력요율)"]

S = []
# 1 표지 (B1: 제목 위 + 비노 가운데, 반전형)
S.append(cover(layout_for(10),
               "첫 차 보험료 133만원,<br>엄마 보험 하나로<br><span class=\"y\">71만원</span>이 됐어요",
               pose="point", accent="y", chip="부모님 차 몰던 3년이 경력이 돼요"))

# 2 영수증 두 장 (좌우 분할, 이번 주 디자인 실험)
def _rcpt(head, col, amt, lines, foot):
    li = "".join(f'<div style="display:flex;justify-content:space-between;font-size:26px;color:#444;padding:8px 0;border-bottom:2px dashed #CFCFCF"><span>{a}</span><span style="font-weight:700">{b}</span></div>' for a, b in lines)
    return f"""<div style="flex:1;background:#F4F1E8;color:#222;border-radius:10px 10px 0 0;padding:24px 24px 26px;box-shadow:0 14px 34px rgba(0,0,0,.55)">
   <p style="font-size:24px;color:#777;font-weight:700;text-align:center">자동차보험 1년</p>
   <p style="font-size:30px;font-weight:900;text-align:center;margin-top:2px;color:{col}">{head}</p>
   <div style="margin-top:14px">{li}</div>
   <p style="font-size:24px;color:#777;margin-top:16px">내는 보험료</p>
   <p style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:66px;line-height:1.05;color:{col};letter-spacing:-.03em">{amt}</p>
   <p style="font-size:23px;color:#555;margin-top:10px;line-height:1.4">{foot}</p>
  </div>"""

S.append(f"""
 <h2>같은 28살, 같은 차<br>영수증이 <span class="y">이렇게</span> 달라요</h2>
 <div style="display:flex;gap:22px;margin-top:24px;align-items:flex-start">
  {_rcpt("경력 0년으로 가입", "#C0392B", "133만497원", [("나이", "28세"), ("차", "아반떼 2,000만원"), ("명의", "본인 첫 가입"), ("인정 경력", "없음")], "처음 가입이라<br>할증이 붙은 값")}
  {_rcpt("엄마 보험 경력 인정", "#1F6FD1", "71만6,582원", [("나이", "28세"), ("차", "아반떼 2,000만원"), ("명의", "본인 첫 가입"), ("인정 경력", "3년 무사고")], "엄마 차 보험에<br>3년 올라가 있었음")}
 </div>
 <div class="box" style="margin-top:22px;padding:18px 30px;border-color:#FFE45C;display:flex;align-items:center;gap:24px">
  <div style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:64px;color:#FFE45C;flex:none">-46.1%</div>
  <p style="font-size:29px;color:#E0E0E0;line-height:1.45">1년에 약 <b style="color:#fff">61만원</b> 차이. 차이를 만든 건 운전 실력이 아니라 <b style="color:#fff">서류</b>였어요.</p>
 </div>
 <div class="box" style="margin-top:16px;padding:20px 30px"><p style="font-size:28px;color:#E0E0E0;line-height:1.45">오른쪽은 엄마 차 보험에 운전자로 3년 동안 올라가 있었고, 그동안 사고가 없었어요. 그래서 <b style="color:#fff">가입 경력 3년과 무사고 경력 3년</b>을 같이 인정받았어요.</p></div>
 <div class="src">출처: 금융감독원 예시(2026.11), SBS Biz·위키트리(2026.11.2~3). 보험사별로 할인 조건과 할인율이 달라요.</div>""")

# 3 왜 첫 차는 비싼가 (가입경력 요율 계단)
def _bar(lab, pct, w, col, note=""):
    return f"""<div style="display:flex;align-items:center;gap:18px">
   <div style="flex:none;width:170px;font-size:29px;font-weight:800;color:#fff">{lab}</div>
   <div style="flex:1;height:86px;background:#1C1C1C;border-radius:12px;position:relative">
    <div style="position:absolute;left:0;top:0;bottom:0;width:{w}%;background:{col};border-radius:12px"></div>
    <span style="position:absolute;left:22px;top:50%;transform:translateY(-50%);font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:44px;color:#121212">{pct}</span>
   </div>
   <div style="flex:none;width:110px;font-size:22px;color:#9E9E9E;line-height:1.3">{note}</div>
  </div>"""

S.append(f"""
 <h2>보험사는 첫 차 주인을<br><span class="r">'경력 0년'</span>으로 봐요</h2>
 <p class="lead" style="margin-top:14px">면허를 딴 지 몇 년이 지났어도 <b>내 이름으로 보험을 든 적</b>이 없으면 처음 가입자예요.</p>
 <div style="display:flex;flex-direction:column;gap:18px;margin-top:28px">
  {_bar("처음 가입", "138.1%", 100, "#FF6B6B", "최대 38.1%<br>더 내요")}
  {_bar("1년 이상", "115.3%", 83.5, "#FFB36B")}
  {_bar("2년 이상", "110.3%", 79.9, "#FFE45C")}
  {_bar("3년 이상", "100%", 72.4, "#7FB2FF", "기준")}
 </div>
 <div class="box" style="margin-top:30px;padding:22px 30px">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">그래서 '인정받는 경력'이 중요해요</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.45;margin-top:6px">내 이름 보험이 아니어도 실제로 운전한 기록이 있으면 최대 3년까지 가입 경력으로 쳐 줘요. 이 계단을 처음부터 건너뛰는 거예요.</p>
 </div>
 <div class="box" style="margin-top:16px;padding:20px 30px;border-color:#FF6B6B"><p style="font-size:28px;color:#E0E0E0;line-height:1.45"><b class="r">면허 딴 날</b>이 아니라 <b style="color:#fff">보험에 운전자로 이름이 오른 날</b>부터 경력이 쌓여요.</p></div>
 <div class="src">출처: 금융위원회(2024.4.2) 보험가입경력요율(참조순보험요율, 보험료 100만원 기준 예시), 금융감독원(2026.11). 회사별 적용률은 달라요.</div>""")

# 4 인정되는 경력 5가지 + 서류
S.append(f"""
 <h2>경력으로 쳐 주는<br><span class="y">운전 기록 5가지</span></h2>
 <table style="font-size:30px;line-height:1.4;margin-top:26px">
  <thead><tr><th style="width:34%">이런 적 있다면</th><th class="new">낼 서류</th><th style="width:22%">받는 곳</th></tr></thead>
  <tbody>
   <tr><th style="color:#fff;width:auto">부모·배우자 보험에<br>운전자로 등록</th><td>보험가입증명서<br><span style="font-size:23px;color:#9E9E9E">미리 등록해 두면 생략</span></td><td>보험사</td></tr>
   <tr><th style="color:#fff">군 운전병</th><td>병적증명서 등</td><td>병무청 등</td></tr>
   <tr><th style="color:#fff">장기렌터카 운전</th><td>임대차계약서, 임차료 낸 내역</td><td>렌터카 업체</td></tr>
   <tr><th style="color:#fff">관공서·회사<br>운전직</th><td>운전직 경력증명서, 원천징수영수증 등</td><td>근무한 곳</td></tr>
   <tr><th style="color:#fff">해외에서<br>자동차보험 가입</th><td>해외 보험가입증명서, 출입국 증명 등</td><td>외국 보험사, 주민센터</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:22px;padding:20px 30px;border-color:#FF6B6B"><p style="font-size:27px;color:#E0E0E0;line-height:1.45"><b class="r">장기렌터카</b>는 내가 임차인으로 계약서에 이름이 있어야 해요. 하루·시간 단위로 빌린 건 빠져요.</p></div>
 <div class="box" style="margin-top:14px;padding:20px 30px;border-color:#FFE45C"><p style="font-size:27px;color:#E0E0E0;line-height:1.45"><b class="y">부모님 보험</b>은 가입 전에 경력 인정 대상자로 미리 등록해 두면 증명서 없이 바로 반영돼요.</p></div>
 <div class="src">출처: 금융위원회(2024.4.2) 경력인정기준 개선, 시대·비즈워치(2026.11). 보험사에 따라 추가 서류가 있을 수 있어요.</div>""")

# 5 경력 계산 규칙
S.append(f"""
 <h2>경력은 이렇게<br><span class="b">계산</span>해요</h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 26px"><div class="num">1</div><div><h3>최대 3년까지</h3><p>그보다 오래 운전했어도 3년까지만 쳐 줘요. 3년이면 할증 계단 끝이에요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">2</div><div><h3>1년 단위, 짧은 건 더해요</h3><p>군 운전병 1년 6개월 + 렌터카 1년 6개월 = 3년처럼 합칠 수 있어요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">3</div><div><h3>겹치는 기간은 한 번만</h3><p>같은 6개월 동안 두 가지를 했어도 6개월로만 계산해요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">4</div><div><h3>사고가 있었다면</h3><p>최근 3년 안에 사고가 있으면 무사고 경력은 못 받아요. 가입 경력은 그대로 인정돼요.</p></div></div>
 </div>
 <div class="box" style="margin-top:20px;padding:20px 30px;border-color:#FFE45C"><p style="font-size:28px;color:#E0E0E0;line-height:1.45">그래서 엄마 보험 <b class="y">3년 무사고</b>가 가장 많이 내려가요. 가입 경력과 무사고 경력을 둘 다 받거든요.</p></div>
 <div class="src">출처: 시대·비즈워치·스마트투데이(2026.11), 금융감독원 예시(2026.11)</div>""")

# 6 같은 사람 네 가지 결과 (움직이는 장)
def _res(i, lab, sub, amt, w, col):
    return f"""<div id="r{i}" style="opacity:0">
   <div style="display:flex;justify-content:space-between;align-items:baseline"><p style="font-size:32px;color:#fff;font-weight:800">{lab}<span style="font-size:23px;color:#9E9E9E;font-weight:600;margin-left:10px">{sub}</span></p><p style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:48px;color:{col}">{amt}</p></div>
   <div style="height:44px;background:#1C1C1C;border-radius:12px;margin-top:10px"><div id="w{i}" data-w="{w}" style="height:100%;width:0;background:{col};border-radius:10px"></div></div>
  </div>"""

S.append(f"""
 <h2>28살 첫 차 1년 보험료<br><span class="y">고르기에 따라</span> 이만큼</h2>
 <div style="display:flex;flex-direction:column;gap:38px;margin-top:44px">
  {_res(1, "아무것도 안 하면", "특약 없음·경력 0", "247만", 100, "#FF6B6B")}
  {_res(2, "본인·연령 한정 특약", "경력 0", "133만", 53.8, "#FFB36B")}
  {_res(3, "군 운전병·렌터카 3년", "1년 6개월씩", "94.6만", 38.3, "#FFE45C")}
  {_res(4, "엄마 보험 3년 무사고", "종피보험자", "71.7만", 29.0, "#7FB2FF")}
 </div>
 <div class="box" id="tot" style="margin-top:32px;padding:22px 30px;border-color:#7FB2FF;opacity:0">
  <p style="font-size:30px;color:#fff;font-weight:800;line-height:1.4">특약과 경력만 챙겨도 <span class="b">절반 아래</span>로</p>
  <p style="font-size:27px;color:#BDBDBD;line-height:1.45;margin-top:6px">할인 특약은 자동으로 들어가지 않아요. 가입할 때 직접 골라야 해요.</p>
 </div>
 <div class="src">출처: 금융감독원 예시(28세, 아반떼 차량가액 2,000만원), SBS Biz(2026.11.2)·위키트리(2026.11.3)·시대(2026.11.2). 보험사·조건에 따라 달라요.</div>""")

# 7 부모가 할 일 vs 자녀가 할 일 (좌우)
def _side(head, col, items):
    li = "".join(f'<div style="display:flex;gap:12px;margin-top:24px"><span style="flex:none;font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:30px;color:{col}">{k}</span><p style="font-size:30px;color:#E0E0E0;line-height:1.45">{v}</p></div>' for k, v in items)
    return f'<div class="box" style="flex:1;padding:32px 26px;border-color:{col}"><p style="font-size:38px;font-weight:900;color:{col}">{head}</p>{li}</div>'

S.append(f"""
 <h2>면허 딴 자녀가 있다면<br><span class="y">각자 할 일</span></h2>
 <div style="display:flex;gap:18px;margin-top:28px;align-items:stretch">
  {_side("부모님", "#FFE45C", [("1", "자녀를 내 차 보험 운전자로 올리고 '경력 인정 대상자'로 등록"), ("2", "계약 하나에 최대 2명까지 미리 등록할 수 있어요"), ("3", "등록해 두면 나중에 따로 서류를 안 내도 돼요")])}
  {_side("자녀", "#7FB2FF", [("1", "첫 차 보험 들기 전에 군 운전병·렌터카 서류부터"), ("2", "온라인 가입 때 뜨는 경력 인정 안내를 넘기지 않기"), ("3", "본인·연령 한정 특약은 직접 선택")])}
 </div>
 <div class="box" style="margin-top:24px;padding:24px 30px"><p style="font-size:29px;color:#E0E0E0;line-height:1.5">금감원은 이달부터 만 19~34세가 온라인으로 가입할 때 경력 인정과 할인 특약을 <b style="color:#fff">팝업으로 따로 안내</b>하게 했어요. 대면·전화 가입 안내 대본도 고쳐요.</p></div>
 <div class="src">출처: 금융감독원(2026.11), 연합뉴스·SBS Biz(2026.11.2), 비즈워치(2026.11.7)·위키트리(2026.11.3, 최대 2명 사전 등록)</div>""")

# 8 이미 가입했다면 + 주의
S.append(f"""
 <h2>이미 비싸게<br><span class="y">가입했다면?</span></h2>
 <div class="box" style="margin-top:28px;padding:26px 32px;border-color:#FFE45C;margin-right:170px">
  <p style="font-size:32px;color:#FFE45C;font-weight:800">지금이라도 신청하세요</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:8px">가입·갱신 때 놓쳤어도 보험기간 중이나 끝난 뒤에 경력 인정을 신청할 수 있어요. 인정되면 그만큼 보험료를 돌려받아요.</p>
 </div>
 {bino('stop', 200, 'position:absolute;right:56px;top:330px;transform:rotate(6deg)')}
 <div class="rows" style="gap:12px;margin-top:22px">
  <div class="row box" style="padding:16px 26px"><div class="num">1</div><div><h3>가입한 보험사에 연락</h3><p>콜센터나 담당자에게 경력 인정 신청을 한다고 말해요.</p></div></div>
  <div class="row box" style="padding:16px 26px"><div class="num">2</div><div><h3>4장의 서류 제출</h3><p>엄마 보험 경력이면 보험가입증명서를 떼서 내요.</p></div></div>
 </div>
 <div class="box" style="margin-top:18px;padding:22px 32px;border-color:#FF6B6B">
  <p style="font-size:30px;color:#FF6B6B;font-weight:800">한정 특약은 이것만 조심</p>
  <p style="font-size:28px;color:#E0E0E0;line-height:1.5;margin-top:6px">본인 한정으로 들었는데 친구나 가족이 운전하다 사고가 나면 보상을 못 받을 수 있어요. 차를 같이 쓰면 범위를 넓혀 두세요.</p>
 </div>
 <div class="src">출처: 시대(2026.11.2)·비즈워치(2026.11.7)·SBS Biz(2026.11.2) 사후 환급, 연합뉴스·스마트투데이(2026.11.2) 한정 특약 주의, 금융위원회(2024.4.2)</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:40px">면허 딴 자녀, 막 취업한 동생에게<br><span class="y">먼저 보내 주세요</span></h2>
 <div class="note" style="margin-top:42px;padding:36px 40px 40px;margin-right:60px">
  <div style="font-size:32px;margin-bottom:10px">첫 차 보험 들기 전 체크</div>
  <div class="ck"><span>부모님 보험에 운전자 등록</span><span>군 운전병·렌터카 서류</span><span>경력 최대 3년 합산</span><span>한정 특약 직접 선택</span><span>놓쳤으면 사후 신청</span></div>
 </div>
 <div class="box" style="margin-top:42px"><p style="font-size:34px;color:#fff;font-weight:700">"운전은 몇 년 했는데 왜 신입이에요?"</p><p style="font-size:30px;margin-top:10px">보험사는 운전 기록이 아니라 서류를 봐요. 그 서류를 챙기는 쪽이 덜 내요.</p></div>
 <p style="font-size:32px;margin-top:32px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 보험료와 인정 여부는 보험사 안내와 약관을 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "6": {"dur": 4.5, "still_t": 4.2, "js": """
window.setT=function(t){
 for(let i=1;i<=4;i++){const s=0.2+(i-1)*0.55, o=c((t-s)/0.3), p=eo(c((t-s-0.1)/0.7));
  $('#r'+i).style.opacity=o; const w=$('#w'+i); w.style.width=(parseFloat(w.dataset.w)*p)+'%';}
 const q=c((t-2.8)/0.4); $('#tot').style.opacity=q; $('#tot').style.transform='translateY('+((1-eo(q))*24)+'px)';
};"""},
}

CAPTION = """첫 차 보험료 보고 놀랐다면
이것부터 확인하세요

28살 같은 차인데
133만원과 71만원

차이는 운전 실력이 아니라
엄마 보험에 이름이 있던 3년

부모님 보험 운전자 등록
군 운전병, 장기렌터카
회사 운전직, 해외 보험
최대 3년 경력으로 쳐 줘요

이미 가입했어도
나중에 신청하면
차액을 돌려받을 수 있어요

면허 딴 자녀에게
공유해 주세요

#자동차보험 #첫차보험료
#사회초년생 #운전경력인정 #보험비밀노트"""
