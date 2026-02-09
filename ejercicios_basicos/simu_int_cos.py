import sympy as sp
x = sp.symbols('x')
y= sp.cos(x)
integral=sp.integrate(y, x)
print("La integral de cos(x) es:", integral)