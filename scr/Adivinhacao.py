

print('*******************************')
print('*     Jogo da adivinhação     *')
print('*******************************')

numero = 5

print('Tenta acertar o número que eu escolhi.')

chute = int(input('Escreva seu número: '))

if(chute == numero):
    print('Você acertou.')
else:
    print('Você errou.')

