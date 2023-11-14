#Alguns cuidados com dados mutáveis.
#Mutaveis = são dados que podem ter seu valor alterado na memoria do dispositivo.
#Imutaveis = são dados que so podem ser copiados da memoria  do dispositivo.

lista = ['joão', 'Paulo']
lista[1] = 'Jose'
print(lista)
nome = 'Paulo'
# nome = 'João'
# nome[2] = 'a'
novo_nome = nome
nome = 'joão'
print(nome)
print(novo_nome)

lista_a = ['João','Paulo']
lista_b = lista_a.copy()
lista_a[1] = 'José'
print(lista_a)
print(lista_b)