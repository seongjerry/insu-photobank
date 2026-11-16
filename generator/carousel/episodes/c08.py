# 캐러셀 c08 · 해지·갈아타기 전에 ③ "보험 괜히 들었나" 싶을 때, 돌려받는 기한
# 커뮤니티 키워드: "보험 가입 후 마음이 바뀌었는데 취소 가능?", "약관 못 받았는데 계약 취소 되나요" (보험 블로그·육아 Q&A·지식iN형 질문 반복, 2026.11 조사)
#   + 아이뉴스24 2026.9.2 대형 생보사 종신보험 청약철회 3년 새 2배 보도로 "가입 취소" 관심 증가. c07 에서 다음 편으로 예고한 주제
#   (참고: 같은 날 가장 큰 이슈는 1·2세대 실손 할인특약·5세대 전환 할인이었으나, 보험사별 세부 조건이 아직 확정 공지 전이라 topic_pool 보류 기준대로 제외)
# 공식·교차 출처:
#  - 청약철회 보장성: 보험증권 받은 날부터 15일·청약한 날부터 30일 중 먼저 오는 날, 접수 3영업일 안 반환, 지연 시 가산, 위약금 청구 금지, 철회 전 보험금 사유 발생 시 효력 없음:
#      금융소비자보호법 제46조(korea.legal) / 금융감독원 소비자경보 2025-3호(2025.2.26) / 보험사 공식 안내(청약철회·계약취소)
#  - 65세 이상 전화 가입 45일, 건강진단 계약·보험기간 90일 이내·전문금융소비자 철회 불가:
#      이투데이 브라보마이라이프 2022.12.14(금감원 금융꿀팁) / 보험사 공식 안내(청약철회·계약취소)
#  - 품질보증해지(계약취소): 계약 성립일부터 3개월, 약관·청약서 부본 미전달·중요내용 미설명·자필서명 누락, 낸 보험료 + 이자:
#      금융감독원 소비자경보 2025-3호(2025.2.26) / 보험사 공식 안내(청약철회·계약취소)
#  - 위법계약해지: 계약일부터 5년·안 날부터 1년 안, 10일 안 수락 여부 통지, 거절 시 사유, 정당한 사유 없으면 직접 해지, 수수료·위약금 금지, 해지 전 위험보험료 등은 환급 안 됨:
#      금융소비자보호법 제47조(보험사 안내문) / 금융위원회 금소법 10문10답 2021.3.25 / 정책브리핑 2021.3.25 / 로톡 해설
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "해지·갈아타기 전에 ③"
TOPIC = "보험 가입 후회될 때 돌려받는 기한·청약철회 15일·품질보증해지 3개월·위법계약해지 5년"
SOURCES = ["https://korea.legal/wiki/금융소비자-보호에-관한-법률-제46조/ (금소법 제46조 청약의 철회)",
           "https://m.samsungfire.com/download/consumer/ca_d86.pdf (금융감독원 소비자경보 2025-3호, 2025.2.26: 청약철회 15일·30일, 계약취소 3개월)",
           "https://www.cardif.co.kr/customer-center/%EB%B3%B4%ED%97%98-%EC%B2%AD%EC%95%BD%EC%B2%A0%ED%9A%8C-%EA%B3%84%EC%95%BD%EC%B7%A8%EC%86%8C.do (보험사 공식 안내: 65세 전화 45일, 예외, 3영업일, 계약취소)",
           "https://bravo.etoday.co.kr/view/atc_view/14218 (이투데이 2022.12.14, 금감원 금융꿀팁: 65세 이상 전화 45일)",
           "https://www.carrotins.com/cdn/dis/doc/pdf/customerPortal/위법계약해지권.pdf (금소법 제47조 위법계약 해지권 안내: 5년·1년·10일)",
           "https://fsc.go.kr/no010101/75613 (금융위원회 금소법 10문10답 2021.3.25: 해지 수수료·위약금 금지, 환급 범위)",
           "https://m.korea.kr/news/policyNewsView.do?newsId=148885436 (정책브리핑 2021.3.25: 5년·1년, 입증책임)",
           "https://www.lawtalk.co.kr/posts/178131 (위법계약해지권 해설: 10일 통지, 직접 해지)",
           "https://inews24.com/view/2000738 (아이뉴스24 2026.9.2, 청약철회 증가 보도, 주제 참고용)"]

