texto = 'eu amo cajazeiras'

crp = []
decrp = []
for i in texto:
    alterada = ord(i) + 3
    convert = chr(alterada)
    crp.append(convert)

print(*crp)


for j in crp:
    alterada = ord(j) - 3
    convert = chr(alterada)
    decrp.append(convert)

print(*decrp)

