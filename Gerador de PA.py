print('Gerador de P.A')
print('-=' * 10)
Primeiro = int(input('Primeiro termo: '))
Razão = int(input('Razão de PA: '))
Termo = Primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(Termo), end='')
    Termo += Razão
    cont += 1
print('FIM')
