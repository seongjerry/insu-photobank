# 캐러셀 c13 · 보험사가 먼저 말 안 해주는 것 ④ 검진에서 "두 달 뒤 다시 봅시다" 들었다면 (추적관찰 vs 추가검사)
# 배정: 주간 plan week-2026-11-23 캐러셀 2번(9점), 금요일(11/27) 배정. 수요일 릴스 ep29(같은 사건)의 캐러셀 확장판
# 커뮤니티 키워드: "검진 재검 나왔는데 고지해야 하나요", "추적관찰도 알려야 하나요"
#   (블라인드 '암보험 고지관련 문의'·'고지의무 궁금한게 있습니다' 글, 지식iN·보험 카페의 검진 후 가입 질문, 2026.11 조사)
# 공식·교차 출처:
#  - 금융감독원 보도자료 2026.7.27 (KDI 경제정보센터 284697): 분조위 2026.7.24 결정, '추가검사'는 선행 검사 후 이상소견이 확인돼
#      보다 정확한 진단을 위해 필요한 검사, 단순 경과관찰·정기검사 제외 / '질병으로 인한 입원'은 증상으로 입원치료·관리 필요성이 인정되는 경우, 임상시험 입원 제외
#  - 뉴시스 2026.7.27: 2023.3.14 두 달 후 혈액검사 권유, 2023년 4월 간편심사보험 가입, 2024년 7월 골수형성이상증후군 진단,
#      3개월 이내 추가검사 필요소견 미고지로 해지·부지급, 판단 근거 3가지 / 2022년 3월 가입, 2019.12·2021.4 임상시험 각 1박 2일,
#      2024년 1~2월 입원 간병인 일당, 3년 이내 질병 입원 미고지로 해지, 판단 근거 3가지, 20일 이내 수락
#  - 헤럴드경제·SBS Biz·아시아경제·조세금융신문·데일리안 2026.7.27, 비즈니스워치 2026.8.1: 같은 사실관계, 재판상 화해 효력
#  - MTN 2024.1.2 (금감원 약관 개선): 병증 유지 상태의 정기검사·추적관찰은 추가검사 아님, 일반 청약서 최근 1년 추가검사(재검사)
#  - KB Think 2026.10.29·뱅크샐러드 2026.8.4: 일반심사 3개월(진단·의심소견·치료·입원·수술·투약)/1년(추가검사·재검사)/5년(입원·수술·7일 이상 치료·30일 이상 투약),
#      간편 3개월(입원·수술·추가검사 필요소견)/N년(입원·수술)/5년(암 등), 설계사에게 말로만 한 것은 고지로 인정되지 않을 수 있음(KB Think, korea.legal 모집인 고지수령권)
#  - 상법 제651조(안 날부터 1월, 계약 체결일부터 3년, 보험사가 알았거나 중과실로 모른 경우 해지 불가), 제655조 단서(인과관계)
#      국가법령 조문(korea.legal 전재)·금감원 분쟁조정사례(손보협회 PDF)로 확인
#  - 확인이 1곳뿐인 내용(검진 후 3개월 가입 제한 없음, 정상 결과 추가검사 고지, 약관 보장개시 2년 규정)은 화면에서 뺌
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "보험사가 먼저 말 안 해주는 것 ④"
TOPIC = "검진 '두 달 뒤 다시' 추적관찰 vs 추가검사·분조위 2건(혈액검사·임상시험 입원)·질문표 기간 읽기·가입 전 순서·해지 통보 대응"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=284697 (금융감독원 2026.7.27 분조위 간편심사보험 알릴의무 명확화)",
           "https://www.newsis.com/view/NISX20260727_0003724388 (뉴시스 2026.7.27)",
           "https://www.heraldk.com/article/2026072621463428594 (헤럴드경제 2026.7.27)",
           "https://biz.sbs.co.kr/amp/article/20000324789 (SBS Biz 2026.7.27)",
           "https://www.tfmedia.co.kr/news/article.html?no=206032 (조세금융신문 2026.7.27)",
           "https://news.bizwatch.co.kr/article/finance/2026/07/31/0019 (비즈니스워치 2026.8.1)",
           "https://news.mtn.co.kr/news-detail/2024010205022487860 (MTN 2024.1.2 금감원 약관 개선)",
           "https://kbthink.com/insurance/trend/insurance-after-checkup.html (KB Think 2026.10.29, 보험사명 화면 미표기)",
           "https://korea.legal/wiki/%ec%83%81%eb%b2%95-%ec%a0%9c651%ec%a1%b0/ (상법 제651조)",
           "https://www.kfpa.or.kr/mem/pdf_file/H/151/H151_8.pdf (금감원 분쟁조정사례, 해지 제척기간)",
           "https://www.teamblind.com/kr/post/암보험-고지관련-문의-stzyd4ck (블라인드, 커뮤니티 말투 참고)"]

