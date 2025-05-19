from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
          tipo = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o PC jogou {computador}, com isso montante de tudo ficou {total}.', end=' ')
    print('--Deu par--!' if total % 2 == 0 else '--Deu Ímpar--!')
    if tipo == 'P':
       if total % 2 == 0:
          print('Você ganhou!')
          v += 1
       else:
           print('Você Perdeu!')
           break
    elif tipo == 'I':
       if total % 2 == 1:
           print('Você ganhou!')
           v += 1
       else:
           print('Você Perdeu!')
           break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
