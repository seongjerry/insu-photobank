# 캐러셀 c04 · 보험사가 먼저 말 안 해주는 것 ③ 보험금 거절 통보 받았을 때
# 커뮤니티 키워드: "보험금 청구했더니 거절", "실비 청구 거절 이의신청", "보험금 부지급 통보 받았어요 어떻게 해요" (네이버 블로그·다음 보험카페·클리앙 실비 청구 글 반복)
# 언론 이슈: SBS Biz "비급여 신경전 가열…보험 분쟁조정, 작년치 넘었다" 2026.11.4 / 아주경제 "금감원, 보험사 분쟁 '끝장 점검'…현장조사 연장" 2026.11.10
# 공식·교차 출처:
#  - 2026년 1~9월 분쟁조정 신청(중복·반복 제외) 34,783건: SBS Biz 2026.11.4 / 아주경제 2026.11.10 (손보 28,382건 + 생보 6,401건 = 34,783건 일치)
#  - 손보 28,382건: 손해보험협회 공시 (FETV 2026.11.10, 아주경제 2026.11.10)
#  - 거절 사유 비율(진단·치료 불인정 67.4%, 약관 이견 20.7%, 손해액 이견 9.0%), 평균 1,618만 원: 한국소비자원 2025년 보험 피해구제 분석 (SBS Biz 2026.6.7, Insurance Business 2026.6.10)
#  - 분쟁조정 절차 30일·60일·20일, 시효중단: 금융소비자보호법 제36조·제40조
#  - 2천만 원 이하 소액분쟁은 조정안 제시 전 금융회사 소송 제기 불가: 금융소비자보호법 제42조 (SBS Biz 2025.9.4)
#  - 보험금 청구권 소멸시효 3년: 상법 제662조
#  - 손해사정사 선임 요청: 실손해 보상 건 대상, 정액담보 제외, 착수 전 통보·동의 시 비용 보험사 부담 (손해보험사 공식 안내, 금융위원회 손해사정 제도 개선)
#  - 지급 지연 시 사유·지급예정일 통지, 가지급보험금(추정 보험금 50% 이내): 표준약관 보험금 지급 조항
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "보험사가 먼저 말 안 해주는 것 ③"
TOPIC = "보험금 청구했더니 거절, 통보 받은 날부터 할 일"
SOURCES = ["https://biz.sbs.co.kr/article/20000344159 (2026.11.4, 1~9월 분쟁조정 신청 34,783건)",
           "https://www.ajunews.com/view/20261110142136361 (2026.11.10, 손보 28,382건·생보 6,401건, 금감원 현장점검 연장)",
           "https://www.fetv.co.kr/news/articleView.html?idxno=313292 (2026.11.10, 손해보험협회 공시)",
           "https://biz.sbs.co.kr/amp/article/20000314907 (2026.6.7, 한국소비자원 보험 피해구제 분석)",
           "https://www.insurancebusinessmag.com/asia/news/breaking-news/korea-consumer-agency-flags-high-payout-refusal-rate-by-insurers-578468.aspx (2026.6.10)",
           "금융소비자보호법 제36조·제40조·제42조, 상법 제662조",
           "https://www.kbinsure.co.kr/m/pop/CG205010002.ec (손해사정사 선임 요청 제도 안내)",
           "https://www.clien.net/service/board/park/19269391 (주제 발굴)"]

S = []
# 1 표지 (B2: 큰 숫자 + 비노 옆, 숫자형)
S.append(cover(layout_for(4),
               "보험금<br>청구했더니<br><span class=\"y\">거절</span>이요?",
               pose="sad", accent="y", big="34,783",
               big_label="올해 9월까지 보험 분쟁조정 신청 (건)",
               source="그냥 넘기기 전에, 통보 받은 날부터 할 일을 정리했어요"))

