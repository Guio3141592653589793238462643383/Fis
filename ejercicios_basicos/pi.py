import numpy as np
n = 1_000_000  
x= np.linspace( 0, 1 , n)
y= 4/(1+x**2)
pi_aprox= np.trapezoid(y,x)
print("El valor aproximado de pi es:", pi_aprox)
