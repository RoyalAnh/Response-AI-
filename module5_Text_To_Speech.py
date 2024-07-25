from gtts import gTTS
import os
from io import BytesIO
import pygame

def load_answer(file_path="output.txt"):
    with open(file_path, "r") as f:
        answer = f.read()
    return answer

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    return tts

def play_audio(tts):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Save tts to a BytesIO object
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Load the audio data from BytesIO
    pygame.mixer.music.load(audio_fp)
    pygame.mixer.music.play()

    # Keep the program running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

def module5():
    answer = load_answer()
    tts = text_to_speech(answer)
    play_audio(tts)
