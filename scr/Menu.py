import Adivinhacao
import Forca

print('*******************************')
print('*      Escolha o seu jogo     *')
print('*******************************')

print('[1] Adivinhação - [2] Forca')

jogo = int(input('Digite qual jogo quer jogar:'))

if(jogo == 1):
    print('Iniciando jogo da Adivinhação')
elif(jogo==2):
    print('Iniciando jogo da Forca')