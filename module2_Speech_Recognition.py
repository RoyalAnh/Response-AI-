import speech_recognition as sr
import numpy as np

def load_audio_data(file_path="./"):
    audio_data = np.load(f"{file_path}/saved_audio_data.npy")
    with open(f"{file_path}/sample_rate.txt", "r") as f:
        sample_rate = int(f.read())
    return audio_data, sample_rate

def recognize_speech(audio_data, sample_rate):
    recognizer = sr.Recognizer()
    recognized_texts = []
    audio_chunk = sr.AudioData(audio_data.tobytes(), sample_rate, 2)
    
    try:
        recognized_text = recognizer.recognize_google(audio_chunk, language='en-US') #vi-VN
        recognized_texts.append(recognized_text)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")

    return recognized_texts

def module2():
    audio_data, sample_rate = load_audio_data()
    recognized_texts = recognize_speech(audio_data, sample_rate)
    
    if recognized_texts:
        with open("recognized_text.txt", "w") as f:
            for text in recognized_texts:
                full_text = f"(With the shortest answer), {text}"
                f.write(f"{full_text}\n")
                print(f"Recognized Text: {full_text}")
        print("Recognized text saved to recognized_text.txt")
    else:
        print("No speech detected or speech recognition failed.")

