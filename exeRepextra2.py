'''
#valor = m2*120 - distCentro*2

for m2 in range(30, 80, 10):
    for dist in range(0, 1000, 100):
        valor = m2 * 120 - dist * 2
        print(f'{valor} = m2:{m2} e dist:{dist}')

'''

inicio = 151

for ano in range(2001, 2024):
    inicio = inicio * 1.04
    print(f'{ano} - {inicio}')