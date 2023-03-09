pago = float(input('digite o valor pago pelo cliente'))
preco = float(input('digite o preco do produto'))

troco = preco - pago

if(troco < 0):
    print('o valor pago eh insuficiente')
elif(troco == 0):
    print('nao tem troco para ser dado')
else:
    print('Troco:')
    if(troco >= 100):
        qtdenotas100 = troco // 100
        troco = troco % 100
        print(f'notas de 100: {qtdenotas100}')
    if(troco >= 50):
        qtdenotas50 = troco // 50
        troco = troco % 50
        print(f'notas de 50: {qtdenotas50}')
    if(troco >= 20):
        qtdenotas20 = troco // 20
        troco = troco % 20
        print(f'notas de 20: {qtdenotas20}')
    if(troco >= 10):
        qtdenotas10 = troco // 10
        troco = troco % 10
        print(f'notas de 10: {qtdenotas10}')
    if(troco >= 5):
        qtdenotas5 = troco // 5
        troco = troco % 5
        print(f'notas de 5: {qtdenotas5}')

