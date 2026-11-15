# 캐러셀 c07 · 해지·갈아타기 전에 ② "더 좋은 걸로 갈아타세요" 이 말 들었다면
# 커뮤니티 키워드: "설계사가 보험 갈아타래요", "기존 보험 해지하고 새로 들라는데", "더 좋은 걸로 갈아타세요" (보험 카페·지식iN형 질문 반복, 2026.11 조사)
#   + 2026.5 금감원 부당승환 소비자경보 이후 "갈아타기 권유" 글 증가, 2026.9 설계사 수 역대 최대 보도. c06 에서 다음 편으로 예고한 주제
# 공식·교차 출처:
#  - 2026년 1분기 부당승환 민원 211건, 직전 분기 137건 대비 54% 증가, 소비자경보 '주의': 금융감독원 2026.5 (KDI 경제정보센터 수록) / 경향신문 2026.5.12 / 디지털데일리 2026.5.13 / 경북매일 2026.5.12
#  - 피해 유형(해약환급금 손실, 부담보·가입 거절, 면책기간 재적용, 보험료 상승), 사례(종신보험 납입 2700만 원 → 환급 2200만 원): 경향신문 2026.5.12 / 경북매일 2026.5.12 / 디지털데일리 2026.5.13
#  - 암보험 등 면책기간 90일: SBS Biz 2024.6.24(금감원 안내) / 경북매일 2026.5.12
#  - 보장이 부족하면 해지 대신 특약 추가·단독형 가입 검토, 무조건 해지 권유는 의심: 금감원(경향신문·디지털데일리·경북매일 2026.5)
#  - 보험업법 제97조 제1항 제5호·제3항(1개월·6개월 기준, 자필서명 예외)·제4항(소멸 후 6개월 안 부활 청구·새 계약 취소)·제5항(특별한 사유 없으면 부활 승낙): 보험업법 원문(korea.legal) / SBS Biz 2024.6.24 / 경향신문 2026.5.12
#  - 승환계약률 비교공시 추진(보험사·채널·상품별, 협회 홈페이지 반기 공시): 금융감독원 2026.5 / SBS Biz 2026.4.28 / 이투데이 2026.8.27 / 헤럴드경제 2026.9.23
from kit import bino
from covers import cover, layout_for

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "해지·갈아타기 전에 ②"
TOPIC = "보험 갈아타기 권유 받았을 때 확인할 것·6개월 안 되돌리기"
SOURCES = ["https://eiec.kdi.re.kr/policy/materialView.do?num=280891 (금융감독원 부당승환 소비자경보 2026.5)",
           "https://www.khan.co.kr/article/202605121200011 (경향신문 2026.5.12, 민원 211건·사례·6개월 부활)",
           "https://www.ddaily.co.kr/page/view/2026051310115190638 (디지털데일리 2026.5.13, 137건→211건)",
           "https://kbmaeil.com/article/20260512500772 (경북매일 2026.5.12, 피해 유형·유의사항)",
           "https://korea.legal/wiki/보험업법-제97조/ (보험업법 제97조 원문)",
           "https://biz.sbs.co.kr/amp/article/20000177808 (SBS Biz 2024.6.24, 6개월 내 부활·취소, 면책 90일)",
           "https://biz.sbs.co.kr/amp/article/20000307157 (SBS Biz 2026.4.28, 승환계약률 공시)",
           "https://www.etoday.co.kr/news/view/2617527 (이투데이 2026.8.27, 비교공시 추진)",
           "https://biz.heraldcorp.com/article/10883528 (헤럴드경제 2026.9.23, 설계사 수·비교공시)"]

S = []
# 1 표지 (A2: 사진 위 + 제목 아래, 질문형)
S.append(cover(layout_for(7), "이 말 듣고 바로<br><span class=\"y\">해지</span>해도 될까요?",
               chip="“더 좋은 걸로 갈아타세요”",
               sub="갈아타기 민원, 한 분기 만에 54% 늘었어요",
               photo="photos/documents/pixabay_962354.jpg"))

