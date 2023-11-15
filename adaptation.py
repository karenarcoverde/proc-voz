import wave

def pitch_shift(input_file, output_file, shift_factor):
    with wave.open(input_file, 'rb') as infile:
        # Lê os parâmetros do arquivo de áudio original
        params = infile.getparams()
        framerate = params.framerate
        nframes = params.nframes
        audio_data = infile.readframes(nframes)

    # Ajusta a taxa de quadros (isso também altera o pitch)
    new_framerate = int(framerate * shift_factor)

    # Cria um novo arquivo de áudio com o pitch alterado
    with wave.open(output_file, 'wb') as outfile:
        # Define os mesmos parâmetros, mas com uma nova taxa de quadros
        outfile.setparams((params.nchannels, params.sampwidth, new_framerate, params.nframes, params.comptype, params.compname))
        outfile.writeframes(audio_data)

# Uso do função
pitch_shift('Patinho.wav', 'helium_audio.wav', 1.5)  # Aumenta o pitch em 50%