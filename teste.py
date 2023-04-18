funcs = [['samuel dantas', 20, 9999], ['pedro',21, 11111],['carla',34, 88]]

buscado = input('digite o nome de quem voce procura')
achei = False
for list_indv in funcs:
    if (list_indv[0].find(buscado) >= 0):
        print(list_indv[0])
