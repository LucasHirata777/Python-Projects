soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += cont + 1
print('Você informou {} números Pares e a soma deles é {}.'.format(cont, soma))
