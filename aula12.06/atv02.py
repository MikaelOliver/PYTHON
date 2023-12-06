marca = input('Informe a MARCA do seu carro: ')
modelo = input('Informe a MODELO do seu carro: ')


lista_carros = []
lista_carros.append(marca)
lista_carros.append(modelo)

dic_carros = {}
dic_carros.update([lista_carros])
print(dic_carros)