login = input('digite o login do usuario')
senha = input('digite a senha do usuario')

while(login == senha):
    print('ERRO!!!')
    login = input('digite o login do usuario novamente')
    senha = input('digite a senha do usuario novamente')

print('agora voce acertou!!!')
