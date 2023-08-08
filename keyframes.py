with open('KeyFramesList.txt', 'rt') as arquivo:
    lista = arquivo.readlines()

gravar = []

for item in lista:
    keyframe = ''
    barra = item.find('.') + 7
    if barra == 6:
        item = '0.000000'
        barra = 8
    corrigido = float(item[0:barra]) - 0.1
    if corrigido < 0:
        corrigido = 0.0
    mili = corrigido % 1
    seg = int(corrigido // 1)
    if seg >= 60:
        if seg >= 3600:     # Bloco das horas
            hora = seg // 3600
            seg = seg - (hora * 3600)
            h = (str(hora) if hora > 9 else ('0' + str(hora))) + ':'
            if seg >= 60:
                minuto = seg // 60
                seg = seg - (minuto * 60)
                m = (str(minuto) if minuto > 9 else ('0' + str(minuto))) + ':'
                segmili = round((seg + mili), 6)
                s = str(segmili) if seg > 9 else ('0' + str(segmili))
                keyframe = h + m + s + '\n'
                print(keyframe, end='')
            else:
                segmili = round((seg + mili), 6)
                s = str(segmili) if seg > 9 else ('0' + str(segmili))
                keyframe = h + '00:' + s + '\n'
                print(keyframe, end='')
        else:   # Bloco dos minutos
            minuto = seg // 60
            seg = seg - (minuto * 60)
            m = (str(minuto) if minuto > 9 else ('0' + str(minuto))) + ':'
            segmili = round((seg + mili), 6)
            s = str(segmili) if seg > 9 else ('0' + str(segmili))
            keyframe = '00:' + m + s + '\n'
            print(keyframe, end='')
    else:   # Bloco dos segundos
        s = str(round(corrigido, 6)) if seg > 9 else ('0' + str(round(corrigido, 6)))
        keyframe = '00:00:' + s + '\n'
        print(keyframe, end='')
    gravar.append(keyframe)

with open('KeyFramesTimes.txt', 'wt+') as kf:
    kf.writelines(gravar)
