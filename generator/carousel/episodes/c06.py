# 캐러셀 c06 · 해지·갈아타기 전에 ① 보험료 버거울 때 해지 말고 이것부터
# 커뮤니티 키워드: "보험료 부담돼서 해지 고민", "해지환급금 원금 반도 안 돼요", "보험 갈아타라는데" (블로그·재테크 커뮤니티·지식iN형 질문 반복, 2026.11 조사)
#   + 금감원 부당승환 소비자경보(2026.5, 1분기 민원 211건) 이후 "갈아타기 권유" 글 증가. c05 에서 다음 편으로 예고한 주제
# 공식·교차 출처:
#  - 중도해지 시 해약환급금이 낸 보험료보다 적거나 없을 수 있음, 해지 후 보장 없음, 해지 전 계약대출·자동대출납입·납입유예·감액완납 먼저: 금융감독원 금융꿀팁 200선 139번(2023.1.4, KDI 경제정보센터 수록) / 뉴스핌 2023.1.3
#  - 계약대출: 순수보장성 제외 대부분 가능, 해약환급금 범위, 별도 이자, 신용조회 없음·중도상환 수수료 없음, 이자 미납으로 대출원리금이 환급금 넘으면 해지될 수 있음: 금감원 금융꿀팁(2023.1.4) / 뉴스핌 2023.1.3
#  - 감액·감액완납·연장정기·납입유예·자동대출납입 정의와 주의(환급금 부족 시 해지될 수 있음, 대출 이자): 생명보험협회 안내(MTN 2023.9.6) / KB 금융 가이드(2026.6.11) / 금감원(토요경제 2018.2.1 감액 예시)
#  - 부활: 해약환급금을 받지 않은 계약, 해지 후 3년 이내, 밀린 보험료+이자, 보험사 심사로 거절될 수 있음, 실효 기간 사고 보장 안 됨: 금감원 금융꿀팁(2023.1.4) / 뉴스핌 2023.1.3 / 손해보험협회 소비자포털 FAQ(아이베이비뉴스 정리)
#  - 출산·육아 3종 세트: 2026년 4월 전 보험사 시행, 본인·배우자 출산 1년 이내 또는 육아휴직·근로시간 단축 중, 보장성 보험료 6개월 또는 1년 납입유예(별도 이자 없음, 보장 유지), 계약대출 이자 상환 최대 1년 유예, 어린이보험 1~5% 할인, 기존 계약 적용, 계약당 1회, 변액 등 일부 제외: 금융위원회 2026.3.31 발표(경북매일·메트로신문 2026.3.31)
#  - 부당승환 소비자경보 '주의', 2026년 1분기 민원 211건(직전 분기 137건 대비 54% 증가), 면책기간 재적용·보험료 상승·가입 거절, 비교안내 확인서 확인: 금융감독원 2026.5 (KDI 경제정보센터) / 이투데이·조세금융신문 2026.5.12
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "해지·갈아타기 전에 ①"
TOPIC = "보험료 버거울 때 해지 말고 쓸 수 있는 방법"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=234219 (금융감독원 금융꿀팁 200선 139, 2023.1.4)",
           "https://www.newspim.com/news/view/20230103000237 (뉴스핌 2023.1.3, 계약대출·부활 세부)",
           "https://news.mtn.co.kr/news-detail/2023090610035532931 (생명보험협회 안내, MTN 2023.9.6)",
           "https://kbthink.com/insurance-guide/reduce-premium.html (2026.6.11, 유예·감액완납·연장정기)",
           "https://www.ibabynews.com/qa/ins-knia-reinstate-lapsed-insurance (손해보험협회 FAQ 정리, 부활)",
           "https://kbmaeil.com/article/20260331500817 (금융위 출산·육아 3종 세트, 2026.3.31)",
           "https://www.metroseoul.co.kr/article/20260331500225 (메트로신문 2026.3.31, 3종 세트 교차)",
           "https://eiec.kdi.re.kr/policy/materialView.do?num=280891 (금융감독원 부당승환 소비자경보 2026.5)",
           "https://tfmedia.co.kr/news/article.html?no=204452 (조세금융신문 2026.5.12, 민원 211건)",
           "https://m.etoday.co.kr/news/view/2583493 (이투데이 2026.5.12, 소비자 유의사항)"]

S = []
# 1 표지 (B1: 제목 위 + 비노 가운데, 반전형)
S.append(cover(layout_for(6), "보험료 버거워서<br><span class=\"r\">해지</span>하려고요?",
               chip="해지 버튼 누르기 전에 이것부터", pose="angry", accent="y"))

