# Listas são um conjuto de elementos/dados.
# extend - server pra unir duas listas.
lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9,10]

# o sinal de + ele  soma numeros e concatena strings.
a = 2
b = 3
print(a + b)

c = "Amo"
d = 'valley'
print(c+d)
lista_c = lista_a + lista_b
print(lista_c, type(lista_c))

#forma errada
lista_d = lista_a.extend(lista_b)
print(lista_d)

#forma certa
lista_a.extend(lista_b)
print(lista_a)