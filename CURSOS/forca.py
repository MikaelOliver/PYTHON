def jogar():
    print('='*32)
    print('Bem vindo ao jogo de adiviação!')
    print('='*32)

    palavra_secreta = 'manga'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input('Qual letra: ')
        chute = chute.strip().upper()
        if( chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print('VOU WIN!!')
    else:
        print('YOU LOSER!!')
    print('FIM DE JOGO!!')







if(__name__ == '__main__'):
    jogar()