#Un viajero desea saber cuánto tiempo tomó el viaje que realizó.
#El tiene la duración en minutos de cada uno de los tramos del viaje.
#Escriba un programa que permita ingresar los tiempos de viaje de los tramos
#y entregue como resultado, el tiempo total del viaje en formato horas:minutos

#El programa debe dejar de pedir tiempos cuando se ingrese un 0.

j = "1"
tramo = int(input("Duración del tramo "+j+" en minutos: "))
suma = 0
minutos = 0
horas = 0

while tramo != 0:
    suma += tramo
    j = int(j)
    j += 1
    j = str(j)
    tramo = int(input("Duración del tramo " + j + " en minutos: "))

horas = suma // 60
minutos = suma % 60

print("Tiempo total del viaje: "+str(horas)+":"+str(minutos))



