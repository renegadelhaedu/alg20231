#CRIANDO FUNÇÕES

def decorar():
    print(15*'-')
    print('MENU')
    print(15*'-')

def decorarDyn(texto):
    print(15*'-')
    print(texto)
    print(15*'-')

def teste():
    return 'meu erro'

def calcularIMC(altura, peso):
    imc = peso/(altura**2)
    return imc