# 2 왜 해지가 손해인가
S.append(f"""
 <h2>해지하면<br><span class="r">세 번 손해</span>예요</h2>
 <p class="lead">보험료가 부담돼서 해지를 고민하는 분이 많아요.<br>그런데 해지는 <b>되돌리기 가장 어려운 선택</b>이에요.</p>
 <div class="rows" style="gap:16px;margin-top:28px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>낸 돈보다 적게 돌려받아요</h3><p>사업비 등이 빠져서 해약환급금이 낸 보험료보다 적거나 아예 없을 수 있어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>보장이 그날로 끊겨요</h3><p>해지한 다음 날 아프거나 다쳐도 그 보험으로는 받을 수 없어요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">3</div><div><h3>다시 들기 어려워요</h3><p>나이가 들면 보험료가 오르고, 그사이 병원 기록이 생기면 가입이 거절되거나 일부 보장이 빠질 수 있어요. 암보험 등은 면책기간도 다시 시작돼요.</p></div></div>
 </div>
 <div class="box" style="margin-top:22px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:30px;color:#E0E0E0;line-height:1.45">그래서 금융감독원도 <b class="y">해지 전에 다른 방법부터</b> 보라고 안내해요.</p></div>
 <div class="src">출처: 금융감독원 금융꿀팁(2023.1.4), 금융감독원 소비자경보(2026.5)</div>""")

# 3 상황별로 고르기 (움직이는 장)
S.append(f"""
 <h2>해지 말고 쓸 수 있는<br><span class="y">6가지 길</span>이 있어요</h2>
 <div style="display:flex;flex-direction:column;gap:16px;margin-top:24px">
  <div class="box" id="m1" style="padding:20px 30px"><p style="font-size:30px;color:#9E9E9E;font-weight:700">당장 목돈이 필요해요</p>
   <div style="display:flex;gap:12px;margin-top:12px;flex-wrap:wrap"><span class="chip">보험계약대출</span></div>
   <p style="font-size:28px;margin-top:12px;color:#BDBDBD">보험은 그대로 두고 해약환급금 안에서 빌려요</p></div>
  <div class="box" id="m2" style="padding:20px 30px"><p style="font-size:30px;color:#9E9E9E;font-weight:700">몇 달만 버티면 돼요</p>
   <div style="display:flex;gap:12px;margin-top:12px;flex-wrap:wrap"><span class="chip">납입유예</span><span class="chip">자동대출납입</span></div>
   <p style="font-size:28px;margin-top:12px;color:#BDBDBD">잠깐 쉬거나, 쌓인 돈으로 대신 내요</p></div>
  <div class="box" id="m3" style="padding:20px 30px;border-color:#FF6B6B"><p style="font-size:30px;color:#9E9E9E;font-weight:700">앞으로 계속은 못 내요</p>
   <div style="display:flex;gap:12px;margin-top:12px;flex-wrap:wrap"><span class="chip" style="background:#FF6B6B">감액</span><span class="chip" style="background:#FF6B6B">감액완납</span><span class="chip" style="background:#FF6B6B">연장정기</span></div>
   <p style="font-size:28px;margin-top:12px;color:#BDBDBD">보장 금액이나 기간을 줄이고 계약은 살려요</p></div>
 </div>
 <div class="note" style="margin-top:34px;font-size:32px;padding:24px 32px;transform:rotate(-1.5deg)">내 상황에 맞는 길부터 찾고<br>그래도 안 될 때 해지를 고민해도 늦지 않아요</div>
 <div class="src">출처: 금융감독원 금융꿀팁(2023.1.4), 생명보험협회 안내(2023.9). 상품마다 쓸 수 있는 방법이 달라요.</div>""")

