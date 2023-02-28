import math
a = float(input('digite o valor'))
b = float(input('digite o valor'))
c = float(input('digite o valor'))

delta = b**2 - 4*a*c

if(delta > 0):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'as raizes sao {x2} e {x1}')
elif(delta == 0):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print(f'a raiz e {x1}')
else:
    print('nao tem raizes reais')
