#faça um programa que declare continua, e execurt um laço while, enquanto a variavel continue for igual a "s" dentro o while o ususuario deve digitar um numero e o programa deve imprimir o dobro do numero digitado. e apos essa impressão pergunte ao usuario se quer parar ou não, caso pressione N o laço deve parar.

continua = 's'
while continua == 's':
    numero = int(input('Digite um numero: '))
    print(numero*2)

    parar = input('"n" para parar "s" para seguir ')
    if continua != parar:
        continua=parar