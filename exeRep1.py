nota = float(input('digite sua nota'))

while(nota < 0 or nota > 10):
    print('invalida')
    nota = float(input('digite sua nota novamente'))

print('agora sim vc colocou uma nota valida')