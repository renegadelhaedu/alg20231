import random
lista = list()
par = list()
impar = list()

for i in range(20):
    #valor = int(input('digite  um numero inteiro'))
    #lista.append(valor)
    lista.append(random.randint(1,99))

for x in lista:
    if(x % 2 == 0):
        par.append(x)
    else:
        impar.append(x)

print(lista)
print(par)
print(impar)