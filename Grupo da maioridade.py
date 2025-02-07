from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc =int(input('Em que ano {}º a pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >=18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores'.format(totmenor))
