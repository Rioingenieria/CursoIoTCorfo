'''
El banco CBI necesita implementar mejoras en sus mecanismos de seguridad,
precisamente en los que están relacionados con la generación de claves
iniciales para sus clientes de tarjetas de crédito.
Para esto, desarrolle un programa que permita generar una clave de 4 dígitos,
usando el siguiente algoritmo:

- Leer tantos números como sea necesario para generar la clave.
- Para cada número deberá recorrer sus dígitos y encontrar el menor.
- Si el dígito menor es par, pasará a formar parte de la clave, en caso contrario,
se procesa el siguiente número hasta formar la clave de 4 dígitos.
- Mostrar la clave obtenida.
'''

from random import randint

clave = ''

while len(clave) != 4:
    num = randint(1, 9999)
    menor = num
    residuo = 0
    #print('El número es', num)
    while num >=1:
        residuo = num % 10
        if residuo < menor:
            menor = residuo
        num = num // 10
    #print('El menor es', menor)
    if menor % 2 == 0:
        clave += str(menor)
print("La clave es", clave)






