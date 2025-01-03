salário = float(input('Quanto é o salário do funcionário? R$ '))
if salário <= 1250:
    novo = salário + (salário * 15/ 100)
else:
    novo = salário + (salário * 10/100)
print ('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}'.format(salário, novo))
