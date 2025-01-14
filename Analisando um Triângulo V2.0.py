print('-=' * 20)
print('Analisando Triângulos V2.0')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos conseguem formar um triângulo.')
    if r1 == r2 == r3:
        print('Forma um Triângulo Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Forma um Triângulo Escaleno!')
    else:
        print('Forma um Triângulo Isóceles!')
else:
    print('Os segmentos não conseguem formar um triângulo.')