S = []
# 1 표지 (A1: 사진 전면 + 하단 제목). 이번 주 디자인 실험: 실사 사진 전면에 큰 글자
S.append(cover(layout_for(13),
               "\"두 달 뒤<br>다시 봅시다\"<br><span class=\"y\">알려야 할까?</span>",
               chip="검진 결과지 받은 분",
               photo="photos/documents/pixabay_10045176.jpg", accent="y"))

# 2 사건 타임라인 (움직이는 장)
def _step(i, when, what, col="#7FB2FF", extra=""):
    return f"""<div class="row" id="t{i}" style="gap:22px;opacity:0;{extra}">
    <div style="flex:none;width:26px;display:flex;flex-direction:column;align-items:center"><div style="width:26px;height:26px;border-radius:50%;background:{col};margin-top:8px"></div></div>
    <div><p style="font-size:30px;color:{col};font-weight:800">{when}</p><p style="font-size:33px;color:#fff;font-weight:700;line-height:1.38;margin-top:4px">{what}</p></div></div>"""

S.append(f"""
 <h2>보험금이 거절된<br><span class="y">한 사람의 1년 4개월</span></h2>
 <p class="lead" style="margin-top:12px">금감원 분쟁조정위원회가 올해 7월 결정한 실제 사건이에요.</p>
 <div style="position:relative;margin-top:26px">
  <div style="position:absolute;left:12px;top:20px;bottom:30px;width:2px;background:#3A3A3A"></div>
  <div style="display:flex;flex-direction:column;gap:22px">
   {_step(1, "건강검진", "혈소판이 낮다는 소견. 혈액검사와 골수검사를 받았어요")}
   {_step(2, "2023년 3월", "골수검사 이상 없음. 의사가 <span class='y'>\"두 달 뒤 혈액검사 다시 해 봅시다\"</span>")}
   {_step(3, "2023년 4월", "간편심사보험 가입. 이 말은 알리지 않았어요")}
   {_step(4, "2024년 7월", "골수형성이상증후군 진단. 암 진단비 청구")}
   {_step(5, "보험사 통보", "\"3개월 안에 받은 추가검사 필요 소견을 안 알렸다\"<br>계약 해지, 보험금 거절", "#FF6B6B")}
  </div>
 </div>
 <div class="box" id="tz" style="margin-top:30px;padding:24px 32px;border-color:#FFE45C;opacity:0"><p style="font-size:36px;color:#fff;font-weight:800">2026년 7월 분조위: <span class="y">보험금을 주라</span></p><p style="font-size:31px;color:#C8C8C8;margin-top:8px">그 혈액검사는 추가검사가 아니라 추적관찰이라고 봤어요.</p></div>
 <div class="src">출처: 금융감독원(2026.7.27 보도자료), 뉴시스·헤럴드경제·SBS Biz(2026.7.27)</div>""")

