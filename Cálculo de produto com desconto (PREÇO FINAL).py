preço = float(input('Quanto custa este produto: '))
desconto = preço - (preço * 5/100)
print('O produto que custava R$ {:.2f}, com o desconto de 5% agora vai custar R$ {:.2f}.'.format(preço,desconto)) 
