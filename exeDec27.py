qtdeMor = float(input('digite o kg do morango'))
qtdeMac = float(input('digite o kg da maca'))
valor = 0
if(qtdeMor <= 5):
    valor = valor + qtdeMor * 2.5
else:
    valor = valor + qtdeMor * 2.2

if(qtdeMac <= 5):
    valor = valor + qtdeMac * 1.8
else:
    valor = valor + qtdeMac * 1.5

if(qtdeMor + qtdeMac > 8 or valor > 25):
    valor = valor * 0.9
    print('vc ganhou um desconto de 10%')

print(f'o valor total pago foi de {valor} reais')


