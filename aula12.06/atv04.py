# criar um siste de login e senha. crie um dicionario contendo os acessor dos colaboradores com nome de usuario e senha, em seguida peça as infromações valide o login do usuario
#MIKAEL VERSION
user = input('informe seu usuario: ').lower()
user_password = input('inform sua senha: ')
colaboradores = {'mikael': '12345',
                 'ze': '23453',
}

for usuario, senha in colaboradores.items():
    if usuario == user and senha == user_password:
        print('ACESSO LIBERADO!!')
        break
else:
    print('Infome uma senha e usuario correto!!')


#PAULO VERSION

# dic_acessos = {
#     'paulo':'123456',
#     'joao':'121212'
#                }

# usuario_senha = {}
# usuario = input('Informe seu USUARIO:')
# senha = input('Informe sua SENHA:')

# usuario_senha[usuario] = senha

# for chave in dic_acessos.keys():
#     if chave == usuario:
#         if dic_acessos[chave] == usuario_senha[usuario]:
#             print('ACESSO LIBERADO!!')
#             break
#         else:
#             print('SENHA INCORRETA')
#             break        

        
