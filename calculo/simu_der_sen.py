import sympy as sp
x= sp.symbols('x')
y= sp.sin(x)
derivada= sp.diff(y, x)
print("La derivada de sin(x) es:", derivada)
