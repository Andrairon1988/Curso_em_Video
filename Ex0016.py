# Solução 1:
# n_real = float(input('Digite um valor: '))
# n_int = int(n_real)
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(n_real,n_int))

# Solução 2:
# import math
# num = float(input('Digite um número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

# Solução 3:
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))