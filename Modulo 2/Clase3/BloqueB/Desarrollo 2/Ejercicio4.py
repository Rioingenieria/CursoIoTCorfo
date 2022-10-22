codigo = input('Ingrese hora cifrada: ')
divide=codigo.find(":")

suma = 0
i=0
for i in range(divide):
    suma += int(codigo[i])
hora = suma % 24

suma = 0
i=0
for i in range(divide+1,len(codigo)):
    suma += int(codigo[i])
minutos = suma % 60

print(hora,":",minutos)
