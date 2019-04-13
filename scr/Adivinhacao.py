import random

print('*******************************')
print('*     Jogo da adivinhação     *')
print('*******************************')

numero = random.randint(1,20)

print('Tenta acertar o número que eu escolhi.')

chute = int(input('Escreva seu número: '))

if(chute == numero):
    print('Você acertou.')
else:
    print('Você errou.')

