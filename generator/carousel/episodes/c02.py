# 캐러셀 c02 · 보험사가 먼저 말 안 해주는 것 ① 현장조사 대응법
# 커뮤니티 키워드: 블라인드 보험 채널 "보험 현장조사 궁금합니다"(백지 포괄 동의서·e음 동의 요구), "현장조사 서명", "건강이음 동의"
# 본부장님 현장 경험: 건강e음·국세청·건보공단 요양급여내역은 필수 동의 아님, 녹취·서면·위임장 범위와 기간, 백지 서명 금지, 대면 전 인증번호 요구 주의
# 공식 출처: 건강보험심사평가원 건강e음(내 진료정보 열람, 최대 5년) / 금융위원회 손해사정 관행 개선(소비자 손해사정사 선임권, 2018.12·2019.6) / 금융감독원 1332
import pathlib as _p
from kit import bino
from covers import cover

SERIES = "보험회사 몰래 적어둔 노트"
LABEL = "보험사가 먼저 말 안 해주는 것 ①"
TOPIC = "보험사 현장조사 나왔을 때 동의서·인증번호 대응법"
SOURCES = ["https://www.teamblind.com/kr/post/보험-현장조사-궁금합니다-el6nlaal",
           "https://www.hira.or.kr (건강e음 내 진료정보 열람)",
           "https://www.fsc.go.kr/po010104/73753 (손해사정 관행 개선 후속조치)"]

_CAP = (_p.Path(__file__).resolve().parents[3] / "photos/capture/blind_fieldcheck.png").as_uri()

S = []
# 1 표지 (B1: 제목 위 + 비노 가운데)
S.append(cover("B1", "현장조사 나와서<br><span class=\"r\">인증번호 불러달래요?</span>",
               chip="보험금 청구한 가족 있다면 필독", pose="stop", accent="y"))

# 2 실제 사연
S.append(f"""
 <h2>블라인드에 올라온<br><span class="y">실제 질문</span>이에요</h2>
 <div style="margin-top:30px;background:#fff;border-radius:24px;padding:18px;box-shadow:0 18px 40px rgba(0,0,0,.6);transform:rotate(-1deg)">
  <img src="{_CAP}" style="width:100%;height:auto;display:block;border-radius:12px">
 </div>
 <div class="note" style="margin-top:44px;font-size:36px;align-self:flex-end;transform:rotate(2deg)">"다른 사람도 다 한대요"<br>이 말에 그냥 서명하는 분 많아요</div>
 <div class="src">출처: 블라인드 보험 채널 (작성자 정보 가림)</div>""")

# 3 왜 나오나
S.append(f"""
 <h2>현장조사,<br>왜 <span class="r">나오는</span> 걸까요?</h2>
 <p class="lead">보험사가 "가입 전 병력을 숨겼는지"<br>확인하려는 경우가 대부분이에요.</p>
 <div class="rows">
  <div class="row box"><div class="num">1</div><div><h3>가입하고 얼마 안 돼서 큰 청구</h3><p>특히 가입 후 2년 안에 암·뇌·심장 같은 진단금을 청구하면 조사가 나오는 경우가 많아요.</p></div></div>
  <div class="row box"><div class="num">2</div><div><h3>입원이 길거나 금액이 클 때</h3><p>청구 금액이 크면 서류만으로 끝내지 않고 사람이 직접 확인해요.</p></div></div>
  <div class="row box"><div class="num">3</div><div><h3>예전 병원 기록이 궁금할 때</h3><p>가입할 때 알린 내용과 실제 진료 기록이 맞는지 보려는 거예요.</p></div></div>
 </div>
 <div class="box" style="margin-top:22px;border-color:#FFE45C"><p style="font-size:31px;color:#E0E0E0">조사를 <b class="r">전부 거부</b>하면 보험금이 늦어지거나 거절될 수 있어요. 정답은 <b class="y">골라서 동의</b>하는 거예요.</p></div>
 <div class="src">보험사·상품에 따라 조사 기준은 다를 수 있어요.</div>""")

