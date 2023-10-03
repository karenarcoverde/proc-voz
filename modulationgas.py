import numpy as np
import sounddevice as sd
import librosa

def transform_to_helium_voice(input_path, output_path):
    # Carregando o áudio
    y, sr = librosa.load(input_path, sr=None)

    # Ajustando o pitch
    y_pitch_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=8)  # Aumentar em 8 semitons para um efeito marcante

    # Convertendo o áudio modificado para um formato que o sounddevice pode reproduzir
    sounddevice_array = np.array(y_pitch_shifted * (2**15), dtype=np.int16)

    # Reproduzindo o áudio usando sounddevice
    sd.play(sounddevice_array, samplerate=sr)

    # Esperando o áudio terminar de tocar
    sd.wait()

    # Salvando o áudio modificado (opcional)
    librosa.output.write_wav(output_path, y_pitch_shifted, sr)

input_audio_file = "Patinho.wav"
output_audio_file = "path_to_your_output_audio_helium.wav"
transform_to_helium_voice(input_audio_file, output_audio_file)


