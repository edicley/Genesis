import random

def jogar():

    print('*******************************')
    print('*     Jogo da adivinhação     *')
    print('*******************************')

    print('Tenta acertar o número que eu escolhi.')

    numero = random.randint( 1,100 )
    chance = 1
    tentativa = 0

    print('Escolha o nível que quer jogar.')
    print('[1]-Fácil [2]-Médio [3]-Difícil')

    nivel = int(input('Selecione o nível:'))

    if(nivel == 1):
        tentativa = 15
    elif(nivel == 2):
        tentativa = 10
    else:
        tentativa = 5

    #print(numero)
    while(chance <= tentativa):


        print('Tentativa {}  de {}.'.format(chance, tentativa))
        print('Escolha um número entre 1 e 100.')

        chute = int(input('Escreva seu número: '))
        chance = chance + 1

        if(chute < 1 or chute > 100):
            print('Número inválido. Você desperdiçou um chance.')
            continue

        if(chute == numero):
            print('Você acertou.')
            break
        elif(chute < numero):
            print('Você errou. O numero que eu escolhi é maior que', chute)
        elif(chute > numero):
            print('Você errou. O número que eu escolhi é menor que', chute)


    print('Eu escolhi o número', numero)
    print('Fim de Jogo!')

if (__name__ == "__main__"):
    jogar()