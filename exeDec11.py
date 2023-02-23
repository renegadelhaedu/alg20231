salario = float(input('digite o seu salario'))

if(salario <= 280):
    final = salario * 1.2
    perc = 20
elif(salario <= 700):
    final = salario * 1.15
    perc = 15
elif (salario <= 1500):
    final = salario * 1.1
    perc = 10
else:
    final = salario * 1.05
    perc = 5

print(f'voce recebia {salario} e agora recebera {final}')
print(f'seu aumento foi de {perc}%')
print(f'voce ganhou no salario um aumento de {final - salario}')


