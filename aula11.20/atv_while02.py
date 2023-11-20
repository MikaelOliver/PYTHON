# MINHA VERSÃO:
while True:
    nome = input('digite o seu nome: ')
    senha = input('digite a sua senha: ')
    if senha == nome:
        print('ERROR senha e nome iguais. Digite Novamente!!')
    elif senha != nome:
        break



# EX PAULO:
tentativas = 1
while tentativas <= 3:
    usuario = input('Informe o seu usuário: ')
    senha = input('Informe o seu usuário: ')
    if senha == usuario:
        print(f'ERROR: essa foi a sua tentativa {tentativas}')
        if tentativas == 3:
            print(f'Suas tentativas acabaram. Tente amanhã')
            break
    else:
        print(f'Acesso liberado!')
        break
    tentativas += 1