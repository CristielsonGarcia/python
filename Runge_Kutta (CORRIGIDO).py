"""
DISCENTES:
    ANGELO JOSE DA SILVA NETO 
    CRISTIELSON GARCIA CRUZ
    HELLEN FERREIRA DA SILVA
    ISAQUE GABRIEL SILVA TRINDADE
    VINICIUS CAVALCANTE HOLANDA
"""

from sys import platform
from os import system
import sympy as sp
from math import sin, cos, exp, cosh, sinh


def LimpaTela():
    # Quando utilizada limpa toda a tela de exibição
    sistema = platform
    if sistema == 'linux':
        system('clear')
    else:
        system('cls')

def titulo():
    # Cria um menu exibindo as opções de aplicação do método e retorna a opção escolhida
    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\t\tMÉTODOS DE RUNGE-KUTTA\n\n')
    print('\t\t1 - MÉTODOS DE RUNGE-KUTTA DE 2ª ORDEM\n')
    print('\t\t2 - MÉTODOS DE RUNGE-KUTTA DE 4ª ORDEM\n')
    print('\t\t3 - SAIR\n')
    n = leiaInteiroMenu('\t\tEscolha o método a ser utilizado: ')
    return n

def funcao():
    # Solicita que o usuário digite a função
    # O programa permite o uso de funções polinomiais, trigonométricas, exponenciais e hiperbólicas.
    print('\t\tDefina a equação diferencial y\' = f\'(x)\n')
    print('\t\tPolinomial: a*x**n + b*x**(n-1) + ... + c*x + d ; n ϵ Z')
    print('\t\tTrigonométrica: cos(x) ; sin(x)')
    print('\t\tHiperbolica: cosh(x) ; sinh(x)')
    print('\t\tExponencial: exp(x)\n')
    expr = input("\t\tf\'(x) = ")
    f = sp.parse_expr(expr)
    return f  

def f(f, x, y):
    # Retorna o valor da função f calculada nos pontos x e y
    return f.subs({'x': x, 'y': y})

def leiaInteiroMenu(msg):
    # Retorna somente os valores 1 e 2, é utilizada para escolher as opções do menu. (Caso se escolha uma opção inválida)
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\t\t\tDigite um opção válida.')
            continue
        else:
            if n > 3 or n < 1:
                print('\t\t\tDigite um opção válida.')
                continue
        return n
    
def leiaInteiro(msg):
    # Retorna somente valores inteiros, é utilizada para tratamente de erros. (Ex: O programa peça um valor inteiro e o usuário digite um letra ou um número com vírgula)
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\t\t\tDigite um opção válida.')
            continue
        else:
            return n
    
def leiaFloat(msg):
    # Retorna somente valores numericos, é utilizada para tratamente de erros. (Ex: O programa peça um valor flutuante e o usuário digite um letra ou um simbolo)
    while True:
        try: 
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\t\t\tDigite um opção válida.')
            continue
        else:
            return n
    
def RungeKutta2():
    # Aplica o método de Runge-Kutta de segunda ordem.
    expr = funcao()
    # Define 'x' e 'y' como variáveis 
    x = sp.Symbol('x')
    y = sp.Symbol('y')

    LimpaTela()

    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\tMÉTODOS DE RUNGE-KUTTA DE 2ª ORDEM\n')
    print(f'\t\ty\' = {expr}\n')
    print('\t\tDigite o valor inicial')
    x0 = leiaFloat('\t\tx0 = ')
    y0 = leiaFloat(f'\t\ty({x0}) = ')

    LimpaTela()

    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\tMÉTODOS DE RUNGE-KUTTA DE 2ª ORDEM\n')
    print(f'\t\ty\' = {expr}')
    print(f'\t\ty({x0}) = {y0}\n')
    print('\t\tPara qual valor de x você deseja encontrar o valor aproximado de y?')
    x = leiaFloat('\t\tx = ')

    LimpaTela()

    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\tMÉTODOS DE RUNGE-KUTTA DE 2ª ORDEM\n')
    print(f'\t\ty\' = {expr}')
    print(f'\t\ty({x0}) = {y0}\n')
    print(f'\t\tDetermine o valor de de y({x})\n')
    h = leiaFloat('\t\tInforme o valor do passo: ')

    passo = round(x/h)
    for i in range(passo): 
        yk = y0 + (h/2)*(f(expr, x0, y0) + f(expr, x0 + h, y0 + h*f(expr, x0, y0)))
        x0 += h
        y0 = yk            
        
    print(f'\n\t\ty({x}) = {y0}')
    opcao = Refazer('\n\t\tDeseja fazer outra operação[S/N]: ')

