# insu-photobank · 무료 사진·나레이션 자동 수집 저장소

Pexels(+Pixabay) 무료 사진을 매주 월요일 새벽 자동으로 받아 `photos/`에 쌓고 `index.json`에 태그를 기록합니다.
`tts/requests/`에 대본 JSON이 올라오면 edge-tts로 한국어 나레이션 mp3를 만들어 `tts/out/`에 커밋합니다.
Claude 콘텐츠 생성기(insu_magazine)가 이 저장소를 읽어 캐러셀·릴스에 사진과 소리를 입힙니다.

## 설정 (최초 1회)
1. https://www.pexels.com/api/ 에서 무료 API 키 발급 (가입만 하면 즉시)
   선택: https://pixabay.com/api/docs/ 키도 발급하면 사진 수 2배
2. Settings → Secrets and variables → Actions → New repository secret
   - `PEXELS_API_KEY` = 발급한 키 (Pixabay는 `PIXABAY_API_KEY`)
3. Actions 탭 → photobank → Run workflow (첫 수집, 약 5~10분)

## 라이선스
- Pexels License / Pixabay Content License: 상업적 이용 가능, 출처 표기 불필요, 사진 자체를 판매하는 용도만 금지
- 주의: 사진 속 인물이 특정 질병·사건의 당사자인 것처럼 단정하는 캐션은 피하기 (두 라이선스 공통 조건)
- `index.json`의 `credit`·`page`에 작가와 원본 링크를 함께 저장하므로 필요하면 언제든 출처 확인 가능
- 나레이션: edge-tts(무료). BGM은 `bgm/` 폴더에 무료 음원 mp3를 넣으면 생성기가 사용

## 키워드 조정
`keywords.json`의 `queries`를 바꾸면 다음 주 수집부터 반영. 당장 받으려면 Actions에서 Run workflow.