# 2 왜 손해인가
S.append(f"""
 <h2>갈아타면 생길 수 있는<br><span class="r">손해 4가지</span></h2>
 <div class="rows" style="gap:12px;margin-top:22px">
  <div class="row box" style="padding:16px 26px"><div class="num">1</div><div><h3>낸 돈보다 적게 돌려받아요</h3><p>중간에 해지하면 해약환급금이 낸 보험료보다 적은 경우가 많아요.</p></div></div>
  <div class="row box" style="padding:16px 26px"><div class="num">2</div><div><h3>보장 빈틈이 생겨요</h3><p>암보험 등은 면책기간(보통 90일)이 새로 시작돼요. 그사이 진단받으면 못 받을 수 있어요.</p></div></div>
  <div class="row box" style="padding:16px 26px"><div class="num">3</div><div><h3>보장이 빠질 수 있어요</h3><p>그사이 생긴 병원·약 기록 때문에 일부 보장을 빼거나(부담보) 가입을 거절할 수 있어요.</p></div></div>
  <div class="row box" style="padding:16px 26px"><div class="num">4</div><div><h3>보험료가 올라요</h3><p>나이가 들어 새로 가입하면 비슷한 보장이라도 보험료가 오를 수 있어요.</p></div></div>
 </div>
 <div class="box" style="margin-top:16px;padding:18px 28px;border-color:#FF6B6B">
  <p style="font-size:27px;color:#9E9E9E;font-weight:700">금감원이 소개한 사례</p>
  <p style="font-size:29px;color:#E0E0E0;line-height:1.42;margin-top:4px">10년 넘게 낸 종신보험 <b style="color:#fff">2700만 원</b>, 해지하고 돌려받은 돈 <b class="r">2200만 원</b>. 사망보험금은 갈아탄 뒤에도 그대로였어요.</p>
 </div>
 <div class="src">출처: 금융감독원 소비자경보(2026.5), 경향신문·경북매일(2026.5.12)·SBS Biz(2024.6) 보도</div>""")

# 3 숫자 (움직이는 장)
S.append(f"""
 <h2>요즘 이 권유가<br><span class="y">유난히 많아요</span></h2>
 <p class="lead" style="margin-top:12px">부당한 갈아타기 관련 민원 (금융감독원 집계)</p>
 <div class="stat" style="margin-top:22px">
  <div class="box"><div class="k">2025년 4분기</div><div class="v" id="v1" style="color:#BDBDBD">137</div><div class="d">건</div></div>
  <div class="box" style="border-color:#FF6B6B"><div class="k">2026년 1분기</div><div class="v r" id="v2">211</div><div class="d">건</div></div>
 </div>
 <div style="display:flex;justify-content:center;margin-top:22px"><span class="chip" id="up" style="background:#FF6B6B;font-size:34px">한 분기 만에 54% 증가</span></div>
 <div class="box" style="margin-top:20px;padding:20px 30px">
  <p style="font-size:28px;color:#9E9E9E;font-weight:700">금감원이 본 이유</p>
  <p style="font-size:30px;color:#E0E0E0;line-height:1.5;margin-top:8px">일부 판매 조직이 설계사 영입 경쟁을 벌이면서, 옮겨 간 설계사가 실적을 채우려고 <b class="y">기존 고객에게 해지 후 새 가입</b>을 권하는 사례가 늘었대요.</p>
 </div>
 <div class="box" style="margin-top:18px;padding:20px 30px;border-color:#FFE45C">
  <p style="font-size:28px;color:#9E9E9E;font-weight:700">이런 말을 들으면 한 번 더 확인</p>
  <p style="font-size:31px;color:#fff;font-weight:700;line-height:1.55;margin-top:8px">"옛날 보험은 보장이 약해요"<br>"지금 안 바꾸면 손해예요"<br>"보험료 더 싸게 맞춰 드릴게요"</p>
 </div>
 <p style="font-size:27px;color:#BDBDBD;margin-top:16px;line-height:1.4">금감원은 소비자경보 '주의'를 내고 승환계약률 공시를 추진 중이에요.</p>
 <div class="src">출처: 금융감독원(2026.5), 디지털데일리·경향신문(2026.5)·이투데이(2026.8) 보도</div>""")

