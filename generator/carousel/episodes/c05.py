# 캐러셀 c05 · 몰라서 못 받는 보험금 ② 숨은 보험금 찾는 법
# 커뮤니티 키워드: "내 이름으로 잠든 돈", "숨은 보험금 찾기 내보험찾아줌 후기", "잠자는 보험금 조회" (네이버 블로그·재테크 블로그 반복, 위키트리 2026.10)
#   + 생명보험협회 '숨은보험금 찾아주기' 캠페인 시작 보도(경향신문 2026.10.27). c01·c04 에서 다음 편으로 예고한 주제
# 공식·교차 출처:
#  - 잔액 10조3천억 원(2025년 말), 2022 12.4조 · 2023 12.1조 · 2024 11.2조: 금융위원회 보도자료 2026.7.8(KDI 경제정보센터 수록) / 경향신문 2026.10.27 / 헤럴드경제 2026.7.6
#  - 2025년 환급 3조2,470억 원·80만 건·건당 평균 404만 원: 금융위원회 2026.7.8 / 헤럴드경제 2026.7.6 / SBS Biz 2026.7.7
#  - 중도·만기·휴면 정의, 만기 후 3년 지나면 휴면, 휴면은 이자 없음: SBS Biz 2026.7.7 / 금융위원회 주요정책문답(2025.6.30)
#  - 만기 후 1년 이내 이자 평균공시이율(예정·공시이율)의 50%: 금융위원회 주요정책문답 2025.6.30 / 정책브리핑 2021.11.5 (둘 다 표준약관 예시)
#  - 내보험찾아줌 cont.insure.or.kr·cont.knia.or.kr, 본인인증 후 24시간, 마케팅 미사용, 유사 사이트 주의: 금융위원회 주요정책문답 2025.6.30 / 금융위 2026.7.8
#  - 사망자 보험: 상속인 금융거래조회·안심상속 원스톱(사망일이 속한 달 말일부터 1년 이내) 후 조회, 청구는 보험사: 금융위원회 주요정책문답 2025.6.30 / SBS Biz 2026.7.7
#  - 서민금융진흥원 출연 휴면보험금: 1397, 서민금융 잇다 앱: 금융위원회 주요정책문답 2025.6.30
#  - 미청구 이유(발생 사실 모름, 만기 후에도 높은 이자가 붙는 줄 앎): 경향신문 2026.10.27 / 행안부 협조 최신 주소 안내: 금융위 2026.7.8
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "몰라서 못 받는 보험금 ②"
TOPIC = "내 이름으로 잠든 숨은 보험금, 찾는 순서"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=283914 (금융위원회 2026.7.8 숨은보험금 집중 안내)",
           "https://khan.co.kr/article/202610271607001 (경향신문 2026.10.27, 잔액 추이·캠페인)",
           "https://www.heraldk.com/article/2026070620001476738 (헤럴드경제 2026.7.6, 환급 실적)",
           "https://biz.sbs.co.kr/amp/article/20000321151 (SBS Biz 2026.7.7, 종류·휴면 이자)",
           "https://fsc.go.kr/po020201/84836 (금융위원회 주요정책문답 2025.6.30, 이자·조회·상속인)",
           "https://www.korea.kr/news/policyNewsView.do?newsId=148895182 (정책브리핑 2021.11.5, 이자 기준)",
           "https://www.wikitree.co.kr/articles/1145190 (주제 발굴)"]

S = []
# 1 표지 (A1: 사진 전면 + 하단 제목, 비밀형)
S.append(cover(layout_for(5),
               "내 이름으로 잠든<br>'이 돈', 아직<br><span class=\"y\">10조 원</span>이 넘어요",
               chip="부모님 것까지 같이 찾아보세요",
               photo="photos/elderly/pixabay_4561704.jpg", accent="y"))