# 4 비교표
S.append(f"""
 <h2>6가지,<br><span class="y">한눈에 비교</span></h2>
 <table style="font-size:28px;line-height:1.36;margin-top:22px">
  <thead><tr><th style="width:22%;font-size:29px">방법</th><th style="font-size:29px">이렇게 돼요</th><th class="new" style="width:34%;font-size:29px">꼭 확인</th></tr></thead>
  <tbody>
   <tr><th style="color:#fff;font-size:29px;padding:17px 14px">계약대출</th><td>해약환급금 안에서 빌려요. 신용조회 없어요</td><td>이자가 붙어요. 쌓이면 해지될 수 있어요</td></tr>
   <tr><th style="color:#fff;font-size:29px;padding:17px 14px">납입유예</th><td>일정 기간 보험료를 안 내고 유지해요</td><td>쌓인 환급금에서 빠져나가요</td></tr>
   <tr><th style="color:#fff;font-size:29px;padding:17px 14px">자동대출<br>납입</th><td>환급금 범위에서 대출로 보험료를 자동 납부</td><td>대출이라 이자가 쌓여요</td></tr>
   <tr><th style="color:#fff;font-size:29px;padding:17px 14px">감액</th><td>보장 금액을 줄이고 보험료도 줄여요</td><td>줄인 만큼은 해지로 처리돼요</td></tr>
   <tr><th style="color:#fff;font-size:29px;padding:17px 14px">감액완납</th><td>지금 환급금으로 보험료를 끝내요. 기간은 그대로</td><td>보장 금액이 크게 줄 수 있어요</td></tr>
   <tr><th style="color:#fff;font-size:29px;padding:17px 14px">연장정기</th><td>보장 금액은 두고 보장 기간을 줄여요</td><td>주로 종신보험. 기간이 짧아져요</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:22px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:29px;color:#E0E0E0;line-height:1.45"><b class="y">환급금이 거의 없는 순수보장성 보험</b>은<br>계약대출·감액완납이 어려워요. 감액부터 물어보세요.</p></div>
 <div class="src">출처: 금융감독원(2023.1.4), 생명보험협회(2023.9.6). 보험사·상품에 따라 다를 수 있어요.</div>""")

# 5 범위 넓히기: 출산·육아 가정
S.append(f"""
 <h2>아이 낳았거나<br><span class="b">육아휴직 중</span>이라면</h2>
 <p class="lead" style="margin-top:16px">2026년 4월부터 <b>모든 보험사</b>에서 이자 없이 미뤄요.</p>
 <div class="box" style="margin-top:20px;padding:20px 30px">
  <p style="font-size:30px;color:#9E9E9E;font-weight:700">대상</p>
  <p style="font-size:31px;color:#fff;font-weight:700;margin-top:8px;line-height:1.4">본인 또는 배우자가 출산 후 1년 이내,<br>육아휴직·육아기 근로시간 단축 중</p>
 </div>
 <div class="rows" style="gap:12px;margin-top:16px">
  <div class="row box" style="padding:18px 28px"><div class="num" style="background:#7FB2FF">1</div><div><h3>보험료 납입유예</h3><p>보장성 보험료를 6개월 또는 1년 미뤄요. 별도 이자 없고 보장은 그대로예요.</p></div></div>
  <div class="row box" style="padding:18px 28px"><div class="num" style="background:#7FB2FF">2</div><div><h3>계약대출 이자 상환유예</h3><p>최대 1년까지 이자를 미뤄요. 미룬다고 이자가 더 붙지 않아요.</p></div></div>
  <div class="row box" style="padding:18px 28px"><div class="num" style="background:#7FB2FF">3</div><div><h3>어린이보험 할인</h3><p>보험료 1~5% 범위로 1년간 할인돼요. 할인율은 보험사마다 달라요.</p></div></div>
 </div>
 <p style="font-size:27px;color:#BDBDBD;margin-top:14px;line-height:1.4">이미 가입한 보험도 돼요. 계약당 1회, 셋 다 같이 써요. 변액보험 등 일부 제외.</p>
 <div class="src">출처: 금융위원회 발표(2026.3.31), 경북매일·메트로신문 보도</div>""")

# 6 지금 할 순서
S.append(f"""
 <h2>해지 전에<br><span class="y">이 순서대로</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 28px"><div class="num">1</div><div><h3>해약환급금부터 확인</h3><p>보험사 앱·고객센터에서 지금 환급금과 대출 가능 금액을 봐요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">2</div><div><h3>몇 달 문제인지, 계속 문제인지</h3><p>잠깐이면 유예·자동대출납입, 계속이면 감액·감액완납 쪽이에요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">3</div><div><h3>꼭 남길 보장 고르기</h3><p>다시 들기 어려운 보장, 오래된 좋은 조건은 마지막까지 남겨요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">4</div><div><h3>보험사에 쓸 수 있는 제도 문의</h3><p>상품마다 가능한 방법과 조건이 달라요. 바뀌는 보장 금액을 숫자로 받아 두세요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">5</div><div><h3>갈아탈 거면 새 보험 승인 먼저</h3><p>새 계약이 확정된 뒤 기존 보험을 정리해야 보장 공백이 없어요.</p></div></div>
 </div>
 <div class="src">출처: 금융감독원 금융꿀팁(2023.1.4)·소비자경보(2026.5)</div>""")

