número = int(input('Digite um número: '))
resultado = número % 2
if resultado == 0:
    print('O número é Par.'.format(número))
else:
    print('O resultado é ímpar.'.format(número))
