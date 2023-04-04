f0 = 0
f1 = 1

n = int(input('qual numero da serie vc quer?'))

for i in range(n):
    fn = f0 + f1
    f0 = f1
    f1 = fn
    print(fn, end=' ')

