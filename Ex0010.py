reais = float(input('Quanto dinheiro você tem na carteira? R$ '))
cotacao = 6.17
dolar = reais/cotacao
print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais, dolar))