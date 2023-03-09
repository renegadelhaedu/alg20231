dia = int(input('digite o dia'))
mes = int(input('digite o mes'))
ano = int(input('digite o ano'))

if(dia >= 1 and dia <= 31):
    if(mes >= 1 and mes <= 12):
        if(ano >0 and ano <= 2023):
            print('data valida')
'''
            
if(dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano >0 and ano <= 2023):
    print('data valida')
else:
    print('data INvalida')
'''