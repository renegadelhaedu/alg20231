'''
sabendo que a india possui 1,5BI hab e cresce 1,2% ao ano, em qual
ano a india ultrapassará 2Bi hab?
'''

ano = 2023
hab = 1.5

while(hab <= 2):
    ano = ano + 1
    hab = hab * 1.012
    print(f'O tamanho da população e {hab:.2f} Bi no ano {ano}')