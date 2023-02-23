salario = float(input('digite seu salario'))

if(salario <= 2300):
    print('vc e isento')
elif(salario <= 3400):
    print(salario * 0.85)
elif(salario <= 4100):
    print(salario * 0.8)
elif (salario <= 5000):
    print(salario * 0.78)
else:
    print(salario * 0.73)

