menor = 999
for i in range(10):
    peso = float(input('informe o peso'))
    alt = float(input('informe a altura'))

    imc = peso / (alt**2)
    if(imc < menor):
        menor = imc

    print(f'o imc foi {imc}')
    if(imc > 30):
        print('procure um medico')
    else:
        print('vc esta saudavel')
print(f'o menor imc encontrado foi {menor}')
