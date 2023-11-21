for i in range(1001):
    print(i)
    if i % 100 == 0:
        print('chegou no multiplo de 100')


lista = []
for interio in range(20):
    interio = int(input('Digite um numero interio: '))
    lista.append(interio)
print(lista[0::2])
print(lista[1::2])