S = []
# 1 표지 (B2: 큰 숫자 + 비노 옆, 숫자형)
S.append(cover(layout_for(8),
               "보험<br>괜히 들었나<br>싶을 땐<br><span class=\"y\">날짜</span>부터",
               pose="check", accent="y", big="15일",
               big_label="가입하고 마음이 바뀌었다면",
               source="15일·3개월·5년, 언제냐에 따라 돌려받는 돈이 달라요"))

# 2 왜 문제인가
S.append(f"""
 <h2>그냥 <span class="r">해지</span>하면<br>손해 보는 이유 3가지</h2>
 <div class="rows" style="gap:16px;margin-top:30px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>해지는 해약환급금만 줘요</h3><p>가입 초기에 해지하면 돌려받는 돈이 낸 보험료보다 훨씬 적거나 거의 없을 수 있어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>철회·취소는 낸 돈을 돌려줘요</h3><p>기한 안에 청약철회나 계약취소를 하면 낸 보험료를 돌려받아요. 계약취소는 이자까지 붙어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">3</div><div><h3>기한이 지나면 권리가 사라져요</h3><p>철회는 보통 15일, 취소는 3개월. 날짜를 넘기면 같은 방법을 쓸 수 없어요.</p></div></div>
 </div>
 <div class="box" style="margin-top:22px;padding:22px 30px;border-color:#FFE45C">
  <p style="font-size:28px;color:#9E9E9E;font-weight:700">이런 마음이 들면 해지 버튼보다 먼저</p>
  <p style="font-size:31px;color:#fff;font-weight:700;line-height:1.55;margin-top:8px">"분위기에 휩쓸려 사인했어요"<br>"설명 들은 거랑 달라요"<br>"약관을 받은 기억이 없어요"</p>
 </div>
 <div class="src">출처: 금융소비자보호법 제46조, 금융감독원 소비자경보(2025.2), 보험사 공식 안내</div>""")

# 3 핵심 숫자 (움직이는 장): 기한 타임라인
def _node(i, num, unit, h, p, col):
    return f"""<div class="row" id="n{i}" style="align-items:center;gap:26px;opacity:0">
   <div style="flex:none;width:200px;text-align:right;font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:84px;line-height:1;color:{col}">{num}<span style="font-size:40px;margin-left:4px">{unit}</span></div>
   <div style="flex:none;width:28px;height:28px;border-radius:50%;background:{col};box-shadow:0 0 0 8px #121212;position:relative;z-index:2"></div>
   <div><h3 style="font-size:36px;font-weight:800;color:#fff;line-height:1.3">{h}</h3><p style="font-size:28px;line-height:1.42;color:#BDBDBD;margin-top:4px">{p}</p></div>
  </div>"""

