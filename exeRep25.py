n = int(input('digite a quantidade de pessoas'))
soma = 0

for i in range(n):
    idade = int(input('digite sua idade'))

    soma += idade # ou soma = soma + idade

media = soma / n

if(media <= 25):
    print('essa galera e jovem')
elif(media <= 60):
    print('esse povo e adulto')
else:
    print('esses senhores sao idosos')
