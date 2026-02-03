def volumen_mej(h,l,a):
    return h*l*a
h=float(input("Ingrese la altura del objeto en m:"))
l=float(input("Ingrese el largo del objeto en m:"))
a=float(input("Ingrese el ancho del objeto en m:"))
Vo=volumen_mej(h,l,a)
print("El volumen del objeto es de:", Vo, "m³")
