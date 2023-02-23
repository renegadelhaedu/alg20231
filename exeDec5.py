n1 = float(input('digite sua primeira nota'))
n2 = float(input('digite sua segunda nota'))

media = (n1 + n2) / 2

if(media == 10):
    print('aprovado com distincao')
elif(media >= 7):
    print('aprovado')
else:
    print('reprovado e tente novamente. voce vai conseguir')