S.append(f"""
 <h2>돌려받는 기한,<br><span class="y">날짜로 정리</span>했어요</h2>
 <p class="lead" style="margin-top:14px">언제 알아챘는지에 따라 쓸 수 있는 방법이 달라요.</p>
 <div style="position:relative;margin-top:36px">
  <div id="ln" style="position:absolute;left:239px;top:20px;width:6px;height:0;background:linear-gradient(#FFE45C,#7FB2FF,#FF6B6B);border-radius:3px"></div>
  <div style="display:flex;flex-direction:column;gap:46px;position:relative">
   {_node(1, "15", "일", "청약철회", "보험증권 받은 날부터 15일 안. 이유 없이 낸 보험료 전부", "#FFE45C")}
   {_node(2, "30", "일", "철회 마지노선", "청약한 날부터 30일이 지나면 철회는 끝. 65세 이상 전화 가입은 45일", "#FFE45C")}
   {_node(3, "3", "개월", "계약취소", "약관을 못 받았거나 설명을 못 들었다면 성립일부터 3개월 안. 낸 보험료 + 이자", "#7FB2FF")}
   {_node(4, "5", "년", "위법계약해지", "잘못 팔린 계약이면 계약일부터 5년, 안 날부터 1년 안. 위약금 없이", "#FF6B6B")}
  </div>
 </div>
 <div class="box" id="ex" style="margin-top:40px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:29px;color:#E0E0E0;line-height:1.45"><b class="y">예시</b> 청약하고 5일 뒤 증권을 받았다면<br>15일을 더해 <b style="color:#fff">청약 후 20일째</b>까지 철회할 수 있어요.</p></div>
 <div class="src">출처: 금소법 제46·47조, 금융감독원 소비자경보(2025.2), 이투데이(2022.12, 금감원 금융꿀팁), 보험사 공식 안내</div>""")

# 4 비교표
S.append(f"""
 <h2>세 가지 방법<br><span class="y">한눈에 비교</span></h2>
 <table style="font-size:27px;line-height:1.38;margin-top:26px">
  <thead><tr><th style="width:19%;font-size:26px"></th><th class="new" style="font-size:28px">청약철회</th><th style="font-size:28px;color:#7FB2FF">계약취소</th><th style="font-size:28px;color:#FF6B6B">위법계약해지</th></tr></thead>
  <tbody>
   <tr><th style="color:#fff;font-size:27px;padding:22px 12px">기한</th><td>증권 받고 15일<br>(청약 후 30일까지)</td><td>계약 성립 후<br>3개월</td><td>계약 후 5년,<br>안 날부터 1년</td></tr>
   <tr><th style="color:#fff;font-size:27px;padding:22px 12px">이유</th><td>필요 없음</td><td>약관·청약서 못 받음, 설명 못 들음, 자필서명 안 함</td><td>설명의무 위반, 부당권유 같은 판매 규칙 위반</td></tr>
   <tr><th style="color:#fff;font-size:27px;padding:22px 12px">돌려받는 돈</th><td>낸 보험료 전부</td><td>낸 보험료 + 이자</td><td>해지 수수료·위약금 없이 정리. 이미 받은 보장 비용은 빠짐</td></tr>
   <tr><th style="color:#fff;font-size:27px;padding:22px 12px">근거</th><td>금소법 제46조</td><td>표준약관</td><td>금소법 제47조</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:26px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:29px;color:#E0E0E0;line-height:1.45">위로 갈수록 <b class="y">돌려받는 돈이 많고</b> 조건이 쉬워요.<br>그래서 <b class="y">빨리 알아챌수록</b> 유리해요.</p></div>
 <div class="src">출처: 금소법 제46·47조, 금융감독원 소비자경보(2025.2), 금융위원회 금소법 10문10답(2021.3)</div>""")