# 2 거절 사유 3가지
S.append(f"""
 <h2>거절 통보서,<br><span class="y">사유부터</span> 보세요</h2>
 <p class="lead">한국소비자원에 들어온 보험금 거절 분쟁<br><b>798건</b>을 사유별로 나누면 이래요.</p>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num" style="width:120px;font-size:30px">67.4%</div><div><h3>주치의 진단·치료를 인정 안 함</h3><p>"수술·입원이 필요 없었다" 같은 경우. <b style="color:#fff">주치의 소견서</b>가 핵심 자료예요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="width:120px;font-size:30px">20.7%</div><div><h3>약관 해석이 다름</h3><p>"보장 대상이 아니다" 같은 경우. 근거가 된 <b style="color:#fff">약관 조항 번호</b>를 받아 두세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="width:120px;font-size:30px">9.0%</div><div><h3>손해액(금액)이 다름</h3><p>일부만 주는 경우. <b style="color:#fff">영수증·세부내역서</b>로 금액을 맞춰 보세요.</p></div></div>
 </div>
 <div class="box" style="margin-top:22px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:29px;color:#E0E0E0;line-height:1.45">거절된 보험금은 평균 <b class="y">1,618만 원</b>. 그냥 넘기기엔 큰돈이에요.</p></div>
 <div class="src">출처: 한국소비자원 2025년 보험 피해구제 신청 분석 (2026.6 발표)</div>""")

# 3 숫자 (움직이는 장)
S.append(f"""
 <h2>억울해서 다투는 사람,<br><span class="r">계속 늘고</span> 있어요</h2>
 <p class="lead">금융감독원에 보험 분쟁조정을 신청한 건수예요.<br>(2026년 1~9월, 중복·반복 신청 제외)</p>
 <div class="box" style="margin-top:28px;text-align:center;padding:30px 20px 34px">
  <p style="font-size:30px;color:#9E9E9E;font-weight:700">보험 분쟁조정 신청</p>
  <div id="big" style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:150px;line-height:1.1;color:#FF6B6B;margin-top:6px">34,783건</div>
  <div style="display:flex;height:58px;border-radius:14px;overflow:hidden;margin:24px 20px 0;background:#2A2A2A">
   <div id="b1" style="width:81.6%;background:#FFE45C"></div><div id="b2" style="width:18.4%;background:#7FB2FF"></div>
  </div>
  <div style="display:flex;justify-content:space-between;margin:14px 20px 0;font-size:28px;font-weight:700">
   <span class="y">손해보험 28,382건</span><span class="b">생명보험 6,401건</span>
  </div>
 </div>
 <div class="box" style="margin-top:24px;padding:24px 30px"><p style="font-size:30px;color:#E0E0E0;line-height:1.45">실손보험 비급여 치료 심사가 깐깐해지면서 다툼이 늘었다는 분석이 많아요. 금감원은 보험사 분쟁 처리 <b class="y">현장점검 기간도 연장</b>했어요(2026.11).</p></div>
 <div class="src">출처: 손해보험협회 공시, SBS Biz(2026.11.4)·아주경제(2026.11.10) 보도</div>""")

# 4 비교표
S.append(f"""
 <h2>다툴 수 있는 길은<br><span class="y">세 가지</span>예요</h2>
 <table>
  <thead><tr><th style="width:20%"></th><th>보험사 재심사</th><th class="new">금감원 분쟁조정</th><th>소송</th></tr></thead>
  <tbody>
   <tr><th>비용</th><td>없음</td><td><b class="y">무료</b></td><td>인지대·변호사 비용</td></tr>
   <tr><th>누가 판단</th><td>보험사</td><td>금감원·분쟁조정위원회</td><td>법원</td></tr>
   <tr><th>기간</th><td>보험사마다 달라요</td><td>법에 정한 기한 있음<br>(7장 참고)</td><td>길게는 수년</td></tr>
   <tr><th>좋은 점</th><td>새 자료로 빨리 뒤집을 수 있어요</td><td>혼자서도 온라인 신청, 시효가 멈춰요</td><td>결과가 확정돼요</td></tr>
   <tr><th>이럴 때</th><td>새 소견서·검사 결과가 생겼을 때</td><td>재심사도 거절됐을 때</td><td>금액이 크고 다툼이 길 때</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:26px;padding:24px 30px;border-color:#FFE45C"><p style="font-size:30px;color:#E0E0E0;line-height:1.45"><b class="y">순서가 중요해요</b><br>보통은 재심사 → 분쟁조정 → 소송 순으로 가요. 앞 단계에서 모은 서류가 다음 단계의 무기가 돼요.</p></div>
 <div class="src">금융소비자보호법 제36조·제40조 기준. 개별 사안은 다를 수 있어요.</div>""")

