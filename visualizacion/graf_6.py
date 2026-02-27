import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

x = np.linspace(-100, 100, 100)
y = x**2-1

filas=[[val_x, val_y] for val_x, val_y in zip(x,y)]
print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))

plt.plot(x, y, label="f(x) = x^2 + 1")
plt.title("Gráfica de f(x) = x^2 + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
