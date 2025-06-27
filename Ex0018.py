from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {} é igual a {:.2f}, o cosseno {:.2f} e a tagente é {:.2f}'.format(angulo, seno, cosseno, tangente))
