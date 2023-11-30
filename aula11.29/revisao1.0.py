# variavel = 1

# print(variavel)

# variavel = 'Paulo'

# print(variavel)

# # regra do fatiamento [i, f , s]

# print(variavel[2:4])



nome = input('nome: ')
tamanho = len(nome)
if tamanho %2 == 0:
    meio = int(tamanho / 2) - 1
    meio2 = int(tamanho/ 2)
    print(nome[meio],nome[meio2])
else:
    meio3 = int(tamanho/2)
    print(nome[meio3])


# def letra_do_meio(palavra):
#     tamanho = len(palavra)
    
#     if tamanho % 2 == 0:
#         # Se a palavra tem um número par de letras, imprime as duas letras do meio
#         meio1 = int(tamanho / 2) - 1
#         meio2 = int(tamanho / 2)
#         print("Letras do meio:", palavra[meio1], palavra[meio2])
#     else:
#         # Se a palavra tem um número ímpar de letras, imprime a letra do meio
#         meio = int(tamanho / 2)
#         print("Letra do meio:", palavra[meio])

# # Recebe a palavra do usuário
# palavra = input("Digite uma palavra: ")

# # Chama a função para imprimir a letra do meio
# letra_do_meio(palavra)]




#utilizando fatiamento e repetição, imprima uma lista de A até o E removendo uma letra de cada vez
# letras = ['a','b','c','d','e']
# for i in range(len(letras)):
#     letras_removida = letras[:i+1]
#     print(letras_removida)

# lista = ['a','b','c','d','e']
# len_da_lista = len(lista)

# for i in range(len_da_lista):
#     print(i)
letras = ['a','b','c','d','e'] # 
len_letras = len(letras)
for i in range(len(letras)):
    lista = letras[:5-i]
    print(lista)
    

    

