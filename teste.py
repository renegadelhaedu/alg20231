texto = 'eu estou com vontade de comer'
criptografado = []
for i in texto:
    new = ord(i) + 4
    criptografado.append(chr(new) )

print(*criptografado)

descripto = []
for i in criptografado:
    new = ord(i) - 4
    descripto.append(chr(new) )

print(*descripto)