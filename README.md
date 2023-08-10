# KeyFrames
 Script para identificação dos tempos de quadros-chave de um video.

 Este script foi feito para converter uma lista de segundos de um video, para hora/minuto/segundo.
 A lista de segundos, correspondente aos keyframes pode ser obtida com o software ffmpeg.

 O ffmpeg é um editor de video por linha de comando, e este é o comando para obter a lista:
 `ffprobe -loglevel error -skip_frame nokey -select_streams v:0 -show_entries frame=pts_time -of csv=print_section=0 video.mp4 > KeyFramesList.txt`

 No Windows, esse comando pode ser colado no bloco de notas e então salvo com a extensão ".bat".
 Então executado com um duplo clique, desde que o "arquivo.bat" esteja na mesma pasta que o video.

 No Linux basta abrir a pasta do video no terminal e colar o comando.

 O resultado deste comando será o arquivo "KeyFramesList.txt".
 Que será utilizado por este script, para formar o arquivo de texto "KeyFramesTimes.txt".
 Contendo os tempos de cada quadro-chave do video analisado.
 