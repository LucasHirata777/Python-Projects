Salário = float(input('Qual é o sálario do funcionário: '))
Reajuste = Salário + (Salário * 15/100)
print('O pagamento do funcionário é R$ {:.2f}, com o aumento de 15%, ele vai receber R$ {:.2f}'.format(Salário, Reajuste))
