menor = 100
maior = -100
soma = 0
qtde = 0
resp = input('digite sim para informar outra tempeturatura, caso contrario digite nao')
entrou = False

while(resp == 'sim'):
    entrou = True
    qtde = qtde + 1
    temp = int(input('digite a temperatura'))
    soma = soma + temp

    if(temp < menor):
        menor = temp

    if(temp > maior):
        maior = temp

    resp = input('digite sim para informar outra tempeturatura, caso contrario digite nao')

if(entrou == True):

    print(f'a menor temperatura lida foi {menor}')
    print(f'a maior temperatura lida foi {maior}')
    media = soma / qtde
    print(f'a media de temperaturas foi {media}')
else:
    print('nenhuma temperatura foi informada')