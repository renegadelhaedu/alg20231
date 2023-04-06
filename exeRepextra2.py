'''desenvolva um programa para descobrir quantos mandatos presidenciais
foram exercidos ate que o brasil ultrapasse 300 MI de habitantes.
dados:
1.2% de crescimento populacional ao ano
230 MI de pop atual

by Shelldon Ryan
'''

population = 230
taxacresc = 1.012
ano = 2023

while (population <= 300):
    ano += 1
    population *= taxacresc

quantidadeDeAnos = ano - 2023
mandatos = quantidadeDeAnos // 4


print(f'Se passaram {quantidadeDeAnos} anos.')
print(f'Foram  {mandatos} mandatos.')
