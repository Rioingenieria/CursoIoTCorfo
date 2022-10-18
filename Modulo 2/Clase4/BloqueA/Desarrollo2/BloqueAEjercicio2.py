'''
El producto interno de dos listas de números es la suma de los productos
de los términos de ambas. Por ejemplo, si: a = [5,1,6] y b = [1,-2,8]
entonces el producto interno entre a y b es:

(5*1) + (1*-2) + (6*8)

Escriba la función producto_interno(a, b) que entregue el producto interno
entre a y b.
'''

def producto_interno(a,b):
    suma = 0
    i = 0
    while i < len(a):
        suma += a[i]*b[i]
        i += 1
    return suma