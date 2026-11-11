# 보험비밀노트 숏폼 자동 운영 플레이북

예약 작업(새 작업 공간)이 매번 이 문서를 처음부터 읽고 그대로 따른다. 본부장님(전성재)은 개발 초보이고, 결과물과 알림은 텔레그램(@Jerryblogbot)으로만 받는다.

계정 구분·브랜드 규칙·캐러셀 규칙·광고 현황은 `generator/INSTAGRAM.md` 에 모아 두었다. 이 문서보다 먼저 읽는다.

## 0. 작업 공간 준비 (모든 예약 작업 공통)
1. 저장소 `seongjerry/insu-photobank` 가 `/home/claude/insu-photobank` 에 없으면 add_repo(owner=seongjerry, repo=insu-photobank, access=push) 후 안내대로 clone. 있으면 `git pull`.
2. 영상 제작이 필요한 작업만: 비공개 폰트 저장소도 받는다. add_repo(owner=seongjerry, repo=insu-assets, access=read) 후 안내대로 `/home/claude/insu-assets` 에 clone. 그다음 `bash generator/kit/setup.sh` (작업 폴더 /home/claude/build). insu-assets 의 파일은 절대 이 공개 저장소에 복사·커밋하지 않는다.
3. 커밋은 `git -c user.name=Claude -c user.email=noreply@anthropic.com commit` 으로, 메시지 끝에 시스템이 안내한 Co-Authored-By 줄을 붙인다.
4. GitHub API는 `gh api` REST만 사용 (GraphQL 불가). 워크플로 실행: `gh api -X POST repos/seongjerry/insu-photobank/actions/workflows/<파일>/dispatches -f ref=main [-f 'inputs[x]=y']`.
5. 공개 저장소다. 개인정보·비밀값을 파일이나 로그에 남기지 않는다.

## 1. 운영 규칙
- **업로드:** 매일 2개, 13:00 / 18:00 (KST). 인스타 릴스 + 유튜브 쇼츠 동시.
- **흐름:** 오전 주제 제안(텔레그램) → 12:00 전 승인 → 제작 → 예약 게시. 12:00까지 답이 없으면 그날은 쉬고 텔레그램으로 알린다.
- **주제 5갈래 (하루 2개는 서로 다른 갈래, 한 주에 고르게):**
  1. 소비자가 궁금해할 보험정보 (청구·가입·해지·갱신)
  2. 보험비밀노트에서만 볼 수 있는 정보 ("보험회사 몰래 적어둔 노트 #N" 시리즈, 다크노트 우선)
  3. 속 시원한 팩폭 ("이건 좋다 / 이건 별로다"를 분명하게. 단 특정 보험사·상품명 비방 금지, 구조와 행동을 비판)
  4. 저장·공유용 체크리스트 (부모님께 공유, 병원 갈 때 꺼내보기)
  5. 설계사가 알아둬야 할 꿀팁 (설계사 대상, 리크루팅 관심층 유입)
- **주제 리서치:** 매번 WebSearch로 블로그·카페·지식iN·커뮤니티(맘카페, 보배드림, 더쿠, 네이트판, 블라인드, 클리앙, 뽐뿌 등)에서 지금 사람들이 많이 묻는 보험 키워드를 먼저 잡고(사람이 가장 많이 몰리는 곳), 최근 유튜브 쇼츠·인스타 릴스에서 조회수 높았던 보험 주제도 함께 본다. 그대로 베끼지 말고 각색하며, 사람들이 쓰는 말투를 훅에 살린다. 자세한 방법은 `generator/carousel/RESEARCH.md` 4장. 숫자·제도는 공식 출처(금감원·금융위·보험협회·법령) 또는 언론 2곳 이상으로 확인. 출처는 plan 파일에 남긴다.
- **중복 금지:** `generator/shorts/experiments.csv` 의 지난 주제와 겹치지 않게.
- **포맷 로테이션 (같은 포맷은 연속 최대 3개):** note_light(흰 노트), note_dark(다크노트), kakao(카톡 대화), lock(잠금화면 알림). experiments.csv 최근 3개가 모두 같은 포맷이면 다음은 반드시 다른 포맷.
- **목소리 섞기 (남성만 연속 3개 이상 금지, 여성 비율 약 40%):**
  - 남: `ko-KR-InJoonNeural` rate +15% (주력), `ko-KR-HyunsuMultilingualNeural` rate +8%
  - 여: `ko-KR-SunHiNeural` rate +10%, `de-DE-SeraphinaMultilingualNeural` rate +8% pitch +25Hz
  - 숫자는 대본에서 한글로 풀어 쓴다 ("일만 원", "이백팔십칠만 원"). "만 원대"는 "일만 원대"로.
