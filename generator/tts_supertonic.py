import sys, sherpa_onnx, soundfile as sf
M="/home/user/tts_model/sherpa-onnx-supertonic-3-tts-int8-2026-05-11/"
def make():
    c=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(supertonic=sherpa_onnx.OfflineTtsSupertonicModelConfig(
        duration_predictor=M+"duration_predictor.int8.onnx",text_encoder=M+"text_encoder.int8.onnx",vector_estimator=M+"vector_estimator.int8.onnx",
        vocoder=M+"vocoder.int8.onnx",tts_json=M+"tts.json",unicode_indexer=M+"unicode_indexer.bin",voice_style=M+"voice.bin"),num_threads=4,provider="cpu"))
    assert c.validate(); return sherpa_onnx.OfflineTts(c)
def gen(tts,text,out,sid,speed=1.25):
    g=sherpa_onnx.GenerationConfig(); g.sid=sid; g.num_steps=8; g.speed=speed; g.extra["lang"]="ko"
    a=tts.generate(text,g); sf.write(out,a.samples,samplerate=a.sample_rate,subtype="PCM_16"); return len(a.samples)/a.sample_rate
if __name__=="__main__":
    t=make()
    for sid in range(10): print(sid, gen(t,"딱 5분만 보고 잘게. 오늘도 하셨죠?",f"/tmp/t{sid}.wav",sid))
