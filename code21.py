import math
from matplotlib import pyplot as plt
x=1
maiorY = 0
maiorX = 1
vals = list()
while(x < 500):

    y = math.sin(math.pi * x)
    if(y > maiorY):
        maiorX = x
        maiorY = y
    vals.append(y)
    x=x+1

print(f'o maior X: {maiorX} e gerou um Y de {maiorY}' )
plt.plot(vals)
plt.show()