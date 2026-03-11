import numpy as np
n = 1_000_000  
x= np.linspace( 2, 4, n)
y= x**2-3*x+5
integral= np.trapezoid(y,x)
print("El valor aproximado de la integral es:", integral)
