somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1,5):
    print('----- {}° pessoa -----'.format(p))
    nome=str(input('Qual é o seu nome: ')).strip()
    idade=int(input('Qual é a sua idade: '))
    sexo=str(input('Qual é o seu sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in "Mn":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and  idade< 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))
