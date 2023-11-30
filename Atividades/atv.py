# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# number = int(input('Digite um número: '))
# for i in range(1, 11):
#    resultado= number * i
#    print(f'{number}* {i} = {resultado}')

# fatorial = 1
# number = int(input('Digite um número: '))
# for i in range(1, number + 1):
#     fatorial = fatorial * i 
    
# print(fatorial)


def vogais(palavra):
    numero_vogais = 0
    vogais = 'aeiou'
    for i in palavra:
        if i in vogais:
            numero_vogais = numero_vogais + 1
    return numero_vogais

wm_palavra = input('Digite uma palavra: ').lower()
resultado = vogais(wm_palavra)
print(f'A palavra {wm_palavra} tem essa quantidade de vogais {resultado}')