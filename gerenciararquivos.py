def salvarArquivo(texto, login):

    f = open(f'produtos_{login}.txt', 'a')
    f.write(texto)
    f.close()


def salvarprodutos():
    lista = []
    lista.append({'nome': 'lapis', 'valor': 14, 'qtde': 5})
    lista.append({'nome': 'cpu', 'valor': 2000, 'qtde': 2})

    for p in lista:
        nome = p['nome']
        valor = p['valor']
        qtde = p['qtde']

        texto = f'nome do produto: {nome}\n'
        texto = texto + f'valor do produto: {valor}\n'
        texto = texto + f'qtde do produto: {qtde}\n\n'

        salvarArquivo(texto, 'rene')


def lerarquivo():
    f = open('produtos_rene.txt', 'r')

    for linha in f.readlines():
        print(linha, end='')

    f.close()
