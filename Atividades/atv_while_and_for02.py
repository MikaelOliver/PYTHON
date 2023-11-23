# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
tentativas = 0
while tentativas<= 3:
    user_name = input('Digite o seu usúario: ')
    user_password = input('Digite a sua senha: ')
    if user_name == user_password:
        print('ERROR senha e usúario iguais.')
        if tentativas == 3:
            print('TENTE NOVAMENTE AMANHÃ!')
            break
    else:
        print('BEM VINDO!!!')
        break
    tentativas = tentativas + 1