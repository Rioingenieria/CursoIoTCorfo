numero = int(input("ingrese el primer numero: "))
a = int(input("ingrese el segundo numero: "))
b = int(input("ingrese el tercer numero: "))
c = int(input("ingrese el cuarto numero: "))
d = int(input("ingrese el quinto numero: "))
valor = 0
if a > b and a > c and a > d:
    valor = a
elif b > a and b > c and b > d:
    valor = b
elif c > a and c > b and c > d:
    valor = c
elif d > a and d > b and d > c:
    valor = d

print("el numero mas lejano al primero es", valor)

