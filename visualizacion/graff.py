from tabulate import tabulate
import numpy as np
x = np.linspace(0, 3, 100 )
y=  x *np.sin(x)
filas=[[val_x, val_y] for val_x, val_y in zip(x,y)]

print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))