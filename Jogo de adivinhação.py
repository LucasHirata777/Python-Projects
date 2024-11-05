from random import randint
from time import sleep
computador = randint(0,5)
print ('-=-' * 20)
print ('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print ('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(5)
print('Pensei no número {}'.format(computador))
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer.')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))
    print('Que pena, você perdeu com isso eu recomendo tentar novamente.')
