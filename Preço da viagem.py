distancia = float(input('Qual é a distãncia da sua viagem?'))
print('Você está prestes a realizar uma viagem de {:.2f} Km.'.format(distancia))
if distancia<= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua viagem é R$ {:.2f}.'.format(preco))