# 4 비교표
S.append(f"""
 <div style="display:flex;justify-content:space-between;align-items:flex-end">
  <h2>사인 전에<br><span class="y">나란히 놓고 비교</span></h2>
  {bino('search', 190, 'margin-bottom:-6px')}
 </div>
 <p class="lead" style="margin-top:14px">기존 보험과 새 보험, <b>같은 줄끼리</b> 적어 달라고 하세요.</p>
 <table style="font-size:30px;line-height:1.4;margin-top:20px">
  <thead><tr><th style="width:27%;font-size:29px">항목</th><th class="new" style="font-size:29px">이걸 확인해요</th></tr></thead>
  <tbody>
   <tr><th style="color:#fff;font-size:30px;padding:27px 14px">보험료</th><td>매달 얼마, 몇 년 내는지. 갱신형이면 오를 수 있는지</td></tr>
   <tr><th style="color:#fff;font-size:30px;padding:27px 14px">보장 내용</th><td>빠지는 보장은 없는지, 금액이 줄지는 않는지</td></tr>
   <tr><th style="color:#fff;font-size:30px;padding:27px 14px">보장 기간</th><td>몇 살까지 보장되는지</td></tr>
   <tr><th style="color:#fff;font-size:30px;padding:27px 14px">면책·감액</th><td>새 보험에서 못 받거나 덜 받는 기간</td></tr>
   <tr><th style="color:#fff;font-size:30px;padding:27px 14px">해약환급금</th><td>지금 해지하면 받는 돈과 낸 돈의 차이</td></tr>
   <tr><th style="color:#fff;font-size:30px;padding:27px 14px">가입 조건</th><td>내 병력 때문에 빠지는 보장(부담보)은 없는지</td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:28px;padding:24px 30px;border-color:#FFE45C"><p style="font-size:31px;color:#E0E0E0;line-height:1.45">이 비교를 적은 종이가 <b class="y">비교안내 확인서</b>예요. 안 주면 먼저 달라고 하세요.</p></div>
 <div class="src">출처: 금융감독원 소비자경보(2026.5), 경북매일(2026.5.12) 보도. 상품마다 항목이 다를 수 있어요.</div>""")

# 5 법에서는 이렇게 봐요
S.append(f"""
 <h2>법은 이런 갈아타기를<br><span class="r">부당하다고 봐요</span></h2>
 <p class="lead" style="margin-top:16px">보험업법 제97조는 기존 계약을 부당하게 없애고 새 계약을 들게 하는 것을 <b>금지</b>해요.</p>
 <div class="rows" style="gap:14px;margin-top:22px">
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#FF6B6B">1</div><div><h3>1개월 안에 해지 + 새 가입</h3><p>새 계약 전후 1개월 안에 기존 계약이 없어졌다면 부당한 갈아타기로 봐요. 손해를 볼 수 있다는 걸 본인이 자필로 확인한 경우는 예외예요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num" style="background:#FF6B6B">2</div><div><h3>6개월 안인데 비교 안내가 없었다면</h3><p>새 계약 전후 6개월 안에 기존 계약이 없어졌는데, 보험료·기간·보장 같은 중요한 내용을 비교해 알려 주지 않았다면 역시 부당하다고 봐요.</p></div></div>
 </div>
 <div style="position:relative;flex:none;height:150px;margin-top:26px">
  <div style="position:absolute;left:0;right:0;top:40px;height:44px;border-radius:12px;background:rgba(255,228,92,.18);border:2px solid #FFE45C"></div>
  <div style="position:absolute;left:30%;right:30%;top:40px;height:44px;border-radius:12px;background:rgba(255,107,107,.55)"></div>
  <div style="position:absolute;left:50%;top:22px;width:4px;height:80px;margin-left:-2px;background:#fff"></div>
  <p style="position:absolute;left:0;right:0;top:0;text-align:center;font-size:24px;color:#fff;font-weight:700">새 계약일</p>
  <p style="position:absolute;left:30%;right:30%;top:100px;text-align:center;font-size:25px;color:#FF6B6B;font-weight:800">앞뒤 1개월</p>
  <p style="position:absolute;left:0;top:100px;font-size:25px;color:#FFE45C;font-weight:800">6개월 전</p>
  <p style="position:absolute;right:0;top:100px;font-size:25px;color:#FFE45C;font-weight:800">6개월 후</p>
 </div>
 <div class="box" style="margin-top:14px;padding:22px 30px;border-color:#FFE45C"><p style="font-size:30px;color:#E0E0E0;line-height:1.45">그래서 <b class="y">자필 서명 한 줄</b>이 중요해요.<br>무슨 내용인지 읽고 나서 쓰세요. 비교해 보고 원해서 바꾸는 건 괜찮아요.</p></div>
 <div class="src">출처: 보험업법 제97조 제1항 제5호·제3항, SBS Biz(2024.6) 보도</div>""")

