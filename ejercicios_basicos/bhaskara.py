import math
def bhaskara(a, b, c):
    if a==0:
        return None

    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return None

    res1=(-b + math.sqrt(discriminante))/(2*a)
    res2=(-b - math.sqrt(discriminante))/(2*a)
    return res1, res2
    
a=float(input("Ingrese el valor de a:"))
b=float(input("Ingrese el valor de b:"))
c=float(input("Ingrese el valor de c:"))
resultado = bhaskara(a,b,c)
if resultado is None:
    print ("La ecuación no tiene soluciones reales.")
else:
    print("Las raíces de la ecuación son: ", resultado[0], "y", resultado[1])
