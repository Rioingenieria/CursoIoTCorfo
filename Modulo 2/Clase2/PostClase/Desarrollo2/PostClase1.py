'''
Una fundación de ayuda a la comunidad está haciendo una campaña para la
recolección de dinero para poner máquinas de ejercicios en un parque. Para
esto se considera que podría haber un total de N benefactores o juntar un
monto total de M pesos (cualquiera de las dos condiciones se debe cumplir)

Escriba un programa que ingrese la cantidad total de benefactores N y el
monto total a recaudar M. Su programa debe solicitar el nombre y el monto
que donará cada benefactor, uno por uno, Su programa debe detenerse una vez
que se alcance el monto total M, o cuando se terminen de ingresar los
N benefactores.

Indique cuál es el monto mayor donado y que benefactor lo donó
'''

benefactores = int(input("Ingrese la cantidad de benefactores: "))
monto = int(input("Ingrese el monto total a recaudar: "))
i = 0
suma = 0
mayor = -float("inf")

while i < benefactores or suma <= monto:
    benefactor = input("Ingrese el nombre del benefactor: ")
    donacion = float(input("Ingrese el monto de su donación: "))
    suma += donacion
    if donacion > mayor:
       mayor = donacion
       benefactormayor = benefactor
    i += 1
    print("La cantidad de benefactores actual es:", i)
    print("El monto actual es:", suma)
print("El monto mayor donado es: "+str(mayor)+" y el benefactor que lo donó es "+benefactormayor)


