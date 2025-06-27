import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('Essa será a lista de apresentação: ')
print(lista)

# random.shuffle possibilita embaralhar os itens de uma lista.
# Outra forma de trabalhar o código é: from random import shuffle.