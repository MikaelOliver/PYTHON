from random import randint
placar_jogador = 0
placar_computador = 0
while True:
    jogador = input('Escolha PAR ou IMPAR: ').lower()
    numero_jogador = int(input('Escolha o seu número: '))

    numero_computador = randint(0, 10)
    resultado = numero_jogador + numero_computador
    if resultado % 2 == 0:
        if jogador == 'par':
            print(f'Jogador WIN!! com o número: {numero_jogador}')
            placar_jogador = placar_jogador + 1
        else:
            print(f'Computador WIN!!com o número: {numero_computador}')
            placar_computador = placar_computador + 1
    else:
        if jogador == 'impar':
            print(f'Jogador WIN!! com o número: {numero_jogador}')
            placar_jogador = placar_jogador + 1
        else:
            print(f'Computador WIN!! com o número: {numero_computador}')
            placar_computador = placar_computador + 1

    print(f'O placar atual é JOGADOR: {placar_jogador} COMPUTADOR: {placar_computador}')
    saida = input('Digite [S] para Sair: ').upper()
    if saida == 'S':
            if placar_computador > placar_jogador:
                confirma_saida = input('Você está perdendo, tem certeza que vai sair FRANGO. Digite "coco": ').lower()
                if confirma_saida == 'coco':
                    print('Volte Sempre.')
                    break
                else:
                    continue

