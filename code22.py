x = 1
maiorX = 1
while(x <= 500):
    y = 2*x + 3*x
    print(y)
    if(y <= 1000):
        maiorX = x
    x = x+1

print(f'o maior x eh {maiorX}')