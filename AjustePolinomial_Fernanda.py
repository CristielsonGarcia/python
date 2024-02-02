import numpy as np
import os 
from sys import platform

def LimpaTela():
    sistema = platform
    if sistema == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def LeiaInteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\t\t\tDigite uma opção válida')
            continue
        else:
            if n < 0:
                print('\t\t\tDigite um valor válida.')
                continue
            return n
        
def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\t\t\tDigite uma opção válida')
            continue
        else:
            return n

def Ajuste_Polinomial():
    n = []
    x = []
    y = []
    var = ['i', 'xi', 'yi']

    c = LeiaInteiro('\t\t\tInforme a quantidade de valores de xi: ')
    LimpaTela()
    print('\t\t\tAjuste Polinomial\n')
    for j in range(0, c):
        n.append(j+1)
        print(f'\t\t\tValor de x{j+1}: ', end='')
        x.append(LeiaFloat(''))
        print(f'\t\t\tValor de y{j+1}: ', end='')
        y.append(LeiaFloat(''))

    LimpaTela()
    print('\t\t\tAjuste Linear Simples\n')
    matriz = [n, x, y]
    for c in range (0, len(matriz)):
        print(f'\t\t\t|{var[c]:^5}|', end = ' ')
        for b in range(0, len(n)):        
            print(f'|{matriz[c][b]:^5}|', end=' ')
        print()

    x = np.array(x)
    y = np.array(y)

    x_potencia = np.column_stack([x ** d for d in range(3)])

    coef = np.linalg.lstsq(x_potencia, y, rcond=None)[0]

    print(f'\n\t\t\tA melhor curva que passa pelos pontos é y = {coef[0]:.2f} + {coef[1]:.2f}x + {coef[2]:.2f}x^2')


Ajuste_Polinomial()