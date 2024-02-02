import sys
import os
from math import cos, sin, exp, sinh, cosh
import sympy as sp
import numpy as np

def LimpaTela():
    sistema = sys.platform
    if sistema == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def Funcao():
    # Solicita que o usuário digite a função
    # O programa permite o uso de funções polinomiais, trigonométricas e exponenciais.
    print('\t\t\tPolinomial: a*x**n + b*x**(n-1) + ... + c*x + d ; n ϵ Z')
    print('\t\t\tTrigonométrica: cos(x) ; sin(x)')
    print('\t\t\tHiperbolica: cosh(x) ; sinh(x)')
    print('\t\t\tExponencial: exp(x)\n')
    expr = input("\t\t\tf(x) = ")
    return expr     #Retorna a função definida pelo usuário

def dividirI(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\t\t\tDigite uma opção válida')
            continue
        else:
            return n
        
def Refazer(msg):
    while True:
        try:
            n = input(msg).upper()
        except (TypeError, ValueError):
            print('\t\t\tDigite um opção válida')
            continue
        else:
            if n == 'S':
                LimpaTela()
                Simpson1()
            elif n == 'N':
                return 0
            elif n != 'S' and n != 'N':
                print('\t\t\tDigite uma opção válida')

def derivada(f, n, a, b):
    x = sp.Symbol('x')
    h = sp.sympify(f, evaluate=False)  # Evita a avaliação imediata da expressão
    f_linha = sp.diff(h, x, n)
    f_linha_lambda = sp.lambdify(x, f_linha)
    x_valores = np.linspace(a, b, 100)
    y_valores = f_linha_lambda(x_valores)
    maximo = np.max(y_valores)
    return maximo     

def Simpson1():
    f = Funcao()
    LimpaTela()
    print('\t\t\t2ª Regra de Simpson\n')
    print(f'\t\t\tf(x) = {f}\n')
    a, b = Intervalo()
    LimpaTela()
    print('\t\t\t2ª Regra de Simpson\n')
    print(f'\t\t\tf(x) = {f}')
    print(f'\t\t\tI = [{a}, {b}]\n')
    while True:
        particao = dividirI('\t\t\tO intervalo I será dividido em quantos subintervalos: ')
        if particao % 3 == 0:
            break
        elif particao % 3 != 0:
            print('\n\t\t\tO número de subintervalos deve ser múltiplo de 3.\n')
            continue
    subInt = (b - a)/particao
    x = a
    integral = eval(f)
    for i in range(1, particao):
        x += subInt
        coef = 2 if i % 3 == 0 else 3  # coeficiente multiplicador
        integral += coef * eval(f)
    x = b
    integral += eval(f)
    #Cálculo do Erro
    maximo = derivada(f, 4, a, b)
    erro = -(b - a)**5*maximo/(80*particao**4)
    integral += erro
    integral *= (3*subInt/8)
    print(f'\n\t\t\tA integral definida da função f no intervalo I é aproximadamente {integral:.10f}\n')
    n = Refazer('\t\t\tFazer outra operação [S/N]: ')

def Intervalo():
    while True:
        try:
            print('\t\t\tInforme o intervalo [a, b]')
            a = float(input('\t\t\ta: '))
            b = float(input('\t\t\tb: '))
        except (TypeError, ValueError):
            print('\t\t\tDigite valores válidos')
        else:
            return a, b
    

#Corpo_Principal
print('\t\t\t2ª Regra de Simpson\n')
Simpson1()



