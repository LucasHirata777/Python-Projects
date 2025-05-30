tot18 = toth = totf20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totf20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos é {tot18}.')
print(f'Total de homens cadastrados foi {toth}.')
print(f'Total de mulheres com menos de 20 anos foi {totf20}')
print ('O programa finalizou!')
