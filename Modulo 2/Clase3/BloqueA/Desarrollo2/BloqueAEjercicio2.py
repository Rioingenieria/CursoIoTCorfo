'''
Escriba un programa que resuelva una ecuación de segundo grado de la forma:
ax^2 + bx + c = 0
x = (- b +- (b^2 - 4ac)^0.5)/2a

Recuerde que primero debe calcular el discriminante (d = b^2 - 4ac)
para determinar si la ecuación, (1) no tiene una solución real (d < 0),
(2) tiene una solución única (d == 0) o (3) tiene 2 soluciones (d > 0).

Use alguna función :)

'''

def discriminante(a, b, c):
    d = b**2-4*a*c
    return d

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

resultado = discriminante(a,b,c)
if resultado > 0:
    print("La ecuación tiene 2 soluciones: ")
    x1 = (-b+resultado**0.5)/2*a
    x2 = (-b-resultado**0.5)/2*a
    print("x1 =", x1)
    print("x2 =", x2)
elif resultado == 0:
    print("La ecuación tiene solución única: ")
    x = -b/2*a
    print("x =", x)
else:
    print("La ecuación no tiene solución real")