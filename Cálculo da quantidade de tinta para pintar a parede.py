largura =float(input('Qual é a largura da parede: '))
altura = float(input('Qual é a altura da parede: '))
a = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área vale {} m2'.format(largura, altura, a))
tinta = a/2
print('Você precisara de {} litros de tinta para pintar a parede'.format(tinta))
