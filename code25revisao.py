'''
o salario dos funcionarios de uma empresa é regimentado por um plano de cargos e salarios.
o plano é baseado num crescimento horizontal do colaborador e usa a quantidade de meses na empresa
e é modelado pela seguinte função:
salario = qtdeMeses X 130 + 2000 + 10^nivelTitulo
'''

mesAtual = int(input('digite o mes de hoje'))
anoAtual = int(input('digite o ano de hoje'))

mesAdmissao = int(input('digite o mes de admissao'))
anoAdmissao = int(input('digite o ano de asmissao'))

titulo = input('digite a titulação - graduado/especialista/mestre/doutor')

qtdeMeses = (anoAtual - anoAdmissao) * 12 + (mesAtual - mesAdmissao)


if (titulo == 'graduado'):
    fator = 1
elif(titulo == 'especialista'):
    fator = 2
elif(titulo == 'mestre'):
    fator = 3
elif(titulo == 'doutor'):
    fator = 4
else:
    fator = 0

salario = qtdeMeses * 130 + 2000 + 10 ** fator

print(salario)