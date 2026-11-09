-- 인스타 예약 게시를 10분마다 정확히 깨우는 Supabase 크론 (GitHub 예약 실행 지연 보완)
-- gh_dispatch_token(Vault)은 보험비밀노트 즉시 동기화 때 넣어둔 토큰을 재사용한다.
create extension if not exists pg_cron;
create extension if not exists pg_net;
select cron.unschedule('bsn_publish_tick') where exists (select 1 from cron.job where jobname='bsn_publish_tick');
select cron.schedule('bsn_publish_tick', '*/10 * * * *', $$
  select net.http_post(
    url := 'https://api.github.com/repos/seongjerry/insu-photobank/dispatches',
    headers := jsonb_build_object(
      'Authorization', 'Bearer ' || (select decrypted_secret from vault.decrypted_secrets where name = 'gh_dispatch_token' limit 1),
      'Accept', 'application/vnd.github+json', 'User-Agent', 'bsn-cron', 'Content-Type', 'application/json'),
    body := '{"event_type":"publish_tick"}'::jsonb)
$$);
select jobname, schedule, active from cron.job where jobname = 'bsn_publish_tick';
