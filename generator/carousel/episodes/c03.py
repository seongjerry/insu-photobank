# 캐러셀 c03 · 보험사가 먼저 말 안 해주는 것 ② 의료자문 동의서
# 커뮤니티 키워드: 블라인드 "의료자문 동의해야 지급한다네요", "의료자문 동의한 사람 대다수가 부지급", 클리앙 보험 게시판 의료자문 질문
# 언론 이슈: IB토마토 연재 "(의료자문 두 얼굴)" 2026.10.16 / FETV [2026 국감] 의료자문 부지급 증가 2026.10.6
# 공식·교차 출처:
#  - 생보사 의료자문 부지급률 30.8% (2025년 하반기, 생명보험협회 공시): IB토마토 2026.10.16 (8,806건 중 2,716건) / CEO스코어데일리 2026.7.16 (평균 30.84%)
#  - 대형 3개 생보사 평균 24.2% (2026년 상반기, 생명보험협회 공시): FETV 2026.10.6 / 토요경제(sateconomy) 기사 제목
#  - 금융감독원·대한의사협회 제3의료자문 업무협약 2026.2.4: 머니투데이·데일리팜·헤럴드경제 (정액형 뇌·심혈관·정형외과 후유장해 시범, 실손 제외, 재자문 비용 보험사 부담)
#  - 약관 제3자 판정 조항(종합병원 전문의 중 함께 정함, 비용 회사 부담), 보험업감독업무시행세칙 피해구제 절차 안내(2020.10)
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "보험사가 먼저 말 안 해주는 것 ②"
TOPIC = "보험사가 의료자문 동의하래요, 서명 전에 확인할 것"
SOURCES = ["https://www.ibtomato.com/ExternalView.aspx?no=19810&type=1 (2026.10.16, 생명보험협회 의료자문 공시)",
           "https://www.ceoscoredaily.com/page/view/2026071316470852516 (2026.7.16, 2025 하반기 생보 평균 30.84%)",
           "https://www.fetv.co.kr/news/articleView.html?idxno=311244 (2026.10.6, 대형 3사 24.2%)",
           "https://www.mt.co.kr/finance/2026/02/04/2026020414260712936 (금감원·의협 제3의료자문 협약)",
           "https://m.dailypharm.com/user/news/335450 (재자문 비용 보험사 부담)",
           "https://www.teamblind.com/kr/post/백내장-수술-보험료-부지급-의료자문-2ZM8CzX3 (주제 발굴)"]

S = []
# 1 표지 (A2: 사진 위 + 제목 아래, 질문형)
S.append(cover(layout_for(3),
               "보험사가<br>'<span class=\"y\">의료자문</span>' 하재요<br>동의해도 되나요?",
               chip="보험금 청구했더니 이런 연락이 왔다면",
               sub="서명하기 전에 이 노트부터 보세요",
               photo="photos/hospital/pixabay_563427.jpg", accent="y"))

# 2 의료자문이 뭔가요
S.append(f"""
 <h2>의료자문,<br>정확히 <span class="y">뭔가요?</span></h2>
 {bino('think', 230, 'position:absolute;right:64px;top:150px')}
 <p class="lead">보험사가 <b>내 주치의가 아닌 다른 의사</b>에게<br>내 진료 기록을 보내 의견을 묻는 거예요.</p>
 <div class="rows">
  <div class="row box"><div class="num">1</div><div><h3>환자를 직접 보지 않아요</h3><p>자문의는 대부분 보험사가 보낸 진료기록·검사 자료만 보고 판단해요.</p></div></div>
  <div class="row box"><div class="num">2</div><div><h3>주치의와 의견이 다를 수 있어요</h3><p>주치의는 "치료가 필요했다", 자문의는 "필요하지 않았다"처럼 갈릴 때가 있어요.</p></div></div>
  <div class="row box"><div class="num">3</div><div><h3>그 의견이 지급 판단 근거가 돼요</h3><p>자문 결과를 근거로 보험금을 깎거나(감액) 안 주는(부지급) 경우가 생겨요.</p></div></div>
 </div>
 <div class="src">보험사·상품에 따라 자문 절차는 다를 수 있어요.</div>""")