# 5 범위 넓히기 + 지급 기한
S.append(f"""
 <h2>'전부 거절'만<br><span class="b">다툴 수 있는 게</span> 아니에요</h2>
 <div class="stat" style="margin-top:28px">
  <div class="box"><div class="k">일부만 줌</div><div class="v y" style="font-size:60px;line-height:1.4">감액</div><div class="d">금액 근거를 요청</div></div>
  <div class="box"><div class="k">한참 안 줌</div><div class="v y" style="font-size:60px;line-height:1.4">지연</div><div class="d">지급예정일 확인</div></div>
  <div class="box"><div class="k">계약을 끊음</div><div class="v y" style="font-size:60px;line-height:1.4">해지</div><div class="d">해지 사유 서면 요청</div></div>
 </div>
 <div class="box" style="margin-top:28px;padding:26px 32px">
  <p style="font-size:32px;color:#fff;font-weight:800">약관에 적힌 지급 약속</p>
  <div class="rows" style="gap:14px;margin-top:16px">
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">1</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">서류 접수 후 <b class="y">3영업일 안</b> 지급이 원칙이에요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">2</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">조사로 늦어지면 <b class="y">사유와 지급예정일</b>을 알려 줘야 해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">3</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">급하면 추정 보험금의 <b class="y">50% 이내</b>를 먼저 받는 가지급제도를 물어보세요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">4</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">기한을 넘겨 주면 그 기간만큼 <b class="y">약정 이자</b>를 더해 줘요.</p></div></div>
  </div>
 </div>
 <div class="note" style="margin-top:40px;font-size:36px;transform:rotate(-1.5deg)">통보가 전화로만 왔다면?<br>날짜·담당자·들은 내용을 바로 적어 두세요</div>
 <div class="src">표준약관 보험금 지급 조항 기준. 보험사·상품에 따라 다를 수 있어요.</div>""")

# 6 통보 받은 날부터 순서
S.append(f"""
 <h2>통보 받은 날부터<br><span class="y">이 순서로</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 28px"><div class="num">1</div><div><h3>거절 사유를 서면으로 받기</h3><p>전화로만 들었다면 사유·근거 약관 조항을 문서로 달라고 하세요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">2</div><div><h3>내 쪽 자료 모으기</h3><p>진료기록, 검사 결과, 주치의 소견서, 통화 날짜·담당자 메모.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">3</div><div><h3>보험사에 재심사 요청</h3><p>거절 사유에 맞는 새 자료를 붙여 다시 판단해 달라고 하세요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">4</div><div><h3>금감원 분쟁조정 신청</h3><p>e-금융민원센터 온라인 또는 1332. 신청 비용은 없어요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">5</div><div><h3>그래도 안 되면 소송 검토</h3><p>조정 결과와 모은 자료를 들고 법률 상담을 받아 보세요.</p></div></div>
 </div>""")

