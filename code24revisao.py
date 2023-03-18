#premio da mega: só ganha quem tiver o nome com uma quantidade letras maior que 5,
#a quantidade de letras tem que ser múltiplo de 5

nome = input('digite seu nome')

qtdeLetras = len(nome)

if(qtdeLetras > 5 and qtdeLetras % 5 == 0):
    print('VOCE GANHOU NA MEGA')
else:
    print('tente outra vez')