- **편집:** 공백 제거 빠른 편집(`generator/kit/fast_build.py`), 30~50초, 배경음악 기본 bgm_04_upbeat_pluck(-34 LUFS), 카톡/잠금화면은 bgm_03_warm_piano 가능.
- **화면 규칙:** 1080x1920, 내용은 세로 중앙(장면 top 85px 이동이 템플릿에 반영됨), 자막은 1600px 위에서 끝, 오른쪽 아이콘 자리 비우기. 흰 노트는 검정 자막·박스 없음, 다크노트는 흰 자막. 상단 브랜드줄·작은 안내문구·심의필 넣지 않음.
- **폰트 (2026-11-09 본부장님 지정):** 템플릿이 `fonts/fonts.css` 를 불러온다.
  - 제목·큰 숫자·자막: **Paperlogy(페이퍼로지)** 800~900, 자막 700. Pretendard보다 글자가 넓으니 제목 글자 크기를 기존보다 약 8% 작게 잡고, 미리보기에서 줄넘김으로 아래 요소와 겹치지 않는지 꼭 확인한다.
  - 카톡형 말풍선 본문은 실제 앱처럼 Pretendard 유지, 카드 제목·자막만 Paperlogy.
  - 잠금화면형 카드 라벨·감성 문구: **오이냉체(Cucumber)** (`class="hand"` 또는 `.big .lb`). 가는 글씨라 44px 이상에서만 쓴다.
  - 숫자·금액·STEP 라벨·체크리스트 항목: **깍두기 도면체(Kkakdugi)** 400/700. 설계도 느낌이라 '비밀노트' 컨셉과 맞는다. 한 화면에 한두 군데만 포인트로 쓰고, 긴 문장에는 쓰지 않는다. (OFL, 저장소 포함)
  - 후킹 한 줄·강조 문구: **차이 라이징체(RisingCHAI)** 800. 비공개 저장소 insu-assets 에 있다. 받지 못했을 때를 대비해 Paperlogy 900으로 대체되도록 `font-family:RisingCHAI,Paperlogy` 로 지정한다.
  - 한 영상에 폰트는 최대 3종까지.
  - 노트형 손글씨(파란 펜·빨간 펜)는 나눔펜 유지.
  - 오이냉체 파일은 재배포 금지 라이선스라 저장소에 없다. 작업 폴더에 없으면 Pretendard로 대체되니 그대로 진행한다.
