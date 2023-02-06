from flask import Flask, render_template, redirect, url_for, jsonify,request
import pyaudio
import numpy as np

# bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/', methods = ['GET', 'POST'])

import wave
# from playsound import playsound


def sound():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = r'test3.wav'
    
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)
    print('음성녹음 시작합니다.')
    frames = []

    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print('음성녹음 완료했습니다.')

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def test():
    print('gsdg')
    while True:
        print('나는 계속 트루 이다.......')
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        # sound()
        print(request.form)
        print('hello')
        # test()
        # print('asdasdasd')
        return render_template('main.html')
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)    