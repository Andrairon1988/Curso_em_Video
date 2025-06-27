vl_PrecoInicial = float(input('Qual o preço do produto? '))
vl_Desconto = vl_PrecoInicial * 0.05
vl_PrecoFinal = vl_PrecoInicial - vl_Desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(vl_PrecoInicial, vl_PrecoFinal))

# Outra forma de cálculo = vl_PrecoInicial - (vl_PrecoInicial * 5/100) --- O mesmo que Preço - 5%