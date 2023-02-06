from flask import Flask, render_template, redirect, url_for, jsonify,request
import pyaudio
import numpy as np
# bp = Blueprint('main', __name__, url_prefix='/')
# @bp.route('/', methods = ['GET', 'POST'])
import time
import wave
# from playsound import playsound

## 한 것: 웹에서 실시간 마이크 녹음 시작 -> 5초마다 파일 저장 -> 녹음 중지 누르면 녹음이 중지.
## 수정 할 것: 마이크 볼륨으로 판별하던가(볼륨이 줄어들면 자동으로 파일이 저장 되거나 / 파일이 저장 될 때 1: 안 / 2: 녕으로
# 끊길 경우 어떻게 해결해 나갈 것 인가??) 
# 전역 변수로 지정을 해놨는데 다른 방법이 있나??? 글로벌을 플라스크 내장 글로벌로 변경해도 좋을 것 같다.

te = False
def sound():
    num = 0
    global te
    while te:
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 5
        p = pyaudio.PyAudio()
        stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)
        print('음성녹음 시작합니다.')
        frames = []
        num += 1
        print('저장된 num은', num)
        for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print('음성녹음 완료했습니다.')
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        WAVE_OUTPUT_FILENAME = f'test{num}.wav'
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        global te
        result = request.get_json()["subNm"]
        if result == 'hi':
            te = True
            sound()
            return jsonify({'msg':'hihifsfsfs'})
        elif result == 'finish':
            te  = False
            return jsonify({'msg':'사용 가능한 닉네임입니다.'})
        
        return jsonify({'msg':'사용 가능한 닉네임입니다.'})
        # return render_template('main.html')
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)    