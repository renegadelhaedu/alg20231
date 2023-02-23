numero1 = int(input('digite um numero'))
numero2 = int(input('digite um numero'))
numero3 = int(input('digite um numero'))

if(numero1 > numero2):
    if(numero1 > numero3):
        print(f'o maior eh o numero {numero1}')

if(numero2 > numero1):
    if(numero2 > numero3):
        print(f'o maior eh o numero {numero2}')

if(numero3 > numero1):
    if(numero3 > numero2):
        print(f'o maior eh o numero {numero3}')