# 3 추가검사 vs 추적관찰
S.append(f"""
 <h2>같은 피검사인데<br><span class="y">이름이 달랐어요</span></h2>
 <table style="margin-top:30px;font-size:30px">
  <thead><tr><th style="width:21%"></th><th>추가검사</th><th class="new">추적관찰</th></tr></thead>
  <tbody>
   <tr><th>뜻</th><td>이상 소견이 나와서 <b style="color:#fff">더 정확히 진단하려고</b> 받는 검사</td><td>치료 없이 상태가 <b style="color:#FFE45C">그대로인지 지켜보는</b> 정기검사</td></tr>
   <tr><th>흔한 말</th><td>"정밀검사 받아 보세요"</td><td>"몇 달 뒤 다시 봅시다"</td></tr>
   <tr><th>청약서</th><td>묻는 항목이면 알려야 해요</td><td>추가검사에 들어가지 않아요</td></tr>
  </tbody>
 </table>
 <p style="font-size:36px;color:#fff;font-weight:800;margin-top:30px">분조위가 본 세 가지</p>
 <div class="rows" style="gap:10px;margin-top:12px">
  <div class="row box" style="padding:16px 26px"><div class="num">1</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">골수검사에서 이상이 없는 상태로, 수치만 보려고 권한 검사</p></div></div>
  <div class="row box" style="padding:16px 26px"><div class="num">2</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">혈소판 감소로 받은 치료나 처방이 없고, 수치도 안정적</p></div></div>
  <div class="row box" style="padding:16px 26px"><div class="num">3</div><div><p style="margin-top:4px;font-size:30px;color:#E0E0E0">일반 혈액검사는 골수검사처럼 원인을 찾는 정밀검사로 보기 어려움</p></div></div>
 </div>
 <div class="src">출처: 금융감독원(2026.7.27), 뉴시스·SBS Biz(2026.7.27), MTN(2024.1.2 금감원 약관 개선). 정기검사·추적관찰 제외 기준은 2024년 1월 약관 개선 때 명확해졌어요.</div>""")

# 4 두 번째 사건: 임상시험 입원
S.append(f"""
 <h2>두 번째 사건,<br><span class="b">임상시험으로 입원</span>한 날</h2>
 <div class="box" style="margin-top:24px;padding:24px 30px">
  <p style="font-size:35px;color:#E0E0E0;line-height:1.6"><b style="color:#fff">2019년 12월, 2021년 4월</b> 신약 임상시험에 참여해 1박 2일씩 두 번 입원<br><b style="color:#fff">2022년 3월</b> 간편심사보험 가입<br><b style="color:#fff">2024년 1~2월</b> 입원해 간병인 일당 청구</p>
 </div>
 <div class="box" style="margin-top:18px;padding:24px 30px;border-color:#FF6B6B"><p style="font-size:34px;color:#E0E0E0;line-height:1.5"><b class="r">보험사</b> "가입 전 3년 안의 질병 입원을 안 알렸다" 해지, 거절</p></div>
 <div class="box" style="margin-top:18px;padding:24px 30px;border-color:#FFE45C">
  <p style="font-size:34px;color:#E0E0E0;line-height:1.5"><b class="y">분조위</b> 질병으로 인한 입원은 <b style="color:#fff">증상 때문에 입원치료나 관리가 필요해서</b> 병원에 머문 경우예요. 이 입원은 아니라고 봤어요.</p>
 </div>
 <div class="rows" style="gap:24px;margin-top:36px">
  <div class="row"><div class="num" style="background:#7FB2FF;width:52px;height:52px;font-size:28px">1</div><p style="font-size:33px;color:#D6D6D6;margin-top:6px">입원기록에 목적이 임상시험, 치료 목적이 아니라는 진단서</p></div>
  <div class="row"><div class="num" style="background:#7FB2FF;width:52px;height:52px;font-size:28px">2</div><p style="font-size:33px;color:#D6D6D6;margin-top:6px">그때 병은 원래 먹던 약으로 통원치료가 가능했던 상태</p></div>
  <div class="row"><div class="num" style="background:#7FB2FF;width:52px;height:52px;font-size:28px">3</div><p style="font-size:33px;color:#D6D6D6;margin-top:6px">참여자 모두 같은 투약·채혈을 받아, 나만의 치료로 보기 어려움</p></div>
 </div>
 <div class="src">출처: 금융감독원(2026.7.27), 뉴시스·헤럴드경제·조세금융신문(2026.7.27), 비즈니스워치(2026.8.1)</div>""")

