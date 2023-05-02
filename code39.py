pessoas = {'234':['rene', 34, 3] , '9887':['maria', 22, 8]}
#cada pessoa tem nome, cpf, idade, nota
op = 999

while(op != 0):

    print('\n1-cadastrar pessoa')
    print('2-listar pessoas')
    print('3-exibir a média de idade das pessoas')
    print('4-buscar uma pessoa pelo CPF')

    op = int(input('digite a opcao desejada '))

    if(op == 1):
        nome = input('digite seu nome ')
        cpf = input('digite seu CPF ')
        idade = int(input('digite sua idade '))
        nota = float(input('digite sua nota media '))
        #antes de add uma pessoa, verifique se o cpf já está cadastrado
        pessoas[cpf] = [nome, idade, nota]

    elif(op == 2):
        print(f'\n\nNome - idade - nota')
        print('---------------------')
        for cpf in pessoas:
            lista = pessoas[cpf]
            print(f'{lista[0]} - {lista[1]} - {lista[2]}')

    elif(op == 3):
        soma = 0
        for cpf in pessoas:
            lista = pessoas[cpf]
            soma = soma + lista[1]

        media = soma / len(pessoas)
        print(f'a media de idades foi {media} anos')

    elif(op == 4):
        cpf = input('digite o cpf para realizar a busca ')
        #terminar a busca