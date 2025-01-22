peso = float(input('Qual é o seu peso em (kg): '))
altura = float(input('Qual é a sua altura em (m): '))
imc = peso / (altura ** 2)
print('O seu imc equivale há {:.2f}.'.format(imc))
if imc < 18.5:
    print('Atenção você está Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Parabéns voc está no seu Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você esta com Sobrepeso, tome cuidado!')
elif imc >= 30 and imc < 40:
    print('Você está com Obesidade, tome muito cuidado!')
else:
    print('Atenção você está com Obesidade Mórbida, tome muito cuidado!')
