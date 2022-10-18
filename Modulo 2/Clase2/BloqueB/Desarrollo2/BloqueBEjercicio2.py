#En estadística descriptiva, se define el rango de un conjunto de datos reales
#como la diferencia entre el mayor y el menor de los datos.
#Por ejemplo, si los datos son [5.96, 6.74, 7.43, 4.99, 7.20, 0.56, 2.80]
#entonces el rango será: 7.43 - 0.56 = 6.87

#Escriba un programa que; (1) pregunte al usuario cuantos datos ingresará
#(2) pida los datos uno por uno, y (3) entregue como resultado el rango de
#los datos (suponga que todos los datos quue ingrese serán válidos.

numerosolicitado = float(input("Ingresar número: "))
mayor = -float("inf")
menor = float("inf")
i = 0
delta = ""

while i < numerosolicitado:
    numeroingresado = float(input("Ingresar número "+str(i+1)+": "))
    if numeroingresado > mayor:
        mayor = numeroingresado
    elif numeroingresado < menor:
        menor = numeroingresado
    i += 1
delta = mayor - menor
print("El rango será: ", mayor, "-", menor, "=", delta)

