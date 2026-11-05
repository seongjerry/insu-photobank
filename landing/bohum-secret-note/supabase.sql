-- 보험비밀노트 상담 신청 테이블 (Supabase SQL Editor에서 실행)
create table if not exists public.bsn_leads (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  name text not null check (char_length(name) between 2 and 20),
  phone text not null check (phone ~ '^01[016789]-?[0-9]{3,4}-?[0-9]{4}$'),
  topic text check (char_length(topic) <= 200),
  call_time text check (char_length(call_time) <= 20),
  marketing_agree text check (char_length(marketing_agree) <= 10),
  page_topic text check (char_length(page_topic) <= 30),
  utm_source text check (char_length(utm_source) <= 100),
  utm_medium text check (char_length(utm_medium) <= 100),
  utm_campaign text check (char_length(utm_campaign) <= 200),
  utm_content text check (char_length(utm_content) <= 200),
  utm_term text check (char_length(utm_term) <= 200),
  referrer text check (char_length(referrer) <= 500),
  submitted_at text check (char_length(submitted_at) <= 40),
  notified_at timestamptz,
  sheet_synced_at timestamptz
);

alter table public.bsn_leads enable row level security;

-- 랜딩페이지(익명)는 '추가'만 가능. 조회·수정·삭제 정책이 없으므로 외부에서 데이터를 읽을 수 없음
drop policy if exists "landing insert only" on public.bsn_leads;
create policy "landing insert only" on public.bsn_leads
  for insert to anon
  with check (notified_at is null and sheet_synced_at is null);

revoke select, update, delete on public.bsn_leads from anon, authenticated;
