import pyaudio
import wave

def record_audio(file_name, duration, sample_rate=44100, chunk_size=1024, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=format,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording...")

    frames = []

    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    file_name = "recorded_audio.wav"
    recording_duration = 5  # in seconds

    record_audio(file_name, recording_duration)
