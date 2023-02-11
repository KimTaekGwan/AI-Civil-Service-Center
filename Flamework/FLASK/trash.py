# 버리긴 아까워서 여기다 둠
# sound는 돌아감
# def sound():
#     num = 0
#     all_frame = []
#     global te
#     while te:
#         CHUNK = 1024
#         FORMAT = pyaudio.paInt16
#         CHANNELS = 1
#         RATE = 44100
#         RECORD_SECONDS = 5
#         p = pyaudio.PyAudio()
#         print('default',p.get_default_input_device_info())
#         stream = p.open(format = FORMAT,
#                     channels = CHANNELS,
#                     rate = RATE,
#                     input = True,
#                     frames_per_buffer = CHUNK)
#         print('음성녹음 시작합니다.')
#         frames = []
#         num += 1
#         print('저장된 num은', num)
#         for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
#             data = stream.read(CHUNK)
#             frames.append(data)
#         print('음성녹음 완료했습니다.')
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
        
#         WAVE_OUTPUT_FILENAME = f'test{num}.wav'
#         wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))
#         wf.close()
#         print('안녕 난 append')
#         all_frame.append(frames)
#     all_frame = sum(all_frame, [])
#     wf = wave.open('test_total.wav', 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(all_frame))
#     wf.close()


# input output 디바이스 확인하기
# import pyaudio
# audio = pyaudio.PyAudio()
# for index in range(audio.get_device_count()):
#     desc = audio.get_device_info_by_index(index)
#     print("DEVICE: {device}, INDEX: {index}, RATE: {rate} ".format(
#         device=desc["name"], index=index, rate=int(desc["defaultSampleRate"])))
# import pyaudio
# audio = pyaudio.PyAudio()
# print(audio.get_default_input_device_info())
    
# {'index': 1, 'structVersion': 2, 'name': 'Built-in Output', 
#  'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 2,
#  'defaultLowInputLatency': 0.01, 'defaultLowOutputLatency': 0.012607709750566893,
#  'defaultHighInputLatency': 0.1,
#  'defaultHighOutputLatency': 0.022766439909297054, 'defaultSampleRate': 44100.0}


# def sound_storage():
#     import wave
#     wf = wave.open('test_total.wav', 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(all_frame))
#     wf.close()
# def sound_storages(frame,WAVE_OUTPUT_FILENAME):
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(self.RATE)
#     wf.writeframes(b''.join(frame))
#     wf.close()