# 6 지금 할 순서
S.append(f"""
 <h2>갈아타라는 말 들으면<br><span class="y">이 순서대로</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:20px 28px"><div class="num">1</div><div><h3>해지 신청부터 하지 않기</h3><p>해지는 되돌리기 어려워요. 결정은 비교가 끝난 뒤에 해요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">2</div><div><h3>비교안내 확인서 받기</h3><p>기존 보험과 새 보험의 보험료·보장·기간·면책을 나란히 받아요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">3</div><div><h3>부족한 것만 채우는 방법 묻기</h3><p>기존 보험에 특약을 더하거나, 모자란 보장만 따로 드는 게 나을 수 있어요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">4</div><div><h3>새 보험 승인 확인 후 정리</h3><p>심사 결과와 빠지는 보장, 면책기간을 확인한 뒤에 기존 보험을 정리해요.</p></div></div>
  <div class="row box" style="padding:20px 28px"><div class="num">5</div><div><h3>설명 자료와 문자 남기기</h3><p>나중에 문제가 생기면 이게 근거가 돼요.</p></div></div>
 </div>
 <div class="src">출처: 금융감독원 소비자경보(2026.5), 경향신문·경북매일(2026.5.12) 보도</div>""")

# 7 Q&A
S.append(f"""
 <h2>헷갈리는 질문<br><span class="b">모아 봤어요</span></h2>
 <div class="qa" style="margin-top:22px;gap:12px">
  <div class="box"><div class="q">기존 보험이 너무 오래돼서 부족해요</div><div class="a">해지 대신 특약을 더하거나 부족한 보장만 단독으로 드는 방법을 금감원도 먼저 권해요.</div></div>
  <div class="box"><div class="q">자필 서명을 이미 했어요</div><div class="a">1개월 기준의 예외가 될 수 있어요. 그래도 비교 안내를 제대로 받았는지는 따로 따져 볼 수 있으니 자료를 모아 두세요.</div></div>
  <div class="box"><div class="q">다른 회사 보험으로 옮겨도 해당되나요?</div><div class="a">회사가 같든 다르든, 기존 계약을 없애고 새로 들게 한 경우를 따져요. 청구는 새 보험을 권한 설계사가 속한 보험사에 해요.</div></div>
  <div class="box"><div class="q">보험사가 조치를 안 해 줘요</div><div class="a">금융감독원에 민원을 넣을 수 있어요. 받은 설명 자료와 문자, 계약 날짜를 함께 내요.</div></div>
 </div>
 <div class="src">출처: 금융감독원(2026.5), 보험업법 제97조, 경향신문(2026.5.12) 보도</div>""")

