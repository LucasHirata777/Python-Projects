from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo {} graus tem o SENO de {:.2f}'.format (an, seno))
cosseno = cos(radians(an))
print('O ângulo {} graus tem o Cosseno de {:.2f}'.format(an, cosseno))
tang = tan(radians(an))
print('O ângulo {} graus tem a Tangente {:.2f}'.format(an, tang))
