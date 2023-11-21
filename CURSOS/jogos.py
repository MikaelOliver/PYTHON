import forca
import adiviacao
print('='*32)
print('ESCOLHA O SEU JOGO!')
print('='*32)
def escolhe_jogo():
    print('(1) FORCA (2)ADIVIAÇÃO')
    jogo = int(input('Qual O Jogo? '))

    if(jogo == 1 ):
        print('Jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando adiviação')
        adiviacao.jogar()


if(__name__ == '__main__'):
    escolhe_jogo()