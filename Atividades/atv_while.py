# faça a soma de dois numero e diga se de uma opção de stop.
while True:
    stop = input('digite"S" para parar: ')
    number1 = int(input('Digite o primeiro numero'))
    number2 = int(input('Digite o primeiro numero'))
    print(number1+number2)
    if stop == 's' or stop == 'S':
        break


