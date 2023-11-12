print('='*30)
print('Bem vindo ao jogo de adiviação!')
print('='*30)

num_scret = 42

chute = int(input('Digite o seu número: '))
print(f'O seu numero é:{chute}')
if(num_scret==chute):
    print('você acertou!!')
else:
    print('Você errou!!')