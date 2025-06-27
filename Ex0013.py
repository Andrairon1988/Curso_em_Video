vl_SalarioInicial = float(input('Qual era o salário do funcionário: '))
vl_AumentoSalario = vl_SalarioInicial * 0.15
vl_SalarioReajustado = vl_SalarioInicial + vl_AumentoSalario
print('Um funcionário que ganhava R${:.2f}, com um aumento de 15% passa a receber R${:.2f}.'.format(vl_SalarioInicial, vl_SalarioReajustado))

# Outra forma de cálculo = vl_SalarioInicial + (vl_SalarioInicial * 15/100) --- O mesmo que Preço - 15%