#Un jugador debe lanzar dos dados numerados del 1 al 6, y su puntaje es la suma
#de los valores obtenidos.
#Un puntaje dado, puede ser obtenido con varias combinaciones posibles.
#Por ejemplo, el puntaje 4 se logra con 3 combinaciones; 1+3, 2+2, 3+1.

#Escriba un programa que pregunte al usuario un puntaje, y muestre como
#resultado la cantidad de combinaciones con las que se puede obtener dicho
#puntaje.

puntaje = int(input("Ingrese el puntaje: "))
d1 = 1
cuenta = 0
while d1 <= 6:
    d2 = 1
    while d2 <= 6:
        if puntaje == d1 + d2:
            print("Combinación:", d1, d2)
            cuenta += 1
        d2 += 1
    d1 += 1
print("Existen", cuenta, "combinaciones para obtener", puntaje)