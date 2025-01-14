from datetime import date
atual= date.today().year
nascimento = int(input('Qual é o seu ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação Mirim.')
elif idade <= 14:
    print('Classificação Infantil.')
elif idade <= 19:
    print('Classificação Júnior.')
elif idade <= 25:
    print('Classficação Sênior.')
else:
    print('Classificação Master.')
