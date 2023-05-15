lista = list() #ordem #armazena Itens  #index #mutavel
tupla = tuple() #ordem #armazena Itens #index #Imutavel
dicionario = dict() #desordem #chave valor #valor mutavel

conjunto = set()
conjunto2 = {"rene", "zezinho", "pedro", "erica", 'erica'}

busca = input('digite o nome para buscar')
for nome in conjunto2:
    if(nome == busca):
        conjunto2.remove(nome)
        print('a pessoa foi deletada')
        break

print(conjunto2)
