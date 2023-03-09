num = int(input('digite um numero menor que 1000'))

qtdeCent = num // 100
resto = num % 100
qtdeDez = resto // 10
unidades = resto % 10

print(f'{qtdeCent} centenas, {qtdeDez} dezenas e {unidades} unidades')