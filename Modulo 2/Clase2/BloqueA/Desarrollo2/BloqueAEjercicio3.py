#Escriba un programa que determine si el número es primo o compuesto.

numero = int(input("Ingrese un número: "))

if numero > 0:
    i = 1
    contador = 0
    while i <= numero:
        divisor = numero % i
        if divisor == 0:
            contador += 1
        i += 1
    if contador > 2:
        print("El número es compuesto")
    else:
        print("El número es primo")