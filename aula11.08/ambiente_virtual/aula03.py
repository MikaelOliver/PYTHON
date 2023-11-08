#Operadores IN e NOT IN

nome = "Paulo"
print('au' in nome)

print('='*20)

seu_nome = input("Informe seu nome: ")
buscar = input('informe o valor a ser encontradado: ')

if(buscar in seu_nome):
    print(f'{buscar} está condido em {seu_nome}')
else:
    print(f'{buscar} NÃO está condido em {seu_nome}')

print('='*20)

nao_nome = "Joãozinho"
print('au' not in nao_nome)