# 3 숫자 (움직이는 장)
S.append(f"""
 <h2>자문 받으면<br><span class="r">얼마나 거절</span>될까요?</h2>
 <p class="lead">생명보험사에서 의료자문을 거친 청구 중<br>보험금을 <b>아예 못 받은</b> 비율이에요.</p>
 <div class="box" style="margin-top:28px;text-align:center;padding:30px 20px 32px">
  <p style="font-size:30px;color:#9E9E9E;font-weight:700">생보사 의료자문 후 부지급률 (2025년 하반기)</p>
  <div id="big" style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:168px;line-height:1.05;color:#FF6B6B;margin-top:6px">30.8%</div>
  <div id="dots" style="display:flex;justify-content:center;gap:14px;margin-top:18px"></div>
  <p style="font-size:32px;color:#fff;font-weight:800;margin-top:22px">자문 10건 중 3건은 <span class="r">0원</span></p>
 </div>
 <div class="stat">
  <div class="box"><div class="k">대형 3개 생보사 평균</div><div class="v y">24.2%</div><div class="d">2026년 상반기</div></div>
  <div class="box"><div class="k">일부만 주는 감액</div><div class="v b" style="font-size:56px;line-height:1.45">별도 집계</div><div class="d">부지급률엔 안 들어가요</div></div>
 </div>
 <div class="src">출처: 생명보험협회 의료자문 공시 (IB토마토·CEO스코어데일리·FETV 보도)</div>""")

# 4 비교표: 보험사 자문 vs 제3의료자문
S.append(f"""
 <h2>결과가 억울하면<br><span class="y">다시 물어볼 수 있어요</span></h2>
 <table>
  <thead><tr><th style="width:24%"></th><th>보험사 의료자문</th><th class="new">제3의료기관 자문</th></tr></thead>
  <tbody>
   <tr><th>언제</th><td>보험사가 필요하다고 볼 때</td><td>내가 결과에 이의를 제기할 때</td></tr>
   <tr><th>의사 선택</th><td>보험사가 정한 곳</td><td>나와 보험사가 <b>함께</b> 정해요</td></tr>
   <tr><th>비용</th><td>보험사 부담</td><td><b class="y">보험사 전액 부담</b></td></tr>
   <tr><th>새로 바뀌는 점</th><td>보험사가 낸 병원 목록 안에서 골랐어요</td><td><b>의사협회</b>를 자문기관으로 고르는 방식 추진 <span class="tag">시범</span></td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:26px;padding:24px 30px"><p style="font-size:29px;color:#E0E0E0;line-height:1.45"><b class="y">시범 대상</b>: 정해진 금액을 주는 정액형 보험 중 <b>뇌·심혈관</b>, <b>정형외과 후유장해</b> 자문. 실손보험은 빠져 있어요.</p></div>
 <div class="box" style="margin-top:20px;padding:24px 30px;border-color:#FFE45C"><p style="font-size:29px;color:#E0E0E0;line-height:1.45"><b class="y">약관에도 적혀 있어요</b><br>지급 사유에 의견이 다르면 종합병원 전문의 중 제3자를 <b>함께</b> 정해 의견을 따를 수 있고, 그 비용은 보험사가 내요. 보험사도 이의 제기 절차를 안내해야 해요.</p></div>
 <div class="src">금융감독원·대한의사협회 제3의료자문 업무협약 (2026.2.4)<br>시범 운영 후 확대 예정, 세부 조건은 보험사에 확인하세요.</div>""")

# 5 서명 전 확인 5가지
S.append(f"""
 <h2>동의서 서명 전<br><span class="y">이것부터 물어보세요</span></h2>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>"왜 자문이 필요한가요?"</h3><p>어떤 부분이 문제인지(진단, 수술 필요성, 입원 기간 등) 먼저 들어 두세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>"어느 병원·진료과에 묻나요?"</h3><p>내 병과 같은 전문 분야 의사인지 확인하세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">3</div><div><h3>"어떤 기록을 보내나요?"</h3><p>내게 유리한 검사 결과·주치의 소견이 빠지지 않았는지 목록을 받아 보세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">4</div><div><h3>"질문지를 볼 수 있나요?"</h3><p>자문의에게 무엇을 묻는지에 따라 답이 달라질 수 있어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">5</div><div><h3>서명한 서류는 사본으로</h3><p>동의서 사진, 통화 날짜·담당자 이름을 남겨 두세요.</p></div></div>
 </div>""")

# 6 주치의 소견서 먼저
S.append(f"""
 <h2>제일 센 무기는<br><span class="b">주치의 소견서</span>예요</h2>
 <p class="lead">자문의는 기록만 보지만, <b>주치의는 나를 직접 진료</b>했어요.<br>자문 전에 미리 내 두면 판단 자료가 달라져요.</p>
 <div class="note" style="margin-top:40px;padding:34px 40px 38px;transform:rotate(-1.5deg)">
  <div style="font-size:30px;margin-bottom:14px">소견서에 담아 달라고 할 것</div>
  <div class="ck" style="font-size:48px;gap:10px">
   <span>진단 근거 (검사 결과 수치)</span>
   <span>이 치료·수술이 필요했던 이유</span>
   <span>입원이 이만큼 필요했던 이유</span>
   <span>다른 치료로 대신 못 한 이유</span>
  </div>
 </div>
 <div class="box" style="margin-top:40px"><p style="font-size:30px;color:#E0E0E0;line-height:1.45">자문 결과가 이미 불리하게 나왔다면?<br>그 결과에 대한 <b class="y">반박 소견서</b>를 받아 재심사를 요청할 수 있어요.</p></div>
 <div class="src">소견서 발급 비용·양식은 병원마다 달라요.</div>""")

