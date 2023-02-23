salario = float(input('digite o seu salario'))

if(salario <= 280):
    perc = 20
elif(salario <= 700):
    perc = 15
elif (salario <= 1500):
    perc = 10
else:
    perc = 5

final = salario * (1 + perc/100)
print(f'voce recebia {salario} e agora recebera {final}')
print(f'seu aumento foi de {perc}%')
print(f'voce ganhou no salario um aumento de {final - salario}')


