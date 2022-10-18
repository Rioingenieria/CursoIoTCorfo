'''
Considere las siguientes asignaciones:

a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27,3),9)
z, w = x
v = (x, a)

Sin usar el computador, indiquen en grupo cuál es el resultado y el tipo
de las siguientes expresiones.
Luego, verifique en el computador.

1. a < b
2. y + w
3. x + a
4. len(v)
5. v[1][1]
6. c[0]
7. a + b[1:5]
8. (a + b)[1:5]
9. str(a[2]) + str(b[2])
10. str(a[2] + b[2])
11. str((a + b)[2])
12. str(a + b)[2][0]
'''

a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27,3),9)
z, w = x
v = (x, a)

uno = a < b
dos = y + w
tres = x + a
cuatro = len(v)
cinco = v[1][1]
seis = c[0]
siete = a + b[1:5]
ocho = (a + b)[1:5]
nueve = str(a[2]) + str(b[2])
diez = str(a[2] + b[2])
once = str((a + b)[2])
doce = str(a + b)[2][0]

print("1. a < b =", uno)
print("2. y + w =", dos)
print("3. x + a =", tres)
print("4. len(v) =", cuatro)
print("5. v[1][1] =", cinco)
print("6. c[0] =", seis)
print("7. a + b[1:5] =", siete)
print("8. (a + b)[1:5] =", ocho)
print("9. str(a[2]) + str(b[2]) =", nueve)
print("10. str(a[2] + b[2]) =", diez)
print("11. str((a + b)[2]) =", once)
print("12. str(a + b)[2][0] =", doce)