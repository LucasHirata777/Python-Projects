nome = str(input('Qual é o seu nome:').strip())
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é diferente e popular no Brasil.')
elif nome == 'Ana' or nome == 'Claúdia' or nome == 'Jéssica' or nome == 'Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')


print('Tenha um Bom Dia, {}'.format(nome))
