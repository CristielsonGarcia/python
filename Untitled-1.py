import sympy as sp

x = sp.Symbol('x')
f = input('f(x) = ')
expr = sp.sympify(f)
_f = sp.diff(f, x)
print(_f)