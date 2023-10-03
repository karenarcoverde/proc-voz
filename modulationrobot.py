import numpy as np
import sounddevice as sd
import librosa

def robotize_voice_by_removing_phase(input_path):
    y, sr = librosa.load(input_path, sr=None)
    
    # Calcula a transformada de Fourier de curta duração
    D = librosa.stft(y)
    
    # Mantém apenas a magnitude e descarta a fase
    magnitude = np.abs(D)
    
    # Reconstrói o sinal usando somente a magnitude (fase zero)
    y_no_phase = librosa.istft(magnitude)
    
    # Reproduzindo o áudio usando sounddevice
    sd.play(y_no_phase, sr)
    
    # Esperando o áudio terminar de tocar
    sd.wait()

input_audio_file = "Patinho.wav"
robotize_voice_by_removing_phase(input_audio_file)




