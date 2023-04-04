base = int(input('digite a base'))
exp = int(input('digite o expoente'))

result = 1
for i in range(exp):
    
    result = result * base

print(f'o resultado foi {result}')

