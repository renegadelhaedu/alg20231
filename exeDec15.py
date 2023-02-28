l1 = int(input('digite o valor do lado'))
l2 = int(input('digite o valor do lado'))
l3 = int(input('digite o valor do lado'))

if(l1 == l2 and l2 == l3):
    print('esse triangulo e equilatero')
elif(l1 != l2 and l2 != l3 and l1 != l3):
    print('esse triangulo e escaleno')
elif((l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or
(l2 == l3 and l3 != l1)):
    print('isosceles')

else:
    print('tem algo de mt errado')