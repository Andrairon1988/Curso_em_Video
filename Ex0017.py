import math
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(catetoOposto ** 2 + catetoAdjacente ** 2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

#solução2 = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
#solução3 = math.hypot(catetoOposto, catetoAdjacente)

#from math import.hypot