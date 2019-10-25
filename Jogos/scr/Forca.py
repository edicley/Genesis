import random

def jogar():

    imprime_cabecalho()
    palavra = carrega_palavra_secreta()
    letras_certas = inicializa_letras_acertadas(palavra)

    acertou = False
    enforcou = False
    erro = 0

    while (not enforcou and not acertou):
        print(letras_certas)

        chute = pede_chute()


        if(chute in palavra):
            marca_chute_correto(chute, letras_certas, palavra)
        else:
            erro += 1
            desenha_forca(erro)

        enforcou = erro == 7
        acertou = '_' not in letras_certas


    if(acertou):
        imprime_mensagem_ganhou()
    else:
        imprime_mensagem_perdeu(palavra)






def imprime_cabecalho():
    print('*******************************')
    print('*     Jogo da adivinhação     *')
    print('*******************************')

def carrega_palavra_secreta():
    arquivo = open('lista_objetos.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper()
    
    return palavra

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Digite uma letra: ')
    chute = chute.strip().upper()

    return chute


def marca_chute_correto(chute, letras_certas, palavra):
    index = 0
    for letra in palavra:
        if (chute.upper() == letra.upper()):
            letras_certas[index] = letra
        index += 1


def imprime_mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdeu(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if(erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erro == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erro == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()