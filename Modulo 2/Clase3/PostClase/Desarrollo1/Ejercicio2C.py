def valida(cadena):
    retorno = True
    for i in cadena.upper():
        if "ACGT ".count(i.upper()) == 0:
            retorno = False
    return retorno

def cantidad(cadena,base):
    return cadena.count(base)

animales = 0
vegetales = 0
no_validas = 0

numero_cadenas = int(input("Cantidad de cadenas a ingresar: "))
for i in range(numero_cadenas):
    cadena = input("Ingrese cadena {}: ".format(i+1))
    adenina = cantidad(cadena,"A")
    citosina = cantidad(cadena,"C")
    guanina = cantidad(cadena,"G")
    timina = cantidad(cadena,"T")

    if valida(cadena):
        if citosina+guanina > adenina+timina:
            vegetales += 1
        else:
            animales += 1
    else:
        no_validas += 1

print("Cantidad animales: {}".format(animales))
print("Cantidad vegetales: {}".format(vegetales))
print("Cantidad no validas: {}".format(no_validas))