- **본문(캡션):** 첫 줄 = 훅, 한 줄 25자 안쪽, 문장 사이 대시(—) 금지, 해시태그 최대 5개(항상 #보험비밀노트 포함), 마지막에 "저장" 또는 "팔로우" 유도. 상담 유도가 필요한 주제만 "프로필 링크".
- **표현:** "무조건", "100%", "최고" 같은 단정·과장 금지. 상품마다 다른 내용은 "~할 수 있어요", "~경우가 많아요". 보험사 비방 금지.

## 2. 상태 파일
- `generator/shorts/plan/YYYY-MM-DD.json`
```json
{"date":"2026-11-10","status":"proposed|approved|partial|produced|skipped","proposed_at":"ISO",
 "slots":[{"slot":"13:00","ep":"ep09","category":2,"topic":"","hook":"","outline":["장면1",".."],"format":"note_dark","voice":"ko-KR-SunHiNeural","sources":["url"],"approved":null,"modify":""},
          {"slot":"18:00","ep":"ep10", "...":"..."}]}
```
- `generator/shorts/experiments.csv`: 제작할 때마다 한 줄 추가 (date,id,topic,format,voice,edit,hook,bgm,length_s,utm_content,...).
- 텔레그램 보내기: `publish/outbox/<YYYYMMDD-HHMM>-<이름>.json` 에 `{"text":"...", "video":"publish/media/epNN.mp4"(선택)}` 를 만들고 push → tg 워크플로가 자동 전송.
- 텔레그램 답장 읽기: tg 워크플로를 `inputs[mode]=poll` 로 실행 → 40초 후 `git pull` → `publish/inbox/latest.json` (messages: date(unix), text).

## 3. 아침 주제 제안 (매일)
1. 오늘 plan 파일이 이미 있으면 중단.
   - `generator/shorts/requests.md` 의 본부장님 요청을 먼저 읽고 반영한다.
   - `publish/queue` 에 오늘 13:00 또는 18:00 으로 이미 approved 된 영상이 있으면 그 슬롯은 새로 제안하지 않는다(plan 의 해당 슬롯에 ep 와 "fixed": true 로 기록하고 보고에 "확정"으로 표시). 포맷·목소리 로테이션 계산에도 그 영상을 포함한다.
2. 리서치 → 2개 주제 확정 (규칙 1 전부 적용). 다음 ep 번호는 experiments.csv 마지막 번호 +1.
3. plan 파일 저장(status=proposed, proposed_at) 후 텔레그램 전송. 형식:
```
📋 오늘 업로드 주제 (11/10 화)

1️⃣ 13:00 · 다크노트 · 여성 음성
"훅 문장"
· 핵심 내용 3줄 요약
· 참고: 최근 인기 영상 유형

2️⃣ 18:00 · 카톡형 · 남성 음성
...

✅ 둘 다 진행: "승인"
✅ 하나만: "1번 승인"
✏️ 수정: "2번 주제 ○○로 바꿔"
⏸ 쉬기: "보류"
(12시까지 답이 없으면 오늘은 쉬어요)
```

## 4. 승인 확인·제작 (09~12시 매시 실행)
1. 오늘 plan 이 없거나 status 가 produced/skipped 면 중단. (partial 이면 남은 슬롯만 확인. "fixed": true 슬롯은 제작하지 않는다)
2. tg poll 실행 → proposed_at 이후 메시지만 해석.
   - "승인/ㅇㅋ/오케이/좋아/진행/고고" → 두 슬롯 승인. "1번 승인" → 해당 슬롯만.
   - "N번 … 바꿔/수정" → 그 내용대로 주제·포맷을 고친 뒤 승인으로 처리.
   - "보류/취소/쉬자" → status=skipped, 텔레그램 "오늘은 쉴게요" 전송, 종료.
   - 해석이 애매하면 승인으로 보지 않고 텔레그램으로 한 줄 되묻는다.
3. 승인 메시지가 없고 지금이 12시 실행이면: status=skipped, 텔레그램 "승인이 없어 오늘은 쉬어요" 전송.
4. 승인된 슬롯 제작:
   1. 대본(장면별 나레이션) 작성 → `tts/requests/<날짜>_bsn_<ep>.json` push → tts 워크플로 완료까지 대기(`tts/out/<id>/done.json`, 15초 간격 최대 6분).
   2. 템플릿으로 페이지 작성: 노트형은 `/home/claude/build/note_head.html` + 장면들 + `note_tail.html` (번호 장면 체크리스트는 본문 앞 `<script>window.NOTE_ITEMS=[...]</script>`), 다크노트는 head 에 `<link rel="stylesheet" href="dark_note.css">` 추가. 예시: `generator/kit/examples/`. 카톡형 `kakao.html`, 잠금화면형 `lock.html` 을 고쳐서 사용.
   3. 미리보기(`python3 generator/kit/render_any.py page.html durs.json prev preview`)로 몇 장 확인: 글자 겹침·넘침·빈 화면 없을 것.
   4. `BUILD=/home/claude/build python3 /home/claude/insu-photobank/generator/kit/fast_build.py page.html <tts_out_dir> <접두어> /home/claude/insu-photobank/publish/media/<ep>.mp4 [bgm] /home/claude/insu-photobank/publish/media/<ep>.jpg`
   5. `publish/queue/<ep>.json`: video, cover, caption, publish_at(오늘 13:00 또는 18:00 +09:00), status=approved, yt_status=approved, yt_title(훅 + " #Shorts").
   6. experiments.csv 한 줄 추가, plan status 갱신(produced 또는 partial).
   7. 텔레그램: 영상 미리보기(video) + 본문 + "13:00 게시 예정" 전송.
5. 이미 게시 시각이 지났으면 즉시 게시되도록 publish_at 을 현재 시각으로.

## 5. 월요일 주간 리포트
1. insights 워크플로 실행(days=8) → 완료 후 pull → `publish/insights/<오늘>.json`.
2. experiments.csv 와 queue 파일을 합쳐 지난주 영상별로 포맷·목소리·주제갈래·훅 유형과 성과(좋아요·댓글·조회·저장·공유)를 표로 정리.
3. 반응 좋았던 영상 TOP 3는 왜 좋았는지(훅, 주제 대상 범위, 포맷, 길이, 업로드 시간) 분석, 하위 영상은 이유와 개선점.
4. 이번 주 방향 제안 3줄 (주제 갈래 비중, 포맷, 목소리).
5. 오류: queue 의 status=error / yt_status=error, 워크플로 실패, insights errors 를 모아 원인과 해결 방법을 쉬운 말로. 본부장님이 직접 해야 하는 일은 단계별로.
6. 텔레그램으로 전송 (길면 나눠서). 리포트 원문은 `generator/shorts/reports/<날짜>.md` 에도 저장.

## 6. 알려진 제한 (리포트에 반영)
- 인스타 조회·도달·저장·공유: 메타 앱에 instagram_manage_insights 권한이 없어 지금은 좋아요·댓글만 수집됨.
- 유튜브 통계: 업로드 토큰에 youtube.readonly 범위가 없어 수집 안 됨 (OAuth Playground에서 youtube.upload + youtube.readonly 로 토큰 재발급하면 해결).
- 유튜브 API 미심사: 업로드 영상이 비공개로 고정될 수 있음 → 스튜디오에서 공개 전환 필요.
- 게시 정시성: Supabase `bsn_publish_tick` 크론(publish/supabase_cron.sql)이 없으면 GitHub 예약 실행이 늦어질 수 있음.