# 5 나도 해당되나
S.append(f"""
 <h2>내 경우도 되는지<br><span class="b">이것부터 확인</span></h2>
 <div class="box" style="margin-top:24px;padding:20px 30px">
  <p style="font-size:30px;color:#FFE45C;font-weight:800">기간이 더 길어지는 경우</p>
  <p style="font-size:29px;color:#E0E0E0;line-height:1.5;margin-top:8px">만 65세 이상이 <b style="color:#fff">전화로 가입</b>했다면 청약 후 30일이 아니라 <b class="y">45일</b>까지 철회할 수 있어요. 증권 받고 15일 기준은 같아요.</p>
 </div>
 <div class="box" style="margin-top:13px;padding:20px 30px;border-color:#FF6B6B">
  <p style="font-size:30px;color:#FF6B6B;font-weight:800">청약철회가 안 되는 계약</p>
  <p style="font-size:29px;color:#E0E0E0;line-height:1.55;margin-top:8px">· 보험사 지원으로 건강진단을 받고 든 계약<br>· 보험기간이 90일 이내인 계약<br>· 전문금융소비자가 든 계약</p>
 </div>
 <div class="box" style="margin-top:13px;padding:20px 30px;border-color:#7FB2FF">
  <p style="font-size:30px;color:#7FB2FF;font-weight:800">철회 전에 아팠다면</p>
  <p style="font-size:29px;color:#E0E0E0;line-height:1.5;margin-top:8px">철회 전에 이미 보험금 받을 일이 생겼다면 철회 효력이 없어요. 그 사실을 알고도 철회했다면 철회돼요. 청구할 일이 있으면 먼저 따져 보세요.</p>
 </div>
 <div class="box" style="margin-top:13px;padding:20px 30px">
  <p style="font-size:30px;color:#fff;font-weight:800">신청은 이렇게</p>
  <p style="font-size:29px;color:#E0E0E0;line-height:1.5;margin-top:8px">콜센터·홈페이지, 서면 말고도 이메일·문자로 철회 뜻을 보낼 수 있어요. 보낸 기록은 남겨 두세요.</p>
 </div>
 <div class="src">출처: 금소법 제46조 제5항·시행령 제37조, 이투데이(2022.12, 금감원 금융꿀팁), 보험사 공식 안내. 상품마다 다를 수 있어요.</div>""")

# 6 지금 할 순서
S.append(f"""
 <h2>후회된다면<br><span class="y">이 순서대로</span></h2>
 <div class="rows" style="gap:12px;margin-top:22px">
  <div class="row box" style="padding:17px 28px"><div class="num">1</div><div><h3>날짜 두 개 확인</h3><p>청약한 날, 보험증권 받은 날. 문자·이메일·증권에 적혀 있어요.</p></div></div>
  <div class="row box" style="padding:17px 28px"><div class="num">2</div><div><h3>15일 안이면 청약철회</h3><p>콜센터·홈페이지·서면으로 신청해요. 해지가 아니라 "철회"라고 말하세요.</p></div></div>
  <div class="row box" style="padding:17px 28px"><div class="num">3</div><div><h3>지났다면 3개월 사유 점검</h3><p>약관·청약서 받았는지, 중요한 내용 설명 들었는지, 직접 서명했는지.</p></div></div>
  <div class="row box" style="padding:17px 28px"><div class="num">4</div><div><h3>잘못 팔렸다면 해지요구서</h3><p>설명과 실제가 달랐던 점을 적어 서면으로 내요. 녹취·문자를 함께 모아요.</p></div></div>
  <div class="row box" style="padding:17px 28px"><div class="num">5</div><div><h3>거절되면 금감원 민원</h3><p>거절 사유를 받아 두고 금융감독원(1332)에 민원·분쟁조정을 신청해요.</p></div></div>
 </div>
 <div class="src">출처: 금소법 제46·47조, 금융감독원 소비자경보(2025.2), 보험사 공식 안내</div>""")

# 7 Q&A
S.append(f"""
 <h2>헷갈리는 질문<br><span class="b">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:22px;gap:12px">
  <div class="box"><div class="q">증권을 아직 못 받았어요</div><div class="a">청약한 날부터 30일 기준이 적용돼요. 두 기한 중 먼저 오는 날까지예요.</div></div>
  <div class="box"><div class="q">철회하면 위약금 내나요?</div><div class="a">아니요. 법으로 위약금이나 손해배상을 청구할 수 없게 돼 있어요.</div></div>
  <div class="box"><div class="q">돈은 언제 돌려받아요?</div><div class="a">철회 접수일부터 3영업일 안이에요. 늦어지면 그 기간만큼 이자를 더해 줘요.</div></div>
  <div class="box"><div class="q">태블릿에 전자서명 했어요</div><div class="a">전자서명도 자필서명으로 봐요. 이 경우엔 약관을 받았는지, 설명을 들었는지를 따져 보세요.</div></div>
  <div class="box"><div class="q">부모님이 전화로 가입하셨어요</div><div class="a">만 65세 이상이면 청약 후 45일까지 철회 기간이 늘어나요. 날짜부터 확인해 주세요.</div></div>
 </div>
 <div class="src">출처: 금소법 제46조, 이투데이(2022.12, 금감원 금융꿀팁), 보험사 공식 안내</div>""")

