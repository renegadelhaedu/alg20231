opcoes = ['s','c','v','d']
sexos = ['f','m']
nome = input('digite seu nome')
idade = int(input('digite sua idade'))
salario = float(input('digite seu salario'))
sexo = input('digite seu sexo')
estciv = input('digite seu estado civil')

while (len(nome) <= 3 or idade < 0 or idade > 150 or salario <= 0
       or sexo not in sexos or estciv not in opcoes):
    nome = input('digite seu nome novamente')
    idade = int(input('digite sua idade novamente'))
    salario = float(input('digite seu salario novamente'))
    sexo = input('digite seu sexo novamente')
    estciv = input('digite seu estado civil novamente')
