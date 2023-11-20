import random

print('='*32)
print('Bem vindo ao jogo de adiviação!')
print('='*32)

num_scret= round(random.random() * 100)
total_tentativas = 10

for rodadas in range(1, total_tentativas +1):
    print(f'Tentativas {rodadas} de {total_tentativas}')
    chute = int(input('Digite um número entre 1 e 100: '))
   
    print(f'O seu numero é:{chute}')
    if(chute< 1 or chute>100):
        print("Você deve digitar um número entre 1 e 100")
        continue
    if(num_scret==chute):
        print('você acertou!!')
        break
    else:
        if(num_scret < chute):
            print('Você fez um chute maior do que o numero secreto')
        elif(num_scret >   chute):
            print('Você fez um chute menor do que o numero secreto')
print(F'O número secreto é:{num_scret}')
print('='*30)
print('Fim do jogo!')
print('='*30)