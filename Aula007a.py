#nome = str(input('Qual é o seu nome? '))
#print('Prazer em te conhecer {}!'.format(nome)) - Conteúdo da aula anterior, na qual aprendemos sobre máscaras.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a multiplicação {} \n e a divisão {:.3f}'.format(s, m, d), end=' ')
#{:.3f} -- é a formatação de casas decimais.
#end=' ' -- permite não quebrar a linha entre os prints.
print('Divisão inteira {} e potência {}'.format(di, e))