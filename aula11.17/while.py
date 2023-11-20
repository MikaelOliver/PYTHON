#while = enquanto.

#loop infinito - quando uma estrutura de repetição não tem fim.
# while True:

contador = 0
while contador < 30:
    print(contador)
    contador += 1 # mesma coisa que: contador = contador +1

    if contador == 12:
        print('cheguei no 12')
    if contador == 20:
        break

print('Saiu do while')