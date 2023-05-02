#dicionário
#estrutura de dados = chave - valor

#pessoas = dict()
#pessoas = {}
pessoas = {'jose':56, 'maria':68, 'carlos':31}

soma = 0
for x in pessoas:
    soma += pessoas[x]
    print(pessoas[x])

media = soma / len(pessoas)
print(f'a media das idades e {media}')