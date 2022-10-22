codigo = input('Ingrese hora cifrada: ')
divide=codigo.find(":")

suma = 0
for c in range(divide):
    suma += int(c)
hora = suma % 24

suma = 0
for c in range(divide,len(codigo)):
    suma += int(c)
minutos = suma % 24

print(hora,":",minutos)