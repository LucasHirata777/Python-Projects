total = totmil = menorp = cont = 0
barato = ' '
while True:
     produto = (str(input('Qual o nome do produto? ')))
     preço = (float(input('Quanto é o preço: R$ ')))
     cont += 1
     total += preço
     if preço > 1000:
        totmil += 1
     if cont == 1 or preço < menorp:
         menorp = preço
         barato = produto
     resp = ' '
     while resp not in 'SN':
         resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
     if resp in 'N':
             break
print(' Fim da execução do Programa! ')
print(f'O valor total da compra foi de R$ {total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$1000.00.')
print(f'O produto mais barato é {barato} e custa R$ {menorp:.2f}.')
