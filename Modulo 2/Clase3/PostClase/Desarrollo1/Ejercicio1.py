numero = int(input("Ingrese n: "))
minimo = 1000
palabra_minimo = ""
maximo = 0
palabra_maximo = ""
for i in range(numero):
    palabra = input("palabra {}: ".format(i+1))
    palabra_recortada = palabra
    for letra in palabra_recortada:
        if palabra_recortada.count(letra) > 1:
            palabra_recortada = palabra_recortada.replace(letra,"",1)
    if len(palabra_recortada) < minimo:
        minimo = len(palabra_recortada)
        palabra_minimo = palabra
    if len(palabra_recortada) > maximo:
        maximo = len(palabra_recortada)
        palabra_maximo = palabra
print("La palabra mas larga es: {}".format(palabra_maximo))
print("La palabra mas corta es: {}".format(palabra_minimo))
