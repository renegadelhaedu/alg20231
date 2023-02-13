#estrutura de decisão
   #simples
   #encadeadas

idade = int(input('digite sua idade'))
if(idade >= 18):
    tempo = idade - 18
    print('pode vender bebida')
    print(f'ele(a) ja pode comprar bebida ha {tempo} ano(s)')
else:
    tempo = 18 - idade
    print(f'NAO pode vender bebida e deve esperar {tempo} ano(s)')

