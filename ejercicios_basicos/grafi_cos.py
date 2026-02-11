import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
x= sp.symbols("x")
y= sp.sin(x)
derivada= sp.diff(y, x)
f= sp.lambdify(x, derivada, 'numpy')
x_vals= np.linspace(0, 8*np.pi, 100)
y_vals=f(x_vals)
plt.plot(x_vals, y_vals)
plt.title("Gráfica de cos(x)")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(True)
plt.show()
filas = [[xv, yv] for xv, yv in zip(x_vals, y_vals)]
print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))