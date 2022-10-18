#Desarrolle una función llamada desviacion_estandar(valores) cuyo parámetro
#valores sea una lista de números reales. La función debe retornanr la desviación
#estandar de los valores:

#sigma = sqrt(sum(xi - x)**2)/n-1))

#Donde n es la cantidad de valores, x periódico es el promedio, y los xi
#son cada uno de los valores. Esto significa que hay que hacerlo siguiendo
#los siguientes pasos:

#1. Calcular el promedio de los valores.
#2. A cada valor, restarle el promedio, y el resultado elevarlo al cuadrado.
#3. Sumar todos los valores obtenidos.
#4. Dividir la suma por la cantidad de valores y sacar la raíz cuadrada del
#resultado.

def desviacion_estandar(valores):
    suma = 0
    promedio = sum(valores) / len(valores)
    for v in valores:
        suma += (v - promedio) ** 2
    return (suma / (len(valores) - 1)) ** 0.5


