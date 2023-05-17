produtos = [{'nome': 'carro', 'cod': '345', 'preco': 65432.0},
            {'nome': 'carroça', 'cod': '123', 'preco': 34567.0}]


def enfeitar(texto):
    print(10 * '-')
    print(texto)
    print(10 * '-')


def buscarProduto():
    busca = input('digite o nome do produto')
    achou = False
    for p in produtos:
        if (p['nome'].find(busca) >= 0):
            enfeitar(p['cod'] + ' - ' + p['nome'])
            achou = True
    if (not achou):
        print('nao foi encontrado nenhum produto')


def buscarCod(lista):
    cod = input('digite o codigo do produto escolhido')
    for i in range(len(lista)):
        if (lista[i]['cod'] == cod):
            return i
    return -1


op = -1
while (op != 0):
    print('1-cadastrar produto')
    print('2-buscar produto')
    print('3-atualizar produto')
    print('4-remover produto')

    op = int(input('digite  a opcao'))

    if (op == 1):
        nome = input('digite o nome')
        cod = input('digite o cod do produto')
        preco = float(input('digite o preco do produto'))

        produtos.append({'nome': nome, 'cod': cod, 'preco': preco})

    elif (op == 2):
        buscarProduto()

    elif (op == 3):
        buscarProduto()

        ind = buscarCod(produtos)
        if (ind >= 0):
            novo_nome = input('atualize o nome')
            novo_preco = float(input('atualize o preço'))
            produtos[ind]['nome'] = novo_nome
            produtos[ind]['preco'] = novo_preco

            enfeitar('produto atualizado com sucesso!')
        else:
            enfeitar('Nao foi possivel achar o produto')

    elif (op == 4):
        buscarProduto()

        ind = buscarCod(produtos)
        if (ind >= 0):
            produtos.pop(ind)
            enfeitar('produto removido com sucesso!')
        else:
            enfeitar('Nao foi possivel achar o produto')



