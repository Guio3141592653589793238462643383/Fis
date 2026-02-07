from tabulate import tabulate
import numpy as np
x = np.arange(0, 101, 1)
y= (-0.2222 * x) +60
filas=[[val_x, val_y] for val_x, val_y in zip(x,y)]
print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))