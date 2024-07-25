import pyaudio
import wave
import numpy as np
import os

def record_audio(output_folder="./", duration=7, sample_rate=44100, chunk_size=1024):
    """
    Ghi âm từ microphone và lưu vào file WAV.
    
    Parameters:
    - output_folder (str): Thư mục để lưu file WAV và dữ liệu âm thanh.
    - duration (int): Thời lượng ghi âm (đơn vị: giây).
    - sample_rate (int): Tốc độ lấy mẫu (đơn vị: Hz).
    - chunk_size (int): Kích thước mỗi khối dữ liệu ghi âm.
    
    Returns:
    - audio_data (np.array): Dữ liệu âm thanh ghi được (dạng numpy array).
    - sample_rate (int): Tốc độ lấy mẫu.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)
    print("Recording...")
    frames = []
    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16) # transform to numpy array
    
    output_file = os.path.join(output_folder, "recorded_audio.wav")
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"Audio saved to {output_file}")

    return audio_data, sample_rate

def read_audio_file(file_path):
    """
    Đọc file âm thanh và trả về dữ liệu âm thanh và tốc độ lấy mẫu.
    """
    with wave.open(file_path, 'rb') as wf:
        sample_rate = wf.getframerate()
        audio_data = wf.readframes(-1)
        audio_data = np.frombuffer(audio_data, dtype=np.int16) # transform to numpy array
    return audio_data, sample_rate

def save_audio_data(audio_data, sample_rate, output_folder="./"):
    """
    Lưu dữ liệu âm thanh và tốc độ lấy mẫu vào file trong thư mục đầu ra.
    """
    np.save(f"{output_folder}/saved_audio_data.npy", audio_data)
    with open(f"{output_folder}/sample_rate.txt", "w") as f:
        f.write(str(sample_rate))
    print(f"Audio data saved to {output_folder}.")

def module1():
    choice = input("Do you want to record audio (y/n)? ")
    if choice.lower() == 'y':
        audio_data, sample_rate = record_audio()
        output_folder = "./"  # save
    else:
        audio_file_path = input("Enter the path to the audio file: ")
        audio_data, sample_rate = read_audio_file(audio_file_path)
        output_folder = "./"  # save
    
    save_audio_data(audio_data, sample_rate, output_folder)
