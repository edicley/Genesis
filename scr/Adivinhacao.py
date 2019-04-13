import random

print('*******************************')
print('*     Jogo da adivinhação     *')
print('*******************************')

numero = random.randint(1,20)
chance = 1

while(chance <= 3):

    print('Tenta acertar o número que eu escolhi.')

    chute = int(input('Escreva seu número: '))

    if(chute == numero):
        print('Você acertou.')
    elif(chute < numero):
        print('Você errou. O numero que eu escolhi é maior que', chute)
    elif(chute > numero):
        print('Você errou. O número que eu escolhi é menor que', chute)

