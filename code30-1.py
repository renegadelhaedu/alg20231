qtde = 0
nome = 'teste'

while(nome != 'sair'):
    nome = input('digite o nome do jogador ou jogadora')

    if(nome == 'rene'):
        continue

    qtde = qtde + 1

print(f'a quantidade foi {qtde - 1}')