from datetime import date
atual = date.today().year
nascimento = int(input('Qual ano você nasceu: '))
idade = atual - nascimento
print ('Quem nasceu em {} tem {} anos de idade no ano {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print('Você não precisa se alistar ainda, faltam {} anos para o seu alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos atrás.'.format(saldo))
