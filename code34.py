lista_nomes = ['pedro','maria','joao','catia','erica','margarida']

busca = input('digite o nome da pessoa que voce procura')
achei = False
for nome in lista_nomes:
    print(nome.find(busca))
    if(nome.find(busca) >= 0):
        print(nome)
        achei = True

if(not achei):
    print('nao foi encontrado ninguem com esse nome')