# 7 분쟁조정 자세히
S.append(f"""
 <h2>분쟁조정,<br><span class="y">이렇게 진행돼요</span></h2>
 <div class="stat" style="margin-top:28px">
  <div class="box"><div class="k">합의 권고</div><div class="v y">30일</div><div class="d">안에 합의 안 되면<br>위원회로</div></div>
  <div class="box"><div class="k">조정안 작성</div><div class="v y">60일</div><div class="d">위원회 회부 후<br>이 안에</div></div>
  <div class="box"><div class="k">수락 결정</div><div class="v y">20일</div><div class="d">안에 답 없으면<br>불수락</div></div>
 </div>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num">✓</div><div><h3>신청하면 시효가 멈춰요</h3><p>보험금 청구 기한(3년)이 조정 기간 동안 흘러가지 않아요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">✓</div><div><h3>2천만 원 이하라면</h3><p>내가 조정을 신청한 소액 사건은 조정안이 나오기 전까지 보험사가 소송을 걸 수 없어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">!</div><div><h3>바로 끝날 수도 있어요</h3><p>조정 대상이 아니거나 진행할 실익이 없다고 보면 회부하지 않고 서면으로 알려 줘요. 그래서 증빙 서류가 중요해요.</p></div></div>
 </div>
 <div class="src">금융소비자보호법 제36조(기간)·제40조(시효중단)·제42조(소액분쟁 특례)</div>""")

# 8 Q&A + 다음 편
S.append(f"""
 <h2>헷갈리는 질문<br><span class="b">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:20px;gap:12px">
  <div class="box"><div class="q">거절된 지 오래됐는데 늦었나요?</div><div class="a">보험금 청구권은 3년이 지나면 소멸해요(상법 제662조). 청구 사유가 생긴 날부터 따져 보세요.</div></div>
  <div class="box"><div class="q">내 편 손해사정사를 둘 수 있나요?</div><div class="a">실손처럼 실제 손해를 보상하는 건은 가능해요. 진단비 같은 정액형은 대상이 아니에요.</div></div>
  <div class="box"><div class="q">손해사정사 비용은 누가 내요?</div><div class="a">보험사가 조사를 시작하기 전에 알리고 동의를 받으면 보험사가 내요.</div></div>
  <div class="box"><div class="q">조정안이 마음에 안 들면요?</div><div class="a">수락하지 않으면 그 뒤에 소송을 선택할 수 있어요.</div></div>
 </div>
 <div style="display:flex;gap:24px;align-items:flex-end;margin-top:22px">
  <div class="note" style="flex:1;font-size:36px;transform:rotate(-1.5deg)">다음 노트<br>숨은 보험금 3분 만에 찾는 법</div>
  {bino('cheer', 180)}
 </div>
 <div class="src" style="padding-bottom:96px;margin-top:14px">손해사정사 선임은 보험사 동의 기준이 있어요. 보험사에 확인하세요.</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">이 노트,<br><span class="y">보험금 거절당한 가족에게</span></h2>
 <div class="note" style="margin-top:44px;padding:36px 40px 40px">
  <div style="font-size:32px;margin-bottom:10px">거절 통보 체크</div>
  <div class="ck"><span>거절 사유는 서면으로</span><span>근거 약관 조항 번호 확인</span><span>주치의 소견서 준비</span><span>재심사 먼저 요청</span><span>금감원 분쟁조정은 무료</span></div>
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">"보험사가 안 된대요"</p><p style="font-size:30px;margin-top:10px">여기서 멈추지 말고, 저장해 두고 순서대로 해 보세요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 개별 사안은 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4, "still_t": 3.6, "js": """
window.setT=function(t){
 const p=eo(c((t-0.2)/1.8));
 $('#big').textContent=Math.round(34783*p).toLocaleString('en-US')+'건';
 const q=eo(c((t-1.6)/1.2));
 $('#b1').style.width=(81.6*q)+'%';$('#b2').style.width=(18.4*q)+'%';
};"""},
}

CAPTION = """보험금 청구했더니
"지급이 어렵습니다"
이런 통보 받아 보셨나요?

올해 9월까지 보험 분쟁조정
신청만 3만4783건이에요
(중복 신청 제외)

👉 거절 사유부터 서면으로
👉 사유별로 챙길 서류가 달라요
👉 재심사 → 분쟁조정 → 소송
👉 금감원 분쟁조정은 무료
👉 신청하면 청구 기한이 멈춰요

그냥 넘기기 전에
저장해 두고 순서대로 하세요

보험금 거절당한 가족에게
공유해 주세요

다음 노트
숨은 보험금 3분 만에 찾는 법

#보험금거절 #보험금청구 #분쟁조정 #실비청구 #보험비밀노트"""
