'''
desenvolva um programa em python para ler o nome de 10 pessoas.
Quando for digitado o nome 'maria', o programa deve informar
quantas pessoas foram lidas até ali e quantas faltaram para completar
as 10 pessoas

'''

cont1 = 0

for nomes in range(1,11):
    nome = input('digite seu nome')

    cont1 = cont1 + 1
    if(nome == 'maria'):
        break

print(f'quantidade de nomes lidos: {cont1}')
print(f'faltaram  {10 - cont1} nomes')