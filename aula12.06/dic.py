dic = {'nome':'Paulo'}
dic2 = dict(nome='mikael')

dic['nome']
reading = dic2.get('nome')

dic.update(sombrenome='Junior')
dic.update({'nome': 'mikael'})
print(dic)
print(reading)
print(dic)
print(dic2)
tupla = ('peso',72.12), #quando adicionar uma tupla, para voce adcionar no dicionario precisa de uma ","
lista = ['data','13/04/1996'],['numeros',[1,2,3,4,5,6,7,8]]
dic.update(tupla) 
dic.update(lista) 

print(dic)

dic.clear()
print(dic   )
