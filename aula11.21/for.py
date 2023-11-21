# trabalha com iteraveis.
# tem que possuir uma variavel de controle.
# iter() - transfomar um objeto em iteravel
# next() - função para imprimir os iteraveis de uma 'lista'

#enumerate() - é um iterador de indices e valores.
# nome = 'paulo'
# letra = iter(nome)
# print(next(letra))
# print(next(letra))
# print(next(letra))
# print(next(letra))
# print(letra)
# for letra in nome:
#     print(letra)

lista_nomes = [ 'João', 'Pedro', 'Mateus', 'Judas', 'Tiago' ]
print(lista_nomes)
for i in enumerate(lista_nomes):
    print(i) 