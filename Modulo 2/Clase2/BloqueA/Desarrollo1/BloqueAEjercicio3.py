numero = int(input("ingresa un numero: "))
i = 2
continuar = True
while i < numero and continuar:
    if numero % i != 0:
        print("es primo")
        continuar = False
    elif numero % i == 0:
        print("no es primo")
        continuar = False
    i += 1
