import wave
import numpy as np
import pyttsx3

def generate_audio_from_text(text, sample_rate=44100):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Đặt tốc độ nói
    engine.setProperty('volume', 0.9)  # Đặt âm lượng
    
    engine.save_to_file(text, 'temp_audio.wav')
    engine.runAndWait()

    with wave.open('temp_audio.wav', 'rb') as wf:
        audio_data = wf.readframes(-1)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)
    
    return audio_data

def write_wav_file(file_path, audio_data, sample_rate=44100):
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)  # mono audio
        wf.setsampwidth(2)  # 2 bytes per sample
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

if __name__ == "__main__":
    texts = [
        "Hello, this is the first voice.",
        "This is the second voice.",
        "And this is the third voice.",
        "Finally, this is the fourth voice."
    ]
    
    combined_audio = np.array([], dtype=np.int16)
    
    for text in texts:
        audio_data = generate_audio_from_text(text)
        combined_audio = np.concatenate((combined_audio, audio_data))
    
    write_wav_file("generated_audio.wav", combined_audio)
    
    print("File 'generated_audio.wav' has been created.")
