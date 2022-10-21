from random import choice

def cadena_adn(cadena):
    adn = ""
    while cadena > 0:
        adn += choice('atcg')
        cadena -= 1
    print(adn)

while 1 == 1:
    largo=int(input("Ingrese largo de la cadena (0 para salir): "))
    if largo != 0:
        cadena_adn(largo)
    else:
        break
