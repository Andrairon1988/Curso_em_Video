largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
dimensao = largura * altura
pintura = dimensao / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(largura, altura, dimensao))
print('Para pintar essa parede, você vai precisar de {:.2f} litros de tinta'.format(pintura))