# 7 Q&A
S.append(f"""
 <h2>헷갈리는 질문<br><span class="b">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:24px;gap:14px">
  <div class="box"><div class="q">한두 달 밀리면 바로 해지되나요?</div><div class="a">보험사가 먼저 납입 독촉(최고) 안내를 해요. 그 기한까지 안 내면 해지돼요. 자동대출납입은 이 기한 전에 신청해야 해요.</div></div>
  <div class="box"><div class="q">계약대출 받으면 보험은 괜찮나요?</div><div class="a">보장은 그대로예요. 다만 이자를 안 내서 원금과 이자가 환급금을 넘으면 계약이 해지될 수 있어요.</div></div>
  <div class="box"><div class="q">납입유예하면 계속 쉬어도 되나요?</div><div class="a">쉬는 동안 쌓인 환급금에서 빠져나가요. 환급금이 바닥나면 계약이 해지될 수 있으니 남은 금액을 확인하세요.</div></div>
  <div class="box"><div class="q">설계사가 더 좋은 걸로 갈아타래요</div><div class="a">비교안내 확인서로 보험기간·보험료·보장·면책을 신·구 계약끼리 비교하고, 설명서와 문자는 보관해 두세요.</div></div>
 </div>
 <div class="src">출처: 금융감독원(2023.1.4·2026.5), 뉴스핌(2023.1.3)·이투데이(2026.5.12) 보도</div>""")

# 8 보너스: 이미 해지됐다면 + 다음 편
S.append(f"""
 <h2>이미 해지됐다면?<br><span class="y">3년 안엔 살릴 수 있어요</span></h2>
 <p class="lead">보험료를 못 내서 해지된 보험은 <b>부활</b>을 신청할 수 있어요.</p>
 <div class="box" style="margin-top:24px;padding:24px 30px">
  <div class="rows" style="gap:16px;margin-top:0">
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">1</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">해지 후 <b class="y">3년 이내</b>, 해약환급금을 <b class="y">안 받은</b> 계약만 돼요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">2</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">밀린 보험료에 이자를 더해 내요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">3</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">새로 가입할 때처럼 건강 상태를 다시 알리고 심사를 받아요. 거절될 수도 있어요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px;background:#FF6B6B">!</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">해지돼 있던 기간에 생긴 사고는 보장되지 않아요.</p></div></div>
  </div>
 </div>
 <div style="display:flex;gap:24px;align-items:flex-end;margin-top:34px">
  <div class="note" style="flex:1;font-size:35px;transform:rotate(-1.5deg)">다음 노트<br>"더 좋은 걸로 갈아타세요" 이 말 들었다면</div>
  {bino('base', 210)}
 </div>
 <div class="src" style="padding-bottom:96px;margin-top:14px">출처: 금융감독원 금융꿀팁(2023.1.4), 손해보험협회 소비자포털 FAQ</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">해지 고민하는 가족에게<br><span class="y">먼저 보내 주세요</span></h2>
 <div class="note" style="margin-top:44px;padding:36px 40px 40px">
  <div style="font-size:32px;margin-bottom:10px">해지 전 체크</div>
  <div class="ck"><span>해약환급금·대출 가능 금액 확인</span><span>몇 달 문제인지 계속 문제인지</span><span>유예·감액·감액완납 문의</span><span>출산·육아휴직이면 3종 세트</span><span>갈아타면 새 보험 승인 먼저</span></div>
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">"그냥 깨 버릴까"</p><p style="font-size:30px;margin-top:10px">해지는 마지막에 해도 늦지 않아요. 보험사에 전화 한 통이 먼저예요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 가능한 방법과 조건은 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4, "still_t": 3.6, "js": """
window.setT=function(t){
 for(let i=1;i<=3;i++){const p=eo(c((t-0.2-(i-1)*0.45)/0.6));const e=document.getElementById('m'+i);
  e.style.opacity=p; e.style.transform='translateX('+((1-p)*-60)+'px)';}
 const q=0.5+0.5*Math.sin(t*2*Math.PI/1.4), on=c((t-1.6)/0.4);
 $('#m3').style.boxShadow='0 0 '+(on*(8+30*q))+'px rgba(255,107,107,'+(on*(0.2+0.4*q))+')';
};"""},
}

CAPTION = """보험료 버거워서
해지하려고요?

해지하면 세 번 손해예요
낸 돈보다 적게 받고
보장은 그날 끊기고
다시 들기도 어려워요

👉 급하면 보험계약대출
👉 잠깐이면 납입유예
👉 계속 힘들면 감액·감액완납
👉 출산·육아휴직이면 이자 없이 유예
👉 해지됐어도 3년 안엔 부활 신청

해지는 마지막에 해도 늦지 않아요
보험사에 전화 한 통이 먼저예요

해지 고민하는 가족에게 공유해 주세요

다음 노트
"더 좋은 걸로 갈아타세요" 이 말 들었다면

#보험해지 #보험료부담 #감액완납
#해약환급금 #보험비밀노트"""
