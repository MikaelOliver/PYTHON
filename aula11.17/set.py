# set - conjuntos

set01 = set('Paulo')
# set02 = set(2) INTEIROS NÃO SÃO INTERAVEIS
set02 = {'Paulo', 'Junior', 'Lara', 'kaynan', 'Felipe'}
print(set01)
print(set02)

lista = [1,2,3,4,5,5,5,5,5,5,5]
print(lista)
set03 = set(lista)
print(set03)
print(7 in set03)
print(5 in set03)
print(7 not in set03)
print(5 not in set03)
# lista1 = set03
# print(lista1)
for i in set03:
    print(i)
set03.add('Paulo')
set03.add(1)
set03.add(6)
set03.update('Paulo')
set03.discard('Paulo')
set03.discard('P')
set03.clear()
print(set03)

set04 = {1,2,3,4,5}
set05 = {4,5,6,7,8}

set06 = set04 | set05 # UNIÃO DE CONJUNTOS
print(set06)

set06 = set04 & set05 # INTERCESSÃO DE CONJUNTOS
print(set06)

set07 = set04 - set05 # DIFF DE CONJUNTO
set06 = set05 - set04 # DIFF DE CONJUNTO
print(set07)
print(set06)