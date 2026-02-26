import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

x = np.linspace(0, 50, 100 )
y=  23 * x

filas=[[val_x, val_y] for val_x, val_y in zip(x,y)]
print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))

plt.plot(x, y, label="f(x) = 23x")
plt.title("Gráfica de 23X")
plt.xlabel("x")
plt.ylabel("f(x) = 23x")
plt.grid(True)
plt.show()

