import random

print('*******************************')
print('*     Jogo da adivinhação     *')
print('*******************************')

print('Tenta acertar o número que eu escolhi.')

numero = random.randint(1,20)
chance = 1
tentativa = 3
print(numero)
while(chance <= 3):


    print('Tentativa {}  de {}.'.format(chance, tentativa))
    print('Escolha um número entre 1 e 20.')
    chute = int(input('Escreva seu número: '))
    chance = chance + 1

    if(chute < 1 or chute > 20):
        print('Número inválido. Você desperdiçou um chance.')
        continue

    if(chute == numero):
        print('Você acertou.')
        break
    elif(chute < numero):
        print('Você errou. O numero que eu escolhi é maior que', chute)
    elif(chute > numero):
        print('Você errou. O número que eu escolhi é menor que', chute)



print('Fim de Jogo!')