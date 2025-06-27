valor = int(input('Digite o valor desejado: '))
antecessor = valor - 1
sucessor = valor + 1
print('Analisando o número {}, seu antecessor é {}, e seu sucessor é {}.'.format(valor, antecessor, sucessor))

# Outra forma de fazer a mesma operação é a seguinte:
#.format(valor, (valor-1), (valor+1)))