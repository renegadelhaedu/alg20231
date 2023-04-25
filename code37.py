alunos = dict()

nome = 'lkjsadj'
while(nome != 'sair'):
    nome = input('digite o nome do aluno')

    if(not nome == 'sair'):
        idade = int(input('digite sua idade'))
        alunos[nome] = idade

    print(alunos)

print('\n-----Nome-----')
for chave in alunos:
    if(alunos[chave] > 25):
        print(chave)