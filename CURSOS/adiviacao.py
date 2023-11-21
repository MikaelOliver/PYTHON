import random
def jogar():

    print('='*32)
    print('Bem vindo ao jogo de adiviação!')
    print('='*32)

    num_scret= random.randrange(1, 101)
    total_tentativas = 0
    pontos = 100


    print('Qual o nível de dificuldad? ')
    print('(1) Fácil (2) Médio (3) Difícil')


    nivel = int(input('Defina um nível: '))
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5



    for rodadas in range(1, total_tentativas +1):
        print(f'Tentativas {rodadas} de {total_tentativas}')
        chute = int(input('Digite um número entre 1 e 100: '))
    
        print(f'O seu numero é:{chute}')
        if(chute< 1 or chute>100):
            print("Você deve digitar um número entre 1 e 100")
            continue
        if(num_scret==chute):
            print(f'você acertou!! E fez {pontos} pontos')
            break
        else:
            if(num_scret < chute):
                print('Você fez um chute maior do que o numero secreto')
            elif(num_scret >   chute):
                print('Você fez um chute menor do que o numero secreto')
            pontos_perdidos = abs(num_scret - chute)
            pontos = pontos - pontos_perdidos
    print(F'O número secreto é:{num_scret}')
    print('='*30)
    print('Fim do jogo!')
    print('='*30)

# para rodar no terminal
if(__name__ == '__main__'):
    jogar()