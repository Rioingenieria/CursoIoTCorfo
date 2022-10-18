'''
Las funciones seno y coseno, pueden ser representadas por sumas infinitas

1) Escriba la función factorial_reciproco(n), que retorne el valor de 1/n!
2) Escriba la función signo(n) que retorne 1 cuando n es par, y -1 cuando n
es impar.
3) Escriba las funciones seno_aprox(x, m) y coseno_aprox(x, m) que aproximen
el seno y el coseno de x, usando los primeros m terminos de las sumatorias.

'''

def factorial_reciproco(n):
    i = 1
    prod = 1
    while i <= n:
        prod *= i
        i += 1
        return 1/prod

def signo(n):
    if n % 2 == 0:
        return 1
    else:
        return -1

def seno_aprox(x, m):
    i = 0
    suma = 0
    while i < m:
        suma += signo(i) * x ** (2 * i + 1) * factorial_reciproco(2 * i + 1)
        i += 1
    return suma

def coseno_aprox(x, m):
    i = 0
    suma = 0
    while i < m:
        suma += signo(i) * x ** (2 * i) * factorial_reciproco(2 * i)
        i += 1
    return suma

