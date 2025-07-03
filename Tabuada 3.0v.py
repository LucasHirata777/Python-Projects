while True:
      n = int(input('Qual é o número que você deseja ver a tabuada: '))
      if n <= 0:
          break
      print('-' * 30)
      for c in range(1,11):
          print(f'O valor da tabuada é {n} x {c} = {n * c}.')
      print('-' * 30)
print('Programa encerrado, o número digitado foi negativo.')
