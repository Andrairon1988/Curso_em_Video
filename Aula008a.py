# Para incluir algo em Python é utilizado o comando "import".
# import doces - Importa todos os doces.
# from doces import pudim - Da biblioteca doces, importa apenas o pudim.
# Exemplo biblioteca math.
# - ceil: arredonda para cima.
# - floor: arredonda para baixo.
# - trunc: elimina o número da vírgula para frente.
# - pow: potência, semelhante a **.
# - sqrt: raíz quadrada.
# - factorial: calcula o fatorial de um número.
# Exemplo: import math ou from math import sqrt, ceil.

from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, floor(raiz)))
