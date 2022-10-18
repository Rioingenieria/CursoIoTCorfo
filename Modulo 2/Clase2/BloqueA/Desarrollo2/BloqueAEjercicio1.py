#Escriba un programa que muestre la talba de multiplicar del 1 al 10 del número
#ingresado por el usuario

numero = round(float(input("Ingrese número: ")))
producto = ""
i = 1
j = 0

while j < 10:
    producto = round(numero*i)
    print(numero, "X", i, "=", producto)
    i += 1
    j += 1
