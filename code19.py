nota = int(input('digite o valor da nota dada'))
troco = nota - 12

print(troco)
qtdeNota5 = troco // 5
restoNota5 = troco % 5
qtdeNota2 = restoNota5 // 2
restoMoedas = qtdeNota2 % 2

print(f'o troco sera em {qtdeNota5} notas de R$5, {qtdeNota2} notas de R$2, {restoMoedas} de moedas')