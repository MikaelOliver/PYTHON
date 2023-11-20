contador = 0
lista = []
while contador < 5:
    n1 = float(input('Informe um número: '))
    lista.append(n1)
    contador += 1
print(lista)
print(f'o maior número é: {max(lista)}') # max() mostra o maior numero da lista.
