/**
 * 보험비밀노트 상담 신청 → 구글 스프레드시트 기록용 Apps Script
 * 1) 새 스프레드시트 > 확장 프로그램 > Apps Script 에 이 코드를 붙여넣기
 * 2) 아래 SECRET 값을 아무 긴 문자열로 바꾸기
 * 3) 배포 > 새 배포 > 유형: 웹 앱 / 실행: 나 / 액세스: 모든 사용자 > 배포
 * 4) 나온 웹 앱 URL 끝에 ?key=SECRET값 을 붙여서 GitHub Secrets 의 SHEET_WEBHOOK_URL 로 등록
 */
const SECRET = '여기에-긴-비밀문자열-입력';
const HEADERS = ['번호', '접수시각', '이름', '연락처', '상담주제', '연락희망시간', '마케팅동의',
  '페이지주제', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', '유입경로', '상담상태', '메모'];
const KEYS = ['id', 'created_at', 'name', 'phone', 'topic', 'call_time', 'marketing_agree',
  'page_topic', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'referrer'];

function doPost(e) {
  if (!e || !e.parameter || e.parameter.key !== SECRET) return out({ ok: false, error: 'unauthorized' });
  const sh = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold').setBackground('#FFF27A');
    sh.setFrozenRows(1);
  }
  const data = JSON.parse(e.postData.contents || '{}');
  const exist = new Set(sh.getLastRow() > 1 ? sh.getRange(2, 1, sh.getLastRow() - 1, 1).getValues().map(r => String(r[0])) : []);
  let added = 0;
  (data.rows || []).forEach(r => {
    if (exist.has(String(r.id))) return; // 중복 방지
    sh.appendRow(KEYS.map(k => k === 'phone' ? "'" + (r[k] || '') : (r[k] || '')).concat(['신규', '']));
    added++;
  });
  return out({ ok: true, added });
}

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