# 2 왜 안 찾아갈까
S.append(f"""
 <h2>내 돈인데<br><span class="y">왜 안 찾아갈까요?</span></h2>
 <p class="lead">숨은 보험금은 <b>받을 금액이 이미 정해졌는데</b><br>아무도 청구하지 않아 남아 있는 돈이에요.</p>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>생긴 줄도 몰라요</h3><p>축하금·학자금·건강자금 같은 중도보험금, 만기보험금이 생겼다는 사실 자체를 모르는 경우가 가장 많아요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>두면 이자가 붙는 줄 알아요</h3><p>만기가 지나면 이자가 크게 줄어요. 3년이 더 지나면 이자가 아예 없어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">3</div><div><h3>안내를 못 받았어요</h3><p>이사·번호 변경으로 우편과 문자가 엉뚱한 곳으로 가요. 그래서 정부가 최신 주소를 확인해 다시 안내하고 있어요.</p></div></div>
 </div>
 <div class="box" style="margin-top:22px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:30px;color:#E0E0E0;line-height:1.45">2025년 말 기준 아직 주인을 못 찾은 돈이 <b class="y">10조3천억 원</b>이에요.</p></div>
 <div class="src">출처: 금융위원회 보도자료(2026.7.8), 경향신문(2026.10.27)</div>""")

# 3 숫자 (움직이는 장)
S.append(f"""
 <h2>줄고는 있지만<br><span class="r">아직 이만큼</span> 남았어요</h2>
 <p class="lead">해마다 연말 기준 숨은 보험금 잔액이에요.</p>
 <div class="box" style="margin-top:26px;padding:30px 34px 26px">
  <div style="display:flex;align-items:flex-end;justify-content:space-around;height:330px;gap:28px">
   <div style="flex:1;text-align:center"><div style="font-family:Kkakdugi,Paperlogy;font-size:38px;font-weight:700;color:#BDBDBD">12.4조</div><div id="g1" style="height:300px;background:#3A3A3A;border-radius:12px 12px 0 0;margin-top:8px"></div></div>
   <div style="flex:1;text-align:center"><div style="font-family:Kkakdugi,Paperlogy;font-size:38px;font-weight:700;color:#BDBDBD">12.1조</div><div id="g2" style="height:293px;background:#3A3A3A;border-radius:12px 12px 0 0;margin-top:8px"></div></div>
   <div style="flex:1;text-align:center"><div style="font-family:Kkakdugi,Paperlogy;font-size:38px;font-weight:700;color:#BDBDBD">11.2조</div><div id="g3" style="height:271px;background:#3A3A3A;border-radius:12px 12px 0 0;margin-top:8px"></div></div>
   <div style="flex:1;text-align:center"><div style="font-family:Kkakdugi,Paperlogy;font-size:44px;font-weight:700;color:#FF6B6B">10.3조</div><div id="g4" style="height:249px;background:#FF6B6B;border-radius:12px 12px 0 0;margin-top:8px"></div></div>
  </div>
  <div style="display:flex;justify-content:space-around;gap:28px;border-top:3px solid #555;padding-top:12px;font-size:27px;color:#9E9E9E;font-weight:700;text-align:center">
   <span style="flex:1">2022</span><span style="flex:1">2023</span><span style="flex:1">2024</span><span style="flex:1;color:#fff">2025</span>
  </div>
 </div>
 <div class="stat" style="margin-top:22px">
  <div class="box"><div class="k">작년에 찾아간 돈</div><div class="v y" id="ref" style="font-size:66px">3조2470억</div><div class="d">80만 건</div></div>
  <div class="box"><div class="k">한 건당 평균</div><div class="v y" id="avg" style="font-size:66px">404만 원</div><div class="d">2025년 청구 기준</div></div>
 </div>
 <div class="src">출처: 금융위원회(2026.7.8), 경향신문(2026.10.27)·헤럴드경제(2026.7.6) 보도</div>""")

# 4 비교표
S.append(f"""
 <h2>숨은 보험금은<br><span class="y">세 종류</span>예요</h2>
 <table>
  <thead><tr><th style="width:19%"></th><th>중도보험금</th><th>만기보험금</th><th class="new">휴면보험금</th></tr></thead>
  <tbody>
   <tr><th>뭔가요</th><td>계약 중간에 나오는 돈 (축하금·학자금·건강자금·생존연금)</td><td>만기가 됐는데 안 찾아간 돈</td><td>만기 후 3년이 지나 시효가 끝난 돈</td></tr>
   <tr><th>이자</th><td>약관 이율대로 붙다가 만기 후 줄어요</td><td>만기 후 1년까지 공시이율의 50% 수준, 이후 더 낮아져요</td><td><b class="r">이자 없음</b></td></tr>
   <tr><th>누가 보관</th><td>보험사</td><td>보험사</td><td>보험사 또는 서민금융진흥원</td></tr>
   <tr><th>어디서 찾나</th><td colspan="2">내보험찾아줌에서 조회·청구</td><td>내보험찾아줌, 서민금융진흥원(1397)</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:24px;padding:24px 30px;border-color:#FFE45C"><p style="font-size:30px;color:#E0E0E0;line-height:1.45"><b class="y">휴면이 돼도 사라지진 않아요</b><br>시효가 끝나도 보관하는 곳에서 돌려받을 수 있어요. 다만 이자가 없으니 미룰 이유가 없어요.</p></div>
 <div class="src">이자는 생명보험 표준약관 예시 기준. 보험사·상품에 따라 다를 수 있어요.</div>""")

