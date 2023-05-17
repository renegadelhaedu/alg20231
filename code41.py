#CRIANDO FUNÇÕES

def decorar():
    print(15*'-')
    print('MENU')
    print(15*'-')

def enfeitarNome(texto):
    print(15*'-')
    print(texto)
    print(15*'-')

def teste():
    return 'meu erro'

def calcularIMC(altura, peso):
    imc = peso/(altura**2)
    return imc

print(enfeitarNome(calcularIMC(2,99)))

soma = 0
for i in range(1):
    alt = float(input('digite sua altura'))
    pe = float(input('digite seu peso'))
    soma += calcularIMC(alt, pe)

media = soma/1
print(enfeitarNome(f'a media de IMC das pessoas foi {media}'))