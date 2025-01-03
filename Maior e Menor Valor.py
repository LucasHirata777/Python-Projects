a = int(input('Primeiro valor: '))
b = int(input('Segunda Valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print ('O menor valor digitado foi {}.'.format(menor))
print ('O maior valor digitato foi {}.'.format(maior))