# 5 질문표 읽는 법 (비노 돋보기)
S.append(f"""
 <h2>청약서 질문은<br><span class="y">기간별로</span> 읽어요</h2>
 {bino('search', 190, 'position:absolute;right:52px;top:140px;transform:rotate(5deg)')}
 <p class="lead" style="margin-top:12px;margin-right:180px">기간마다 묻는 게 달라요. 흔한 틀은 이래요.</p>
 <table style="margin-top:28px;font-size:32px">
  <thead><tr><th style="width:20%"></th><th>일반심사</th><th class="new">간편심사</th></tr></thead>
  <tbody>
   <tr><th>3개월</th><td>진단, 의심 소견, 치료·입원·수술·투약</td><td>입원·수술·<b style="color:#FFE45C">추가검사가 필요하다는 소견</b></td></tr>
   <tr><th>1년</th><td><b style="color:#fff">실제로 받은</b> 추가검사·재검사</td><td>묻지 않는 상품이 많아요</td></tr>
   <tr><th>N년</th><td>상품마다 달라요</td><td>입원·수술<br>(2년·3년 등 상품마다)</td></tr>
   <tr><th>5년</th><td>입원·수술, 7일 이상 치료, 30일 이상 투약 등</td><td>암 등 정해진 큰 병의 진단·입원·수술</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:30px;padding:24px 30px;border-color:#FFE45C"><p style="font-size:31px;color:#E0E0E0;line-height:1.5">검진 결과지를 받았다면 <b style="color:#fff">종합소견의 문장</b>과 질문 문장을 나란히 놓고 보세요. 진단이 없어도 의심 소견을 묻는 칸이 있어요.</p></div>
 <div class="src">출처: 금융감독원(2024.2.27 알릴의무 유의사항), MTN(2024.1.2), 업계 안내 자료(2026). 질문은 보험사·상품마다 달라요.</div>""")

# 6 가입 전 순서
S.append(f"""
 <h2>검진 뒤 가입한다면<br><span class="y">이 순서로</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 26px"><div class="num">1</div><div><h3 style="font-size:36px">결과지 종합소견을 끝까지 읽기</h3><p style="font-size:29px;margin-top:6px">"재검", "추가검사", "추적관찰", "경과 관찰" 같은 말에 표시해 두세요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">2</div><div><h3 style="font-size:36px">의사에게 목적을 묻기</h3><p style="font-size:29px;margin-top:6px">"더 정확히 진단하려는 검사인가요, 상태를 지켜보는 건가요?" 진료기록에 어떻게 적혔는지도요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">3</div><div><h3 style="font-size:36px">질문 문장을 직접 읽고 답하기</h3><p style="font-size:29px;margin-top:6px">설계사에게 말로만 전한 건 알린 것으로 인정되지 않을 수 있어요. 청약서 화면에 적힌 답을 확인하세요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">4</div><div><h3 style="font-size:36px">애매하면 적고 심사받기</h3><p style="font-size:29px;margin-top:6px">결과는 그대로 가입, 특정 부위 보장 제외, 보험료 할증, 거절 중 하나예요.</p></div></div>
  <div class="row box" style="padding:20px 26px"><div class="num">5</div><div><h3 style="font-size:36px">검사 기록과 소견서 보관</h3><p style="font-size:29px;margin-top:6px">나중에 다툼이 생기면 검사 목적을 보여 줄 자료가 돼요.</p></div></div>
 </div>
 <div class="src">출처: 금융감독원(2026.7.27), 비즈니스워치(2026.8.1·2024.2.27), 업계 안내 자료(2026)</div>""")

# 7 해지·거절 통보를 받았다면
S.append(f"""
 <h2>해지 통보를 받았다면<br><span class="r">바로 끝은 아니에요</span></h2>
 <div class="stat" style="margin-top:24px">
  <div class="box"><div class="k">보험사가 안 날부터</div><div class="v y">1개월</div><div class="d">이 안에만 해지할 수 있어요</div></div>
  <div class="box"><div class="k">계약한 날부터</div><div class="v b">3년</div><div class="d">지나면 해지할 수 없어요</div></div>
 </div>
 <div class="qa" style="gap:12px;margin-top:22px">
  <div class="box"><p class="q" style="font-size:30px">보험사가 이미 알았다면?</p><p class="a">계약할 때 보험사가 그 사실을 알았거나 큰 실수로 몰랐다면 해지할 수 없어요(상법 제651조).</p></div>
  <div class="box"><p class="q" style="font-size:30px">알리지 않은 내용과 상관없는 병이라면?</p><p class="a">관련이 없다는 게 증명되면 보험금은 받을 수 있어요. 증명은 가입자 쪽이 해야 해요(상법 제655조).</p></div>
  <div class="box"><p class="q" style="font-size:30px">검사 목적이 쟁점이라면?</p><p class="a">진료기록과 소견서로 목적을 확인하고 금감원 분쟁조정을 신청할 수 있어요. 조정안은 양쪽이 20일 안에 받아들이면 재판상 화해와 같은 효력이 생겨요.</p></div>
 </div>
 <div class="src">출처: 상법 제651조·제655조, 금융감독원 분쟁조정사례, SBS Biz·조세금융신문(2026.7.27). 사건마다 사정이 달라 결과도 달라질 수 있어요.</div>""")

