CustoDia = 60
CustoKm = 0.15

Dia = int(input('Por quantos dias o carro foi locado? '))
km = float(input('Quantos Km foram percorridos? '))
ValorTotal = (CustoDia * Dia) + (CustoKm + km)
print('O total a pagar é de R${:.2f}'.format(ValorTotal))
