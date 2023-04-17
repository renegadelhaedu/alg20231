#lista é uma estrutura de dados
#lista armazena valores dentro dela

'''
desenvolva um programa em python para ler 4 numeros informados pelo usuário
e depois exiba todos os numeros na ordam contraria
'''



nums = [9, 5, 1 ,8]

for i in range(len(nums)):
    for j in range(len(nums)-1):
        if(nums[i] < nums[j]):
            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux

print(nums)


