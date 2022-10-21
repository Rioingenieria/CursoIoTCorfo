def descifra(palabra):
    i = 1
    cifrado = ""
    while i <= len(palabra):
        cifrado += palabra[-i]
        i += 2
    return(cifrado)


palabra = input('Ingrese palabra: ')
print(descifra(palabra))