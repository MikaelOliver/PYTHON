#possuem CHAVE(KEYS) e VALOR(VALUES)
# parametro: {} ou dict{}


pessoa = { 'nome':'Paulo',
          'sobrenome 1':'junior',
          'sobrenome 2':'junior',
          'sobrenome 3':'junior',
          'sobrenome 4':'junior'}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

k = pessoa.keys()
v = pessoa.values()

for chave in k:
    print(chave)
print('='*20)
for valor in v:
    print(valor)
print('='*20)

for chave in pessoa:
    print(chave)
print('='*20)


for chave, valor in pessoa.items():
    print(f'a chave é: {chave.upper()} e esse o valor dela: { valor.upper()}')

print('='*20)

print(pessoa['sobrenome 4'])

print('='*20)

d1 = {'valor1': 100,
      'valor2': 200,
      'valor3': 300, }
d2 = d1.copy()
print(d1)
d2['valor2'] = 'jefferson'
print(d1)
print(d2)
print(type(d2))

d3 = d1.pop('valor3')
print(d1)




outro_nome = {'valor5': 5,
               'valor6': 6}

d1.update(outro_nome)

print(d1)
d4 = d1.has_key('valor5')
print(d4)