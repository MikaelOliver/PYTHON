numero = int(input('Digite um numero: '))
intervalo = range(1, numero+1,)
contador = 0
for i in intervalo:
    if numero % i == 0:
        print(f'Foi divisivel por {i} ')
        contador +=1
if contador == 2 or contador == 1:
    print(f'O número {numero} é primo')