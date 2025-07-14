print('=' * 30)
print('{:^30}'.format('Banco Lucas'))
print('=' * 30)
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
Saque = int(input('Digite o valor do saque: R$ '))
total = Saque
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
           print(f'Total de cédulas é {totalced} de {ced}.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco!')
