p1 = input('telefonou para a vitima?')
p2 = input('esteve no local do crime?')
p3 = input('mora perto da vitima?')
p4 = input('devia para a vitima?')
p5 = input('ja trabalhou com a vitima?')

soma = 0

if(p1 == 'sim'):
    soma = soma + 1
if(p2 == 'sim'):
    soma = soma + 1
if(p3 == 'sim'):
    soma = soma + 1
if(p4 == 'sim'):
    soma = soma + 1
if(p5 == 'sim'):
    soma = soma + 1

if(soma <= 1):
    print('inocente')
elif(soma == 2 ):
    print('suspeito')
elif(soma <= 4 ):
    print('cumplice')
elif(soma == 5):
    print('assassino. ligue para PEDRO vir prender')







