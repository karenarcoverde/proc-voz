import numpy as np
import sounddevice as sd
import librosa
import soundfile as sf

def robotize_voice_by_removing_phase(input_path, output_path):
    y, sr = librosa.load(input_path, sr=None)
    
    # Calcula a transformada de Fourier de curta duração
    D = librosa.stft(y)
    
    # Mantém apenas a magnitude e descarta a fase
    magnitude = np.abs(D)
    
    # Reconstrói o sinal usando somente a magnitude (fase zero)
    y_no_phase = librosa.istft(magnitude)
    # Salva o áudio resultante em um arquivo
    sf.write(output_path, y_no_phase, sr)
    # Reproduzindo o áudio usando sounddevice
    sd.play(y_no_phase, sr)
    
    # Esperando o áudio terminar de tocar
    sd.wait()

input_audio_file = "Patinho.wav"
output_audio_file = "Patinho_robotizado.wav"
robotize_voice_by_removing_phase(input_audio_file, output_audio_file)




