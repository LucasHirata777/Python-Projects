número = int(input('Digite um número: '))
print ('''Escolha uma das bases para a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual {}.'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual {}.'.format(número, oct(número)[2:]))
elif opção == 3:
    print(('{} convertido para Hexadecimal é igual {}.'.format(número, hex(número)[2:])))
else:
    print('Opção inválida, digite novamente.')
