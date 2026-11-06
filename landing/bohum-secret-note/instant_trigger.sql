-- 보험비밀노트: 신청이 들어오는 즉시 GitHub 동기화(leads.yml)를 실행시키는 트리거
-- 1) 아래 '여기에_토큰_붙여넣기' 부분만 본인 GitHub 토큰으로 바꾸고 전체 실행
-- 토큰은 Supabase Vault에 암호화 저장되고, 이 파일에는 남지 않는다.

delete from vault.secrets where name = 'gh_dispatch_token';
select vault.create_secret('여기에_토큰_붙여넣기', 'gh_dispatch_token');

create extension if not exists pg_net;

create or replace function public.bsn_notify_github()
returns trigger
language plpgsql
security definer
set search_path = public, extensions
as $$
declare tok text;
begin
  select decrypted_secret into tok
    from vault.decrypted_secrets where name = 'gh_dispatch_token' limit 1;
  if tok is null then return new; end if;
  perform net.http_post(
    url := 'https://api.github.com/repos/seongjerry/insu-photobank/dispatches',
    headers := jsonb_build_object(
      'Authorization', 'Bearer ' || tok,
      'Accept', 'application/vnd.github+json',
      'User-Agent', 'bsn-supabase-trigger',
      'Content-Type', 'application/json'),
    body := jsonb_build_object('event_type', 'new_lead')
  );
  return new;
exception when others then
  return new;  -- 알림이 실패해도 신청 저장은 절대 막지 않는다 (5분 예약이 보완)
end $$;

revoke all on function public.bsn_notify_github() from public, anon, authenticated;

drop trigger if exists bsn_leads_notify on public.bsn_leads;
create trigger bsn_leads_notify
  after insert on public.bsn_leads
  for each row execute function public.bsn_notify_github();

-- 확인용: 최근 호출 결과 (status_code 204면 성공)
-- select id, status_code, created from net._http_response order by created desc limit 5;
