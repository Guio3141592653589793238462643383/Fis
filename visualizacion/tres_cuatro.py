from tabulate import tabulate
import numpy as np
x= np.linspace(3, 4, 500)
y= np.exp(x)
filas=[[val_x, val_y] for val_x, val_y in zip(x,y)]
print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))