# 7 불리한 결과 나왔을 때 순서
S.append(f"""
 <h2>거절·감액 통보를 받았다면<br><span class="y">이 순서로</span></h2>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>자문 결과 설명·회신서 요청</h3><p>어떤 근거로 거절했는지 서면으로 받아 두세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>주치의 반박 소견서로 재심사</h3><p>자문 내용 중 사실과 다른 부분을 짚어 달라고 하세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">3</div><div><h3>제3의료기관 자문 요청</h3><p>보험사와 함께 의사를 정하고, 비용은 보험사가 내요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">4</div><div><h3>금융감독원 분쟁조정 (1332)</h3><p>신청 비용은 무료예요. 온라인으로도 접수돼요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">5</div><div><h3>손해사정사 직접 선임 검토</h3><p>보험사 쪽이 아닌 내 편 손해사정사를 둘 수 있어요.</p></div></div>
 </div>
 <div class="src">약관 제3자 판정 조항, 금융감독원 분쟁조정 안내 기준. 보험사·상품에 따라 다를 수 있어요.</div>""")

# 8 Q&A + 보너스 + 다음 편
S.append(f"""
 <h2>헷갈리는 질문<br><span class="b">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:20px;gap:12px">
  <div class="box"><div class="q">동의 안 하면 어떻게 되나요?</div><div class="a">심사가 길어지거나 지급이 늦어질 수 있어요. 바로 거부하기보다 5가지를 확인한 뒤 정하세요.</div></div>
  <div class="box"><div class="q">실손보험도 의사협회 고를 수 있나요?</div><div class="a">시범 대상에서 실손은 빠져 있어요. 이의가 있으면 약관의 제3자 판정 절차를 물어보세요.</div></div>
  <div class="box"><div class="q">보험사별 거절 비율도 볼 수 있나요?</div><div class="a">생명·손해보험협회 공시실에 회사별 의료자문 현황이 올라와요.</div></div>
  <div class="box"><div class="q">심사가 길어져 돈이 급하면요?</div><div class="a">보험사에 가지급보험금(일부 먼저 받기)이 되는지 물어보세요.</div></div>
 </div>
 <div style="display:flex;gap:24px;align-items:flex-end;margin-top:22px">
  <div class="note" style="flex:1;font-size:36px;transform:rotate(-1.5deg)">다음 노트 ③<br>보험금 거절 통보 받은 날 할 일</div>
  {bino('shh', 180)}
 </div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">이 노트,<br><span class="y">보험금 청구할 가족에게</span></h2>
 <div class="note" style="margin-top:44px;padding:36px 40px 40px">
  <div style="font-size:32px;margin-bottom:10px">의료자문 체크</div>
  <div class="ck"><span>왜 자문하는지 먼저 묻기</span><span>보내는 기록 목록 확인</span><span>주치의 소견서 먼저 내기</span><span>결과는 서면으로 받기</span><span>억울하면 제3의료기관</span></div>
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">"동의해야 지급된대요"</p><p style="font-size:30px;margin-top:10px">이 말 듣고 바로 서명하기 전에, 저장해 두고 하나씩 확인하세요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 개별 사안은 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4, "still_t": 3.6, "js": """
(function(){const d=$('#dots');for(let i=0;i<10;i++){const e=document.createElement('div');e.style.cssText='width:46px;height:46px;border-radius:50%;background:#3A3A3A';d.appendChild(e);}})();
window.setT=function(t){
 const p=eo(c((t-0.2)/1.6));
 $('#big').textContent=(30.8*p).toFixed(1)+'%';
 const ds=$('#dots').children;
 for(let i=0;i<10;i++){const on=i<3&&t>(1.9+i*0.25);ds[i].style.background=on?'#FF6B6B':'#3A3A3A';ds[i].style.transform='scale('+(on?1+0.25*Math.max(0,1-(t-(1.9+i*0.25))*4):1)+')';}
};"""},
}

CAPTION = """보험금 청구했더니
"의료자문 동의하셔야
지급돼요" 이런 연락
받아 보셨나요?

의료자문은 주치의가 아닌
다른 의사가 기록만 보고
의견을 내는 거예요

👉 생보사 자문 후 부지급률
2025년 하반기 30.8%
👉 서명 전 물어볼 것 5가지
👉 주치의 소견서를 먼저
👉 억울하면 제3의료기관 자문
비용은 보험사 부담

금감원과 의사협회가
소비자가 자문기관을 고르는
시범 운영도 준비했어요

보험금 청구할 가족에게
미리 공유해 주세요

다음 노트 ③
보험금 거절 통보 받은 날

#의료자문 #보험금청구 #보험금거절 #부모님보험 #보험비밀노트"""
