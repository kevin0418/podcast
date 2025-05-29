import sounddevice as sd
import soundfile as sf

# WAV 파일 읽기
path = "happy-podcast.wav"
data, sample = sf.read(path)

sd.play(data, sample)

# 소리 재생데이터data, sanple)
sd.wait()  # 재생이 끝날 때까지 대기



# # pip install sounddevice soundfile
# import sounddevice as sd
# import soundfile as sf

# # WAV 파일 읽기
# path = "happy-podcast.wav"
# data, sample = sf.read(path)

# # 소리 재생
# sd.play(data, sample)  # 여기가 잘못되었었네요
# sd.wait()  # 재생이 끝날 때까지 대기