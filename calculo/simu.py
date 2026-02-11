import numpy as np
n = 1_000_000  
x= np.linspace( 0, np.pi , n)
y=np.trapezoid(np.sin(x), x)
print("El valor aproximado de la integral de sin(x) es:", y)
