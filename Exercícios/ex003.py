print('-'*20)
print('Soma de dois números')
print('-'*20)
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 == int(n1) and n2 == int(n2):
    print(f'{n1:.0f} + {n2:.0f} = {n1+n2:.0f}')
else:
    print(f'{n1:.1f} + {n2:.1f} = {n1+n2:.1f}')
