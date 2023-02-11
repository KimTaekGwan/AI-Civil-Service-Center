from flask import Flask, render_template, redirect, url_for, jsonify,request
import pyaudio
import numpy as np
# bp = Blueprint('main', __name__, url_prefix='/')
# @bp.route('/', methods = ['GET', 'POST'])
import time
import wave
## 한 것: 웹에서 실시간 마이크 녹음 시작 -> 5초마다 파일 저장 -> 녹음 중지 누르면 녹음이 중지.
## 수정 할 것: 마이크 볼륨으로 판별하던가(볼륨이 줄어들면 자동으로 파일이 저장 되거나 / 파일이 저장 될 때 1: 안 / 2: 녕으로
# 끊길 경우 어떻게 해결해 나갈 것 인가??) 
# 전역 변수로 지정을 해놨는데 다른 방법이 있나??? 글로벌을 플라스크 내장 글로벌로 변경해도 좋을 것 같다.
class sound_store:
    #class 내 변수 설정 -> 이걸 False로 변경
    te = True
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.total_frame = []
    def sound_storages(self, frame,WAVE_OUTPUT_FILENAME):
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frame))
        wf.close()
    def sounds(self):
        num = 0
        while sound_store.te:
            frames = []
            num += 1
            self.p = pyaudio.PyAudio()
            stream = self.p.open(format = self.FORMAT,
                        channels = self.CHANNELS,
                        rate = self.RATE,
                        input = True,
                        frames_per_buffer = self.CHUNK)
            for i in range(0, int(self.RATE/self.CHUNK*self.RECORD_SECONDS)):
                data = stream.read(self.CHUNK)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            self.p.terminate()
            WAVE_OUTPUT_FILENAME = f'test{num}.wav'
            self.sound_storages(frames,WAVE_OUTPUT_FILENAME)
            self.total_frame.append(frames)
            
        self.total_frame = sum(self.total_frame, [])
        self.sound_storages(self.total_frame,'test_total.wav')
        
        
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        s = sound_store()
        result = request.get_json()["subNm"]
        if result == 'hi':
            s.sounds()
            return jsonify({'msg':'hihifsfsfs'})
        elif result == 'finish':
            sound_store.te  = False
            return jsonify({'msg':'사용 가능한 닉네임입니다.'})
        
        return jsonify({'msg':'사용 가능한 닉네임입니다.'})
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)    
    
