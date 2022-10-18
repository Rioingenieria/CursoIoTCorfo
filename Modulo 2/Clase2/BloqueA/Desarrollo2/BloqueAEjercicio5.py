#A partir de un número cualquiera (entrada) es posible hacer una sucesión
#de números que termina en 1, para ello deberá seguir las siguientes instrucciones:
#- Si el número es par, se debe dividir por 2.
#- Si el número es impar, se debe multiplicar por 3 y sumarle 1.
#Con esto se obtiene el siguiente número de la sucesión, al cual se le aplican
#las mismas operaciones. La sucesión termina cuando el número obtenido es 1.

#Escriba un program que muestre cada número de la sucesión generada hasta
#llegar a 1.

continuar = True
numero = int(input("Ingrese número:"))
while continuar == True:
    par = numero % 2
    if par == 0:
        numero = round(numero / 2)
        print(numero)
    else:
        numero = round((numero * 3) + 1)
        print(numero)
    if  numero == 1:
        continuar = False


