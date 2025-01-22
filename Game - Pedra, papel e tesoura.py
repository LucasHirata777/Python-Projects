from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[0] Pedra 
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 20)
print('O computador escolheu {}.'.format(itens[computador]))
print('O Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
       print('Empate')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Você perdeu')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 0:
        print('Você perdeu!')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Jogando inválida!')

elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 0:
        print('Você ganhou!')
    else:
        print('Jogador inválido!')
