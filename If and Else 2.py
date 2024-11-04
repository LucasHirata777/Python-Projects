n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2)/2
print ('A sua média vale {:.1f}'.format(m))
if m >=7:
    print ('Você obteve uma média boa e foi aprovado')
else:
    print ('Sua média é ruim e você não foi aprovado')