# 5 범위 넓히기: 이자 줄어드는 흐름 + 돌아가신 분 보험
S.append(f"""
 <h2>미룰수록 <span class="r">이자가</span><br><span class="r">줄어들어요</span></h2>
 <div class="box" style="margin-top:28px;padding:26px 32px">
  <p style="font-size:32px;color:#9E9E9E;font-weight:700">만기보험금 이자 흐름 (표준약관 예시)</p>
  <div style="display:flex;height:84px;border-radius:14px;overflow:hidden;margin-top:22px;font-size:30px;font-weight:800;color:#121212;text-align:center;line-height:84px">
   <div style="flex:1;background:#FFE45C">만기 전</div><div style="flex:1;background:#C9B84A">1년 이내</div><div style="flex:1.4;background:#7A7330;color:#fff">1~3년</div><div style="flex:1.2;background:#3A3A3A;color:#FF6B6B">3년 후</div>
  </div>
  <div style="display:flex;margin-top:16px;font-size:29px;color:#D6D6D6;text-align:center;line-height:1.35">
   <div style="flex:1">약관 이율</div><div style="flex:1">공시이율의<br>50%</div><div style="flex:1.4">더 낮아짐</div><div style="flex:1.2;color:#FF6B6B">휴면<br>이자 0</div>
  </div>
 </div>
 <div class="box" style="margin-top:24px;padding:26px 32px">
  <p style="font-size:36px;color:#fff;font-weight:800">돌아가신 부모님 보험도 찾을 수 있어요</p>
  <div class="rows" style="gap:18px;margin-top:20px">
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">1</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0"><b class="y">상속인 금융거래조회</b> 또는 <b class="y">안심상속 원스톱</b>을 먼저 신청해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">2</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">받은 접수번호로 내보험찾아줌에서 보험 내역을 조회해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">3</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">청구는 사이트에서 안 되니 해당 보험사에 직접 해요.</p></div></div>
  </div>
 </div>
 <div class="note" style="margin-top:48px;font-size:36px;transform:rotate(-1.5deg)">안심상속 원스톱은 사망일이 속한 달의<br>말일부터 1년 안에 신청해야 해요</div>
 <div class="src">출처: 금융위원회 주요정책문답(2025.6.30), SBS Biz(2026.7.7)</div>""")

# 6 찾는 순서
S.append(f"""
 <h2>지금 폰으로<br><span class="y">이 순서대로</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 28px"><div class="num">1</div><div><h3>'내보험찾아줌' 접속</h3><p>cont.insure.or.kr 또는 cont.knia.or.kr. 생명·손해보험협회가 함께 운영해요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">2</div><div><h3>본인인증</h3><p>휴대폰 간편인증·공동인증서로 24시간 언제든 돼요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">3</div><div><h3>숨은 보험금 조회</h3><p>가입 내역과 숨은 보험금이 한 번에 떠요. 잊고 있던 보험도 확인하세요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">4</div><div><h3>보험사·지급 사유 확인</h3><p>중도·만기·휴면 중 무엇인지, 금액과 이자 조건을 봐요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">5</div><div><h3>청구하고 입금 확인</h3><p>살아 있는 본인 보험금은 사이트에서 청구까지 돼요. 보험사 확인 후 입금돼요.</p></div></div>
 </div>
 <div class="src">출처: 금융위원회 주요정책문답(2025.6.30)·보도자료(2026.7.8)</div>""")

