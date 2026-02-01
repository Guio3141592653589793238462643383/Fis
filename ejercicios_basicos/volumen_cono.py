from volumen_cono import vol_cono
import math
def vol_cono(radio, altura):
    return (1/3)* math.pi *(radio**2)*altura
radio=float(input("Ingrese el radio de la base del cono (cm):"))
altura=float(input("Ingrese la altura del cono (cm):"))
Vc=vol_cono(radio, altura)
print("El volumen del cono es de:", Vc, "cm³")
