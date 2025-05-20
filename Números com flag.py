soma = cont = 0
while True:
      n = int(input('Digite um número (999 para parar): '))
      if n == 999:
          break
      cont += 1
      soma += n
print(f'A soma dos valores foi {soma}.')
print(f'Ao total foram digitados {cont} números.')