# 4 필수 vs 필수 아님
S.append(f"""
 <h2>다 서명해야 할까요?<br><span class="y">아니에요</span></h2>
 <table>
  <thead><tr><th style="width:50%">보통 필요한 것</th><th class="new">꼭 해야 하는 건 아닌 것</th></tr></thead>
  <tbody>
   <tr><td>보험금 청구에 필요한<br>개인정보 동의</td><td><b>건강e음</b> 인증<br>(심평원 앱)</td></tr>
   <tr><td>이번 청구와 관련된<br>병원 서류</td><td><b>국세청</b> 기록 조회 동의</td></tr>
   <tr><td>범위·기간이 적힌<br>병원 위임장</td><td>건보공단<br><b>요양급여내역서</b></td></tr>
   <tr><td></td><td>병원·기간이 빈<br><b>백지 포괄 위임장</b></td></tr>
  </tbody>
 </table>
 <div class="box" style="margin-top:22px;padding:24px 30px"><p style="font-size:29px;color:#E0E0E0;line-height:1.45"><b class="y">건강e음</b>은 본인 인증 한 번이면 최근 5년 진료 내역이 한 번에 보이는 앱이에요. 숨길 게 없다면 동의해도 되지만, 이번 병과 상관없는 기록까지 다 보이니 <b>불필요한 논쟁</b>이 생길 수 있어요.</p></div>
 <div class="src">건강e음: 건강보험심사평가원 '내 진료정보 열람' (최대 5년)</div>""")

# 5 인증번호 경고 (움직이는 장)
S.append(f"""
 <h2 style="margin-top:40px">이 말 들으면<br><span class="r">일단 멈추세요</span></h2>
 <div id="warn" class="box" style="margin-top:40px;border:4px solid #FF6B6B;padding:40px 40px;background:#1E1414">
  <p style="font-size:30px;color:#FF9C9C;font-weight:700">조사원 (만나기도 전에 전화로)</p>
  <p style="font-size:50px;color:#fff;font-weight:900;line-height:1.3;margin-top:14px">"문자로 간 인증번호<br>좀 불러주세요"</p>
 </div>
 <div class="rows" style="margin-top:30px;gap:16px">
  <div class="row box" id="r1" style="padding:22px 28px"><div class="num" style="background:#FF6B6B">!</div><div><h3>인증번호 = 내 기록 열쇠</h3><p>불러주는 순간 내 진료 기록 조회를 허락한 것과 같아요.</p></div></div>
  <div class="row box" id="r2" style="padding:22px 28px"><div class="num">✓</div><div><h3>인증번호는 아무에게도 X</h3><p>필요하면 만나서, 무엇을 보는지 서면으로 확인한 뒤 결정하세요.</p></div></div>
 </div>
 <div class="note" style="margin-top:36px;font-size:36px;align-self:flex-start">부모님·가족한테 꼭 공유해 주세요</div>""")

# 6 대응 4원칙
S.append(f"""
 <h2>현장조사 대응<br><span class="y">4가지 원칙</span></h2>
 <div class="rows">
  <div class="row box"><div class="num">1</div><div><h3>대화는 녹음해 두세요</h3><p>무엇을 요구했고 뭐라고 설명했는지 남겨 두면 나중에 다툼이 생겨도 근거가 돼요.</p></div></div>
  <div class="row box"><div class="num">2</div><div><h3>요구 사항은 서면으로</h3><p>"이 서류가 꼭 필요하다"는 말은 문자·공문으로 받아 두세요. 말로만 듣고 서명하지 마세요.</p></div></div>
  <div class="row box"><div class="num">3</div><div><h3>위임장엔 범위와 기간</h3><p>어느 병원에서, 어떤 서류를, 언제부터 언제까지 발급받는지 직접 적어 넣으세요.</p></div></div>
  <div class="row box"><div class="num">4</div><div><h3>빈칸에 서명만은 절대 X</h3><p>서명한 서류는 사진을 찍거나 사본을 받아 두세요.</p></div></div>
 </div>""")

# 7 위임장 예시 + 백지 사례
S.append(f"""
 <h2>병원 위임장,<br><span class="y">이렇게 채우세요</span></h2>
 <div class="note" style="margin-top:34px;padding:34px 40px 38px;font-size:34px;transform:rotate(-1.5deg)">
  <div style="font-size:30px;margin-bottom:14px">위임장 예시</div>
  <div class="ck" style="font-size:48px;gap:10px">
   <div>발급 병원: ○○내과 한 곳만</div>
   <div>서류: 진단서·진료기록 사본</div>
   <div>기간: 2024년 1월 ~ 2026년 8월</div>
   <div>용도: 이번 보험금 청구 심사</div>
  </div>
 </div>
 <div class="box" style="margin-top:40px;border-color:#FF6B6B"><p style="font-size:31px;color:#E0E0E0;line-height:1.45"><b class="r">백지 위임장에 서명만 하면?</b><br>그 한 장으로 동의하지 않은 다른 병원까지 찾아가 서류를 떼는 사례가 실제로 많아요. 빈칸이 있으면 직접 채우거나 줄을 그어 두세요.</p></div>""")

