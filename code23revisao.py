#determine o valor do juros final pago pelo produto e o valor do produto com juros, sendo que o valor inicial
#do juros começa em 9% quando dividido em 2x. Ao aumentar cada parcela incrementa-se 15%
#em juros da parcela anterior
parcelas = int(input('digite a quantidade de parcelas'))
valorProduto = float(input('digite o valor do produto'))

j1 = 0 #credito a vista
j2 = 9/100
j3 = j2 * 1.15 # ou j2 + (0.15 * j2)
j4 = j3 * 1.15
j5 = j4 * 1.15

if(parcelas == 1):
    jurosFinal = j1
elif(parcelas == 2):
    jurosFinal = j2
elif(parcelas == 3):
    jurosFinal = j3
elif(parcelas == 4):
    jurosFinal = j4
elif(parcelas == 5):
    jurosFinal = j5
else:
    print('quantidade de parcelas invalida')

if(parcelas >= 1 and parcelas <=5):

    valorFinal = valorProduto * (1 + jurosFinal)
    print(f'valor final do produto:R${valorFinal:.2f} em {parcelas} vezes no cartao')
    print(f'voce pagou de juros {jurosFinal * 100:.2f}%')