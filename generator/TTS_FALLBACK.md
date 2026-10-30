# 나레이션 대체 경로 (edge-tts 가 막힐 때)
클라우드 프록시가 speech.platform.bing.com(edge-tts)을 403으로 막는다. huggingface.co 도 막혀 있다. GitHub 릴리스 다운로드는 된다.
2026-10-30 확인된 방법: sherpa-onnx + Supertonic 3 (오프라인, 한국어 지원)
1. python3 -m pip install --break-system-packages sherpa-onnx soundfile
2. curl -SL https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/sherpa-onnx-supertonic-3-tts-int8-2026-05-11.tar.bz2 후 압축 해제 (경로는 generator/tts_supertonic.py 의 M 변수)
3. sid 0~4 는 여성, 5~9 는 남성(음높이로 확인). speed 는 1.1 이 적당. 1.3 은 숫자가 뭉개진다. 숫자는 한글로 풀어 쓰면 더 정확(5분은 "오 분")
4. 장면별 wav 를 ffmpeg 로 mp3(44100)로 바꿔 tts/out/<id>/NN.mp3 에 넣고 insu_render.py 실행
5. 검수: sherpa-onnx SenseVoice(asr-models 릴리스)로 받아쓰기해 문장 확인
참고: Playwright 는 python 패키지가 브라우저 빌드(/opt/pw-browsers 의 1243)와 맞아야 한다: pip install playwright==1.63.0
참고: apt 의 PIL 이 깨져 있으면 pip install --ignore-installed pillow