# 8 동의하기 싫을 때 말하는 법 + Q&A
S.append(f"""
 <h2>동의하기 싫을 땐<br><span class="b">이렇게 말하세요</span></h2>
 <div class="rows" style="gap:14px;margin-top:26px">
  <div class="row box" style="padding:22px 28px"><div class="num">1</div><div><h3>"이 동의가 필수인가요?"</h3><p>필수라고 하면 그 근거를 서면으로 달라고 하고, 어떤 서류인지 다시 물어보세요.</p></div></div>
  <div class="row box" style="padding:22px 28px"><div class="num">2</div><div><h3>"병원 위임장으로 해 주세요"</h3><p>"개인정보가 민감해서요"라고 요청하면 위임장 방식으로 진행해야 해요.</p></div></div>
 </div>
 <div class="qa" style="margin-top:22px">
  <div class="box"><div class="q">조사 결과가 억울하면요?</div><div class="a">손해사정사를 내가 직접 선임해 달라고 요청할 수 있어요. 금감원 1332 분쟁조정도 무료예요.</div></div>
  <div class="box"><div class="q">조사가 길어져 돈이 급하면요?</div><div class="a">보험사에 가지급보험금(일부 먼저 받기)을 청구할 수 있는지 물어보세요.</div></div>
 </div>
 <div class="src">손해사정사 선임권: 금융위원회 손해사정 관행 개선 (2018·2019)<br>세부 절차는 보험사·상품마다 달라요.</div>""")

# 9 마무리
S.append(f"""
 <h2 style="margin-top:44px">이 노트,<br><span class="y">가족 단톡방에 보내 주세요</span></h2>
 <div style="display:flex;gap:28px;align-items:flex-end;margin-top:40px">
  <div class="note" style="flex:1;padding:36px 40px 40px">
   <div style="font-size:32px;margin-bottom:10px">현장조사 체크</div>
   <div class="ck"><span>인증번호 안 불러주기</span><span>녹음 · 서면으로 받기</span><span>위임장 범위 · 기간</span><span>백지 서명 X</span></div>
  </div>
  {bino('point', 300)}
 </div>
 <div class="box" style="margin-top:40px"><p style="font-size:34px;color:#fff;font-weight:700">조사원 전화는 갑자기 와요.</p><p style="font-size:30px;margin-top:10px">부모님이 보험금 청구할 일이 생기기 전에 미리 알려 드리세요.</p></div>
 <p style="font-size:32px;margin-top:34px;color:#BDBDBD">주제별 보험 노트 더 보기<br><b class="y" style="font-size:42px;font-weight:900">insusecretnote.com</b></p>
 <div class="src">일반 정보이며, 개별 사안은 약관과 보험사 안내를 확인하세요.</div>""")

SLIDES = S

MOTION = {
    "5": {"dur": 4, "still_t": 3.5, "js": """
window.setT=function(t){
 const p=0.5+0.5*Math.sin(t*2*Math.PI/1.2);
 $('#warn').style.boxShadow='0 0 '+(10+40*p)+'px rgba(255,107,107,'+(0.25+0.45*p)+')';
 const f1=eo(c((t-0.4)/0.5)), f2=eo(c((t-0.9)/0.5));
 $('#r1').style.opacity=f1; $('#r1').style.transform='translateY('+((1-f1)*30)+'px)';
 $('#r2').style.opacity=f2; $('#r2').style.transform='translateY('+((1-f2)*30)+'px)';
};"""},
}

CAPTION = """현장조사 나온 조사원이
"인증번호 불러주세요"
이러면 일단 멈추세요

보험금 청구했더니
조사원이 와서
동의서를 잔뜩 내밀었다는
사연, 정말 많아요

👉 건강e음·국세청 기록
요양급여내역서는
꼭 해야 하는 동의가 아니에요
👉 대화는 녹음, 요구는 서면
👉 위임장엔 병원·서류·기간
👉 빈칸에 서명만은 절대 X

⚠️ 백지 위임장 한 장으로
동의 안 한 병원 서류까지
떼 가는 경우도 있어요

부모님이 보험금 청구할 일
생기기 전에
가족 단톡방에 공유해 주세요

다음 노트 ②
의료자문 동의서, 서명 전에
팔로우하고 받아 보세요

#현장조사 #보험금청구 #손해사정 #부모님보험 #보험비밀노트"""
