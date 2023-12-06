# Crie uma lista de alunos com nome e nota final de cada aluno e coloce em um dicionario, depois imprima
lista = [['Pedro',5.5],['joão',7],['Henrique',10]]
dic = {}
dic.update(lista)
print(dic)
#inserio mais 04 alunos e notas no seu dicionario.
dic.update({'Guilherme': 7})
dic.update({'Mateus': 8})
dic.update({'Artur': 9})
dic.update({'Antonio': 1})
print(dic)
dic_ordenado = sorted(dic.items())
print(dic_ordenado)