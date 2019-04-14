def jogar():

    print('*******************************')
    print('*        Jogo da forca        *')
    print('*******************************')

    palavra = 'jaca'.upper()
    print('A palavra escolhida possui {} letras'.format(len(palavra)))
    letras_certas = ['_' for letra in palavra]

    acertou = False
    enforcou = False
    erro = 0

    while (not enforcou and not acertou):
        print(letras_certas)
        chute = input('Digite uma letra: ')
        chute = chute.strip().upper()

        if(chute in palavra):
            index = 0
            for letra in palavra:
                if(chute.upper() == letra.upper()):
                    letras_certas[index] = letra
                index += 1
        else:
            print('Essa letra não existe.')
            erro += 1

        enforcou = erro == 6
        acertou = '_' not in letras_certas


    if(acertou):
        print('Você ganhou')
    else:
        print('Você errou!')

    print('Fim de Jogo!')

if (__name__ == "__main__"):
    jogar()