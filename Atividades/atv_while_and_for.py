# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input('Digite a sua nota: '))

    if nota < 0 or nota > 10:
        print('Nota invalida!!!')
        break
    else:
        print(f'A sua nota é {nota}')
