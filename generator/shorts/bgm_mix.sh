#!/bin/bash
# 사용: bgm_mix.sh 음성효과음.wav 배경음.wav 출력.wav [배경음 dB, 기본 -25]
V=$1; B=$2; O=$3; G=${4:--37}
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ffmpeg -y -v error -i "$V" -stream_loop -1 -i "$B" -filter_complex \
"[1:a]atrim=0:$D,loudnorm=I=${G}:TP=-9:LRA=7,afade=t=in:d=0.6,afade=t=out:st=$(echo "$D-1.5"|bc):d=1.5[b];\
[0:a]asplit=2[v][k];[b][k]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400:makeup=1[bd];\
[v][bd]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[o]" -map "[o]" -ar 44100 -ac 2 "$O"
