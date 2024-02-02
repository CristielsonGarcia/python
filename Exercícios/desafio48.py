print('Soma de todos os ímpares entre 1 e 500 que são divisíveis por 3')
s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print(f'A soma será {s}')