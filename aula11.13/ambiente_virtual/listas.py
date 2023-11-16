# uma lista é representada pelos []
# len - metodo que retorna a quantidade de itens de uma lista - OBS: todo metodo, por obrigação retorna algum valor.
# append -ele coloca os valores no fim do lista
#del - remove item especifico da lista
#remove - remove um objeto especifico da lista
#pop - remove o ultimo objeto da lista
#insert - adiciona um objeto em qualquer lugar da lista
#copy - copiar uma lista mudando o endereço
lista = []
lista = ['back']
lista.append('front') 
print(lista, type(lista))
print(len(lista))
lista.append('data')
print(lista, type(lista))

lista = ['back','tarde',21, True, 8.8]
print(f'a quantidade de alunos na turma é:{lista[2]}')

lista[2] = 22
print(lista)

lista[1] = False
print(lista)

lista[1] = ['neyva','alice','lara','paula', 'geisa']
print(lista)
print(lista[1][2])

print(lista[-2])
del lista[-2]
print(lista[-2])
print(lista)

lista.remove('back')
print(lista)

lista.insert(0,'Amontada Valley')
print(lista)
lista.insert(2,'professor')
print(lista)
