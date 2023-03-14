login = input('digite o login ')
senha = input('digite a senha ')

while(login != 'catolica' or senha != 'ccpb'):
    print('login ou senha incorreta')
    login = input('digite o login novamente ')
    senha = input('digite a senha novamente ')

print('Login feito com sucesso!!!')
