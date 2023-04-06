numero = int(input('digite o numero para calculo do fatorial '))

fat = 1

for i in range(1, numero + 1):
    fat = fat * i
    print(fat)