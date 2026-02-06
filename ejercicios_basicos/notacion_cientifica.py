n=float(input("Ingrese el número que desea convertir a notación científica:"))
exponente=0
if n<1 and n>0:
    while n<1: 
        n=n*10
        exponente=exponente-1
elif n>=10:
    while n>=10:
        n=n/10
        exponente=exponente+1
print("El número en notación científica es:", n, "x 10^", exponente)
