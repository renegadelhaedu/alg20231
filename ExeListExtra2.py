'''faça um programa em python que leia o nome, idade e salario
dos funcionários de uma empresa e armazene todos em uma lista.
Cada funcionário será uma lista.
A quantidade de funcionários é incerta.
Use um menu dentro de um while com duas funcionalidades: cadastrar e buscar
'''
pessoas = []

op = 99
while(op != 0):
    print('\n\n--------MENU----------\n')
    print('1-cadastrar pessoa')
    print('2-listar pessoas')
    print('0-sair')

    op = int(input('digite a opcao desejada'))

    if(op == 1):
        nome = input('digite seu nome')
        idade = int(input('digite sua idade'))
        sal = float(input('digite seu salario'))

        pessoas.append([nome, idade, sal])

        print('Cadastro feito com sucesso!')

    elif(op == 2):
        print('\nNome - idade - salario')
        for p in pessoas:
            print(f'{p[0]} - {p[1]} - {p[2]}')