# 8 보너스: 위법계약해지 10일 + 다음 편
S.append(f"""
 <h2>위법계약해지,<br><span class="r">10일</span>을 기억하세요</h2>
 <p class="lead">해지를 요구하면 회사에도 <b>답해야 할 기한</b>이 있어요.</p>
 <div class="box" style="margin-top:22px;padding:24px 30px">
  <div class="rows" style="gap:16px;margin-top:0">
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">1</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">해지요구서를 받은 날부터 <b class="y">10일 안</b>에 받아 줄지 알려 줘야 해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">2</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">거절하면 <b class="y">거절 이유</b>도 함께 알려 줘야 해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">3</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">정당한 이유 없이 거절하면 소비자가 <b class="y">직접 해지</b>할 수 있어요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">4</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">해지 수수료·위약금은 받을 수 없어요.</p></div></div>
  </div>
 </div>
 <p style="font-size:27px;color:#BDBDBD;margin-top:16px;line-height:1.45">해지 전까지 받은 보장 비용은 돌려받지 못해요. 이건 손해배상이나 분쟁조정으로 따로 다퉈요.</p>
 <div class="note" style="margin-top:26px;font-size:34px;transform:rotate(-1.5deg)">다음 노트<br>무료 건강강연 다녀온 부모님께</div>
 <div class="src" style="padding-bottom:96px;margin-top:14px">출처: 금소법 제47조, 금융위원회 금소법 10문10답(2021.3.25), 정책브리핑(2021.3.25)</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">보험 들고 고민하는 가족에게<br><span class="y">먼저 보내 주세요</span></h2>
 <div class="note" style="margin-top:44px;padding:36px 40px 40px">
  <div style="font-size:32px;margin-bottom:10px">해지 버튼 누르기 전 체크</div>
  <div class="ck"><span>청약일·증권 받은 날 확인</span><span>15일 안이면 청약철회</span><span>약관·설명·서명 3가지 점검</span><span>3개월 안이면 계약취소</span><span>잘못 팔렸으면 해지요구서</span></div>
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">"해지하면 얼마 못 받아요"</p><p style="font-size:30px;margin-top:10px">해지 말고 철회·취소가 되는지부터 보면 달라져요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 조건은 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4.5, "still_t": 4.2, "js": """
window.setT=function(t){
 const H=document.querySelector('#n4').offsetTop+20;
 $('#ln').style.height=(H*eo(c((t-0.2)/2.6)))+'px';
 for(let i=1;i<=4;i++){
  const p=eb(c((t-0.3-i*0.55)/0.5)), o=c((t-0.3-i*0.55)/0.35);
  const n=$('#n'+i); n.style.opacity=o; n.style.transform='translateX('+((1-p)*40)+'px)';
 }
};"""},
}

CAPTION = """보험 가입하고
"괜히 들었나" 싶을 때
해지 버튼부터 누르면
손해 볼 수 있어요

👉 증권 받고 15일 안: 청약철회
👉 약관·설명·서명 빠졌으면
   3개월 안: 계약취소
👉 잘못 팔린 계약이면
   5년 안: 위법계약해지

철회·취소는 낸 보험료를
돌려받을 수 있어요

만 65세 이상이 전화로 가입했다면
철회 기간이 45일까지 늘어요

보험 들고 고민하는 가족에게
공유해 주세요

다음 노트
무료 건강강연 다녀온 부모님께

#보험청약철회 #보험취소 #위법계약해지
#보험해지 #보험비밀노트"""
