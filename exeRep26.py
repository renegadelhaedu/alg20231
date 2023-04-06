
qtde = int(input('digite a quantidade de eleitores'))

cand1 = 0
cand2 = 0
cand3 = 0

for i in range(qtde):
    voto = int(input('digite 1, 2 ou 3 para votar no seu candidato'))

    while(voto < 1 or voto > 3):
        voto = int(input('ERRO. digite 1, 2 ou 3 para votar no seu candidato'))

    if(voto == 1):
        cand1 += 1 #ou cand1 = cand1 + 1
    elif(voto == 2):
        cand2 += 1
    elif(voto == 3):
        cand3 += 1

print(f'candidato 1 obteve {cand1} votos')
print(f'candidato 2 obteve {cand2} votos')
print(f'candidato 3 obteve {cand3} votos')

if(cand1 > cand2 and cand1 > cand3):
    print('o candidato 1 foi o vencedor')
elif(cand2 > cand1 and cand2 > cand3):
    print('o candidato 2 foi o vencedor')
elif(cand3 > cand1 and cand3 > cand2):
    print('o candidato 3 foi o vencedor')
else:
    print('foi marmelada')