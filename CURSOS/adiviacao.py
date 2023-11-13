print('='*32)
print('Bem vindo ao jogo de adiviação!')
print('='*32)

num_scret = 42

chute = int(input('Digite o seu número: '))
print(f'O seu numero é:{chute}')
if(num_scret==chute):
    print('você acertou!!')
else:
    if(num_scret < chute):
        print('Você fez um chute maior do que o numero secreto')
    if(num_scret > chute):
        print('Você fez um chute menor do que o numero secreto')
print('='*30)
print('Fim do jogo!')
print('='*30)