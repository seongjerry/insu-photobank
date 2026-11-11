"""보험비밀노트 캐러셀 표지 틀 4종 (2026-11-11 본부장님 선택: A1·A2·B1·B2)

에피소드 번호로 순서가 정해진다: c01 A1 → c02 B1 → c03 A2 → c04 B2 → c05 A1 ...
    from covers import cover, layout_for
    COVERS = {"a": cover(layout_for(ID_NUM), ...)}

공통 고정: 어두운 배경, Paperlogy 제목, 하단 @insu_secretnote 줄, 상단 시리즈 문구·쪽번호 없음.
바꾸는 것: 사진(주제별), 비노 포즈(같은 포즈 주 1회), 강조색(y 노랑·r 빨강·b 파랑), 훅 유형(비밀·질문·반전·숫자).
제목 안에서 강조할 부분은 <span class="y|r|b">...</span> 으로 감싼다.
사진 속 인물을 질병 당사자로 단정하지 않는다. 얼굴보다 손·뒷모습·풍경 사진을 우선한다.
"""
import pathlib
from kit import bino

R = pathlib.Path(__file__).resolve().parents[2]
ORDER = ["A1", "B1", "A2", "B2"]


def layout_for(n):
    """에피소드 번호(1, 2, ...) → 표지 틀"""
    return ORDER[(int(n) - 1) % len(ORDER)]


def _ph(p):
    return (R / p).as_uri()


def cover(kind, title, chip="", sub="", photo="", pose="wow", accent="y", big="", big_label="", source=""):
    """kind: A1|A2|B1|B2
    A1 사진 전면 + 하단 제목 (비밀형 훅에 잘 맞음). photo, chip, title
    A2 사진 위 + 아래 제목 (질문형). photo, chip(작은 윗줄), title, sub
    B1 제목 위 + 비노 가운데 (반전형). title, pose, chip(아래 알약)
    B2 큰 숫자 + 비노 옆 (숫자형). big("23.1%"), big_label(숫자 위 설명), title, pose, source
    """
    acc = {"y": "#FFE45C", "r": "#FF6B6B", "b": "#7FB2FF"}[accent]
    if kind == "A1":
        return f"""
<div style="position:absolute;inset:0;background:url({_ph(photo)}) center/cover;filter:grayscale(1) contrast(1.1) brightness(.75)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.1) 30%,rgba(0,0,0,.92) 72%)"></div>
{f'<span class="chip" style="position:absolute;left:72px;top:700px;background:transparent;color:{acc};border:3px solid {acc}">{chip}</span>' if chip else ''}
<h1 style="position:absolute;left:72px;right:72px;top:790px">{title}</h1>"""
    if kind == "A2":
        return f"""
<div style="position:absolute;left:0;right:0;top:0;height:690px;background:url({_ph(photo)}) center 40%/cover;filter:grayscale(1) brightness(.85)"></div>
<div style="position:absolute;left:0;right:0;top:560px;height:130px;background:linear-gradient(transparent,#121212)"></div>
<div style="position:absolute;left:72px;right:72px;top:780px">
 {f'<p style="font-size:36px;color:#9E9E9E;font-weight:700">{chip}</p>' if chip else ''}
 <h1 style="margin-top:18px;font-size:90px">{title}</h1>
 {f'<p style="margin-top:28px;font-size:34px;color:#BDBDBD">{sub}</p>' if sub else ''}
</div>"""
    if kind == "B1":
        return f"""
<h1 style="text-align:center;margin-top:40px;font-size:88px">{title}</h1>
{bino(pose, 640, 'position:absolute;left:220px;top:420px')}
{f'<span class="chip" style="position:absolute;left:50%;transform:translateX(-50%);top:1130px;background:{acc}">{chip}</span>' if chip else ''}"""
    if kind == "B2":
        return f"""
{bino(pose, 620, 'position:absolute;right:-90px;top:470px;transform:rotate(-8deg)')}
<p style="font-size:38px;color:#9E9E9E;font-weight:700;margin-top:40px">{big_label}</p>
<div style="font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:260px;line-height:1;color:{acc};margin-top:10px;letter-spacing:-.04em">{big}</div>
<h1 style="position:absolute;left:72px;top:640px;font-size:84px;width:560px">{title}</h1>
{f'<p style="position:absolute;left:72px;top:1060px;font-size:33px;color:#BDBDBD;width:470px">{source}</p>' if source else ''}"""
    raise ValueError(kind)
