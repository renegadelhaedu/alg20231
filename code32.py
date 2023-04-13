#listas
#lista é uma estrutura de dados

import random

dezenas = [23, 11, 4, 44, 12, 30]
qtde = 0
while(len(dezenas) > 0):
    num = random.randint(1,60)
    qtde += 1
    for i in dezenas:
        if( num == i):
            dezenas.remove(num)
            break
    print(f'chutou {num} e o tamanho da lista {len(dezenas)}')

print(f'numero de tentivas foi {qtde}')