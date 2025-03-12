from random import randint
computador = randint(0,10)
print('Sou seu PC... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
palpites = 0
acertou = False
while not acertou:
    jogador =int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Você está longe... o número que pensei é maior, tente mais uma vez!')
        elif jogador > computador:
            print('Você errou... o número que eu pensei é menor, tente mais uma vez!')
print('Acertou com {} tentativas, Parabéns!!! '.format(palpites))
