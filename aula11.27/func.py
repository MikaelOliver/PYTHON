def argumentos(numeros):

    if numeros >= 0:
        return 'P'
    if numeros < 0:
        return 'N'
 
number = int(input('Digite um numero: '))
print(argumentos(number))