'''faça um programa em python que leia o nome, idade e salario
dos funcionários de uma empresa e armazene todos em uma lista.
Cada funcionário será uma lista.
A quantidade de funcionários é incerta.
Use um menu dentro de um while com duas funcionalidades: cadastrar e buscar

'''
funcs = list()
op= 99
while(op != 0):
    print('---------MENU----------')
    print('1-cadastrar')
    print('2-buscar')
    print('3-listar')
    print('0-sair')
    op = int(input('digite a opcao desejada'))

    if(op == 1):
        indiv = list()
        nome = input('digite seu nome')
        idade = int(input('digite sua idade'))
        salario = float(input('digite seu salario'))

        indiv.append(nome)
        indiv.append(idade)
        indiv.append(salario)
        funcs.append(indiv)

        print('Funcionario cadastrado com sucesso \n')

    elif(op == 2):
        buscado = input('digite o nome de quem voce procura')

        for list_indv in funcs:

            if (list_indv[0].find(buscado) >= 0):
                print(list_indv[0])
                achei = True

        if (not achei):
            print('nao foi encontrado ninguem com esse nome')

    elif(op == 3):
        for indv in funcs:
            print(indv[0])