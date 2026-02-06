import math
def alt_cono(Vc, radio):
    return (3*Vc)/(math.pi*(radio**2))
def vol_cono(radio, altura):
    return (1/3)* math.pi *(radio**2)*altura
def rad_cono(Vc, altura):
    return math.sqrt((3*Vc)/(math.pi*altura))
input_tip = input("¿Qué desea calcular? (1: Volumen, 2: Altura, 3: Radio): ")
if input_tip == "1":
    radio=float(input("Ingrese el radio de la base del cono (cm):"))
    altura=float(input("Ingrese la altura del cono (cm):")) 
    Vc=vol_cono(radio, altura)
    print("El volumen del cono es de:", Vc, "cm³")
elif input_tip =="2":
    Vc=float(input("Ingrese el volumen del cono en cm³:"))
    radio=float(input("Ingrese el radio de la base del cono (cm):"))
    altura=alt_cono(Vc,radio)
    print("La altura del cono es de:", altura, "cm")
elif input_tip=="3":
    Vc=float(input("Ingrese el volumen del cono en cm³:"))
    altura=float(input("Ingrese la altura del cono (cm):"))
    radio=rad_cono(Vc, altura)
    print("El radio de la base del cono es de:", radio, "cm")
else:
    print("Opción no válida. Por favor seleccione 1,2 o 3.")