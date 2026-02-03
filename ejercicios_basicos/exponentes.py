import math
def potencia(base, exponente):
    return base **exponente
def raiz(base, indice):
    return base **(1/indice)
pre_input = input("¿Qué desea calcular? (1: Potencia, 2: Raíz): ")
if pre_input == "1":
    base=float(input("Ingrese la base:"))
    exponente=float(input("Ingrese el exponente:"))
    potencia_resultado=potencia(base, exponente)
    print("El resultado de la potencia es de:", potencia_resultado)
elif pre_input == "2":
    base=float(input("Ingrese el radicando:"))
    indice=float(input("Ingrese el índice de la raíz:"))
    raiz_resultado=raiz(base, indice)
    print("El resulado de la raíz es de:", raiz_resultado) 
else:
    print("Opción no válida. Por favor seleccione 1 o 2.")