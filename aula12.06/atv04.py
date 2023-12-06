# criar um siste de login e senha. crie um dicionario contendo os acessor dos colaboradores com nome de usuario e senha, em seguida peça as infromações valide o login do usuario

user = input('informe seu usuario: ').lower()
user_password = input('inform sua senha: ')
colaboradores = {'mikael': '12345',
                 'jerfferson': '23453',
}

for usuario, senha in colaboradores.items():
    if usuario == user and senha == user_password:
        print('ACESSO LIBERADO!!')
        break
    else:
        print('Infome uma senha e usuario correto!!')
        break

# if user in colaboradores.keys() and user_password in colaboradores.values():
#     # if colaboradores.get(user) == colaboradores.keys():
#     print('ACESSO LIBERADO!')
# else:
#     print('INFORME UM USUARIO E SENHA DE UM COLABORADOR')