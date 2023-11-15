# proc-voz

https://librosa.org/doc/latest/recordings.html <br>
https://www.educative.io/answers/librosa-library-in-python <br>
https://www.javatpoint.com/librosa-library-in-python <br>
https://medium.com/strategio/using-librosa-to-change-the-pitch-of-an-audio-file-49efdb2dd6c

<br>


need ffmpeg.exe e ffplay.exe

<br>
Este trecho do código é responsável por alterar a taxa de quadros (ou taxa de amostragem) do arquivo de áudio. Vamos dividir a explicação em partes:

Taxa de Quadros (Framerate) ou Taxa de Amostragem:

A taxa de quadros, também conhecida como taxa de amostragem, é uma medida de quantas amostras de áudio são capturadas por segundo. É medida em Hertz (Hz). Por exemplo, uma taxa de amostragem comum para CDs é de 44.100 Hz, o que significa que 44.100 amostras são gravadas por segundo.
O que Acontece Quando Alteramos a Taxa de Amostragem:

Quando aumentamos a taxa de amostragem de um arquivo de áudio sem alterar o conteúdo do áudio, estamos efetivamente acelerando a reprodução desse áudio. Isso porque estamos dizendo ao reprodutor para tocar mais amostras por segundo do que antes.
Ao acelerar a reprodução, o pitch (altura tonal) do áudio também aumenta. É semelhante ao que acontece quando você toca um disco de vinil mais rápido do que sua velocidade normal.
Shift Factor:

O shift_factor é um número pelo qual multiplicamos a taxa de amostragem original. Se o shift_factor for maior que 1, a taxa de amostragem será aumentada, o que acelera a reprodução do áudio e aumenta seu pitch.
Por exemplo, um shift_factor de 1.5 multiplicará a taxa de amostragem original por 1.5. Se a taxa de amostragem original fosse 44.100 Hz, a nova taxa de amostragem será de 66.150 Hz.
Aplicação Prática:

No código, new_framerate = int(framerate * shift_factor) calcula a nova taxa de amostragem multiplicando a taxa de amostragem original pelo fator de mudança.
Isso é usado para criar um novo arquivo de áudio com a taxa de amostragem alterada, resultando em um áudio com pitch mais alto.
