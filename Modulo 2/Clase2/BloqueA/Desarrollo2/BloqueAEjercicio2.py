#Escriba un programa que entregue todos los divisores de un número entero ingresado.
#Su programa deberá validar que el número ingresado sea positivo (> 0).
#En caso que cero o negativo, deberá mostrar un mensaje de error.

numero = int(input("Ingrese un número: "))

i = 1
acumulador = ""

if numero > 0:
    while i <= numero:
        divisor = numero % i
        if divisor == 0:
            j = str(i)
            acumulador += " "+j
        i += 1
    print(acumulador)
else:
    print("Error, debe ingresar un número mayor a 0")