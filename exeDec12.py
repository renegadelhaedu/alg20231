horas = float(input("Digite a quantidade de horas: "))
valor_hora = float(input("Digite o valor de sua hora: "))
sb = horas * valor_hora

if(sb <= 900):
	ir = 0
elif(sb <= 1500):
	ir = sb * 0.05
elif(sb <= 2500):
	ir = sb * 0.1
else:
	ir = sb * 0.2

inss = sb * 0.1
fgts = sb * 0.11
sind = sb * 0.03
sl = sb - (ir + inss + sind)

print(f'restou apenas R${sl} de RS{sb}')
print(f'IRRF:{ir} \ninss:{inss} \nfgts:{fgts} \nsindicato:{sind}')
