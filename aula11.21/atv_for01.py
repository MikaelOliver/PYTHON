for i in range(1001):
    print(i)
    if i % 100 == 0:
        print('chegou no multiplo de 100')


lista = []
for interio in range(10):
    interio = int(input('Digite um numero interio: '))
    lista.append(interio)
print(len(lista[0::2]))
print(len(lista[1::2]))