# 7 Q&A
S.append(f"""
 <h2>헷갈리는 질문<br><span class="b">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:24px;gap:14px">
  <div class="box"><div class="q">부모님 것을 제가 조회할 수 있나요?</div><div class="a">본인인증이 필요해요. 부모님 휴대폰으로 함께 인증해서 조회하세요.</div></div>
  <div class="box"><div class="q">중도보험금은 두면 이득 아닌가요?</div><div class="a">이자는 상품 약관마다 달라요. 약관 이율을 먼저 보고 받을 때를 정하세요.</div></div>
  <div class="box"><div class="q">휴면보험금이 내보험찾아줌에 없어요</div><div class="a">서민금융진흥원으로 넘어갔을 수 있어요. 1397이나 '서민금융 잇다' 앱에서 확인하세요.</div></div>
  <div class="box"><div class="q">조회하면 보험 권유 전화 오나요?</div><div class="a">내보험찾아줌은 입력 정보를 마케팅에 쓰지 않아요. 전화가 온다면 비슷하게 만든 다른 사이트일 수 있어요.</div></div>
  <div class="box"><div class="q">보험사에서 안내 우편이 왔어요</div><div class="a">정부가 행정안전부 협조로 최신 주소를 찾아 우편·모바일로 안내하고 있어요. 금액은 내보험찾아줌에서 직접 확인하세요.</div></div>
 </div>
 <div class="src">출처: 금융위원회 주요정책문답(2025.6.30)·보도자료(2026.7.8)</div>""")

# 8 주의 + 다음 편
S.append(f"""
 <h2>이런 문자는<br><span class="r">누르지 마세요</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 28px"><div class="num" style="background:#FF6B6B">!</div><div><h3>"숨은 보험금 있어요" 링크 문자</h3><p>링크로 들어가 주민번호·계좌를 넣지 말고, 주소창에 직접 입력해 들어가세요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num" style="background:#FF6B6B">!</div><div><h3>주소가 다른 비슷한 사이트</h3><p>공식 주소는 cont.insure.or.kr · cont.knia.or.kr 이에요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num" style="background:#FF6B6B">!</div><div><h3>대신 찾아 준다며 정보 요구</h3><p>내보험찾아줌 조회·청구는 본인이 직접 할 수 있어요.</p></div></div>
 </div>
 <div style="display:flex;gap:24px;align-items:flex-end;margin-top:30px">
  <div class="note" style="flex:1;font-size:36px;transform:rotate(-1.5deg)">다음 노트<br>보험료 버거울 때, 해지 말고 이것부터</div>
  {bino('money', 220)}
 </div>
 <div class="src" style="padding-bottom:96px;margin-top:14px">출처: 금융위원회 주요정책문답(2025.6.30) 유사 사이트 주의 안내</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">이 노트,<br><span class="y">부모님께 보내 주세요</span></h2>
 <div class="note" style="margin-top:44px;padding:36px 40px 40px">
  <div style="font-size:32px;margin-bottom:10px">숨은 보험금 체크</div>
  <div class="ck"><span>내보험찾아줌 내 것 조회</span><span>부모님 것도 같이 조회</span><span>중도·만기 이자 조건 확인</span><span>휴면은 1397에서도 확인</span><span>링크 문자는 누르지 않기</span></div>
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">"우리 집엔 없겠지"</p><p style="font-size:30px;margin-top:10px">조회는 무료예요. 명절 전에 가족이 같이 한 번씩 해 보세요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 개별 금액과 이자는 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4, "still_t": 3.6, "js": """
const H=[300,293,271,249];
window.setT=function(t){
 for(let i=0;i<4;i++){const p=eo(c((t-0.2-i*0.3)/0.9));document.getElementById('g'+(i+1)).style.height=(H[i]*p)+'px';}
 const q=eo(c((t-1.1)/1.1));
 const r=Math.round(32470*q);$('#ref').textContent=(r>=10000?Math.floor(r/10000)+'조'+(r%10000):r)+'억';
 $('#avg').textContent=Math.round(404*q)+'만 원';
};"""},
}

CAPTION = """내 이름으로 잠든 보험금
아직 10조 원이 넘어요

작년에 찾아간 돈만
3조2470억 원, 80만 건
한 건당 평균 404만 원이에요

👉 중도·만기·휴면 세 종류
👉 만기 지나면 이자 뚝
👉 3년 더 지나면 이자 0
👉 내보험찾아줌에서 조회
👉 돌아가신 분 보험도 확인

조회는 무료예요
부모님 것까지 같이 찾아보세요

부모님께 공유해 주세요

다음 노트
보험료 버거울 때, 해지 말고 이것부터

#숨은보험금 #내보험찾아줌 #휴면보험금
#부모님보험 #보험비밀노트"""
