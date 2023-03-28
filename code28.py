'''
desenvolva um programa em python para ler as 3 notas dos alunos
da sala e calcule a média
'''

soma = 0

for i in range(0, 70):
    nota = float(input('digite a nota do aluno'))
    soma = soma + nota

media = soma / 70

print(f'a media foi {media}')