# 8 헷갈리는 질문
S.append(f"""
 <h2>검진 뒤 가장 많이 묻는<br><span class="y">질문 4개</span></h2>
 <div class="qa" style="gap:14px;margin-top:24px">
  <div class="box"><p class="q">혹 크기만 해마다 보는 중이에요</p><p class="a">치료 없이 상태를 지켜보는 정기검사는 추가검사가 아니라는 게 금감원 기준이에요. 다만 질문이 진단이나 의심 소견 자체를 묻는다면 그건 따로 답해야 해요.</p></div>
  <div class="box"><p class="q">간편보험은 질문이 적으니 괜찮죠?</p><p class="a">질문이 적을 뿐, 묻는 항목은 사실대로 답해야 해요. 어기면 해지나 보험금 거절이 생길 수 있어요.</p></div>
  <div class="box"><p class="q">분조위 결정이 나면 바로 받나요?</p><p class="a">신청인과 보험사가 모두 20일 안에 받아들여야 성립해요. 결정만으로 확정되는 건 아니에요.</p></div>
  <div class="box"><p class="q">임상시험 입원은 다 괜찮은가요?</p><p class="a">이번 사건은 치료 목적이 아니라는 진단서와 통원 가능했던 상태가 근거였어요. 사정이 다르면 판단도 달라질 수 있어요.</p></div>
 </div>
 <div class="src">출처: 금융감독원(2026.7.27), MTN(2024.1.2), 아시아경제·조세금융신문(2026.7.27)</div>""")

# 9 마무리 (이번 주 문장 흐름 실험: 표지 질문의 답을 한 문장으로 다시 말하고 끝냄)
S.append(f"""
 <h2 style="margin-top:36px">"두 달 뒤 다시"는<br><span class="y">추적관찰</span>이었어요</h2>
 <p class="lead" style="margin-top:16px">그래서 이 사건은 보험금을 받는 쪽으로 결정됐어요.</p>
 <div class="note" style="margin-top:40px;padding:36px 40px 40px;margin-right:60px">
  <div style="font-size:32px;margin-bottom:10px">검진 뒤 가입 전 체크</div>
  <div class="ck"><span>종합소견 문장 표시하기</span><span>추가검사인지 추적관찰인지</span><span>질문 문장 직접 읽기</span><span>애매하면 적고 심사</span><span>기록·소견서 보관</span></div>
 </div>
 <p style="font-size:32px;margin-top:44px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 질문 항목과 판단은 상품 청약서·약관과 개별 사정에 따라 달라요.</div>""")

SLIDES = S

MOTION = {
    "2": {"dur": 5, "still_t": 4.8, "js": """
window.setT=function(t){
 for(let i=1;i<=5;i++){const s=0.15+(i-1)*0.55, o=c((t-s)/0.4);
  const e=$('#t'+i); e.style.opacity=o; e.style.transform='translateY('+((1-eo(o))*24)+'px)';}
 const z=c((t-3.2)/0.5); $('#tz').style.opacity=z; $('#tz').style.transform='scale('+(0.94+0.06*eb(z))+')';
};"""},
}

CAPTION = """"두 달 뒤 다시 봅시다"
검진 때 이 말 듣고
보험 가입하셨나요?

이 말을 안 알렸다고
암 진단비가 거절된 사건
금감원은 주라고 했어요

이유는 하나
추가검사가 아니라
추적관찰이었거든요

추가검사는 더 정확히
진단하려고 받는 검사
추적관찰은 치료 없이
상태를 지켜보는 검사

검진 결과지 받은 분은
종합소견 문장부터
다시 읽어 보세요

#건강검진 #고지의무
#간편보험 #보험금청구
#보험비밀노트"""