# 8 보너스: 6개월 안이면 되돌리기 + 다음 편
S.append(f"""
 <h2>이미 갈아탔다면?<br><span class="y">6개월 안엔 되돌릴 수 있어요</span></h2>
 <p class="lead">부당하게 갈아탄 거라면 <b>법으로 정한 권리</b>가 있어요.</p>
 <div class="box" style="margin-top:22px;padding:24px 30px">
  <div class="rows" style="gap:16px;margin-top:0">
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">1</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">기존 보험이 없어진 날부터 <b class="y">6개월 안</b>에 청구해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">2</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0"><b class="y">기존 보험은 부활</b>, <b class="y">새 보험은 취소</b>를 요구할 수 있어요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">3</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">새 보험을 권한 설계사가 속한 보험사에 청구해요.</p></div></div>
   <div class="row"><div class="num" style="width:52px;height:52px;font-size:28px">4</div><div><p style="margin-top:4px;font-size:29px;color:#E0E0E0">보험사는 특별한 사유가 없으면 부활을 받아 줘야 해요.</p></div></div>
  </div>
 </div>
 <p style="font-size:27px;color:#BDBDBD;margin-top:16px;line-height:1.45">6개월이 지나면 이 방법은 쓰기 어려워요. 날짜부터 확인하세요.</p>
 <div class="note" style="margin-top:26px;font-size:34px;transform:rotate(-1.5deg)">다음 노트<br>가입하고 후회될 때, 돌려받는 기한</div>
 <div class="src" style="padding-bottom:96px;margin-top:14px">출처: 보험업법 제97조 제4·5항, 경향신문(2026.5.12)·SBS Biz(2024.6.24) 보도</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">갈아타기 권유 받은 가족에게<br><span class="y">먼저 보내 주세요</span></h2>
 <div class="note" style="margin-top:44px;padding:36px 40px 40px">
  <div style="font-size:32px;margin-bottom:10px">갈아타기 전 체크</div>
  <div class="ck"><span>해지 신청은 맨 마지막에</span><span>비교안내 확인서 받기</span><span>면책기간·빠지는 보장 확인</span><span>특약 추가로 될지 묻기</span><span>6개월 안이면 부활 청구 가능</span></div>
 </div>
 <div class="box" style="margin-top:44px"><p style="font-size:34px;color:#fff;font-weight:700">"좋은 걸로 바꿔 드릴게요"</p><p style="font-size:30px;margin-top:10px">좋은지 아닌지는 종이 한 장에 나란히 적어 보면 보여요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 실제 조건은 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "3": {"dur": 4, "still_t": 3.6, "js": """
window.setT=function(t){
 const p=eo(c((t-0.3)/1.4));
 $('#v1').textContent=Math.round(137*c(t/0.6));
 $('#v2').textContent=Math.round(137+(211-137)*p);
 const u=eb(c((t-1.8)/0.5));
 $('#up').style.opacity=c((t-1.8)/0.3); $('#up').style.transform='scale('+(0.6+0.4*u)+')';
 const q=0.5+0.5*Math.sin(t*2*Math.PI/1.4), on=c((t-2.2)/0.4);
 $('#v2').parentElement.style.boxShadow='0 0 '+(on*(8+28*q))+'px rgba(255,107,107,'+(on*(0.2+0.4*q))+')';
};"""},
}

CAPTION = """"더 좋은 걸로 갈아타세요"
이 말 듣고 바로 해지하면
손해 볼 수 있어요

갈아타기 민원이
한 분기 만에 54% 늘었어요

👉 해지 신청은 맨 마지막에
👉 비교안내 확인서 먼저 받기
👉 면책기간·빠지는 보장 확인
👉 부족하면 특약 추가부터
👉 6개월 안이면 되돌릴 수 있어요

자필 서명 한 줄도
읽고 나서 쓰세요

갈아타기 권유 받은 가족에게
공유해 주세요

다음 노트
가입하고 후회될 때, 돌려받는 기한

#보험갈아타기 #부당승환 #보험해지
#비교안내확인서 #보험비밀노트"""
