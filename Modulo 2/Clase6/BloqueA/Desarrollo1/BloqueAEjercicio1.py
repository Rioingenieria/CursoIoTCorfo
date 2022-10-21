archivo = open("quijote.txt")
contador_linea = 0
contador_letras = 0
contador_palabras = 0
for linea in archivo:

    contador_palabras += len(linea.split())
    contador_linea += 1
    contador_letras += len(linea)

archivo.close()
print(contador_linea)
print(contador_palabras)
print(contador_letras)
