print('Supermercado Novo Tempo')
v_prod = float(input('Informe o valor do produto [R$]: '))
print('Escolha a forma de pagamento')
print('1 - À vista (dinheiro/cheque)')
print('2 - À vista no cartão de crédito')
print('3 - Parcelado 2x no cartão de crédito')
print('4 - Parcelado 3x ou mais no cartão')
escolha = int(input('Faça sua escolha: '))
if escolha == 1:
    print(f'Valor total a ser pago R${v_prod * 0.9:.2f}')
elif escolha == 2:
    print(f'Valor total a ser pago R${v_prod * 0.95:.2f}')
elif escolha == 3:
    print(f'Valor total a ser pago R${v_prod}')
else:
    print(f'Valor total a ser pago R${v_prod*1.2:.2f}')