def RungeKutta4():
    # Aplica o método de Runge-Kutta de quarta ordem.
    expr = funcao()
    # Define 'x' e 'y' como variáveis 
    x = sp.Symbol('x')
    y = sp.Symbol('y')

    LimpaTela()

    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\tMÉTODOS DE RUNGE-KUTTA DE 4ª ORDEM\n')
    print(f'\t\ty\' = {expr}\n')
    print('\t\tDigite o valor inicial')
    x0 = leiaFloat('\t\tx0 = ')
    y0 = leiaFloat(f'\t\ty({x0}) = ')

    LimpaTela()

    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\tMÉTODOS DE RUNGE-KUTTA DE 4ª ORDEM\n')
    print(f'\t\ty\' = {expr}')
    print(f'\t\ty({x0}) = {y0}\n')
    print('\t\tPara qual valor de x você deseja encontrar o valor aproximado de y?')
    x = leiaFloat('\t\tx = ')

    LimpaTela()

    print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
    print('\t\tMÉTODOS DE RUNGE-KUTTA DE 4ª ORDEM\n')
    print(f'\t\ty\' = {expr}')
    print(f'\t\ty({x0}) = {y0}\n')
    print(f'\t\tDetermine o valor de de y({x})\n')
    h = leiaFloat('\t\tInforme o valor do passo: ')

    passo = round(x/h)
    for i in range(passo): 
        k1 = h * f(expr, x0, y0)
        k2 = h * f(expr, x0 + h/2, y0 + k1/2)
        k3 = h * f(expr, x0 + h/2, y0 + k2/2)
        k4 = h * f(expr, x0 + h, y0 + k3)
        yk = y0 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        x0 += h
        y0 = yk     
              
        
    print(f'\n\t\ty({x}) = {y0}')
    opcao = Refazer('\n\t\tDeseja fazer outra operação[S/N]: ')
    
    
def Escolha(n):
    # Retorna o método de Runge-Kutta escolhido pelo usuário
    if n == 1:
        LimpaTela()
        print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
        print('\t\tMÉTODOS DE RUNGE-KUTTA DE 2ª ORDEM\n\n')
        RungeKutta2()
    elif n == 2:
        LimpaTela()
        print('\n\tSOLUÇÕES NUMÉRICAS DE EQUAÇÕES DIFERENCIAIS ORDINÁRIAS\n\n')
        print('\t\tMÉTODOS DE RUNGE-KUTTA DE 4ª ORDEM\n\n')
        RungeKutta4() 
    elif n == 3:
        LimpaTela()
        print('\n\t\t\tOBRIGADO!!!\n\n')

def Refazer(msg):
    # Responsável por permitir ao usuário refazer uma nova operação sem a necessidade de executar o código novamente
    while True:
        try:
            n = input(msg).upper()
        except (TypeError, ValueError):
            print('\t\t\tDigite um opção válida')
            continue
        else:
            if n == 'S':
                LimpaTela()
                opcao = titulo()
                Escolha(opcao)
                break
            elif n == 'N':
                return n
            elif n != 'S' and n != 'N':
                print('\t\t\tDigite uma opção válida')
                continue  




#-------------------------------------- Função Principal --------------------------------------

#Chamada da função "titulo"
n = titulo()
Escolha(n)
