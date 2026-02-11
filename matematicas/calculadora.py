import math
def suma(a, b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b==0:
        return print("Error: División por cero no permitida,")
    else:
        return a/b
def potencia(base, exponente):
    return base **exponente
def raiz(base, indice):
    return base **(1/indice)
inputo=input("¿Qué operación desea realizar? (1. Suma, 2. Resta, 3. Multiplicación, 4. División, 5. Potencia, 6. Raíz):")
if inputo=="1":
    a=float(input("Ingrese el primer número: "))
    b=float(input("Ingrese el segundo número:"))
    resultado_suma=suma(a,b)
    print("El resultado de la suma es:", resultado_suma)
elif inputo=="2":
    a=float(input("Ingrese el primer número: "))
    b=float(input("Ingrese el segundo número:"))
    resultado_resta=resta(a,b)
    print("El resultado de la resta es:", resultado_resta)
elif inputo=="3":
    a=float(input("Ingrese el primer número: "))
    b=float(input("Ingrese el segundo número:"))
    resultado_multiplicacion=multiplicacion(a,b)
    print("El resultado de la multiplicación es:", resultado_multiplicacion)
elif inputo=="4":
    a=float(input("Ingrese el primer número: "))
    b=float(input("Ingrese el segundo número:"))
    resultado_division=division(a,b)
    print("El resultado de la división es:", resultado_division)
elif inputo=="5":
    base=float(input("Ingrese la base:"))
    exponente=float(input("Ingrese el exponente:"))
    potencia_resultado=potencia(base, exponente)
    print("El resultado de la potencia es de:", potencia_resultado)
elif inputo=="6":
    base=float(input("Ingrese el radicando:"))
    indice=float(input("Ingre el indice de la raíz:"))
    raiz_resultado=raiz(base, indice)
    print("El resultado de la raíz es de:", raiz_resultado)
else:
    print("Opción no válida. Por favor seleccione un número del 1 al 6.")
