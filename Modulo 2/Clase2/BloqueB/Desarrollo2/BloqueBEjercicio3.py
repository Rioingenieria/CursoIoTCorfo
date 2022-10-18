#Escriba un programa que pida al usuario un valor entero n
#E imprima un patrón triangular de n líneas:

n = int(input("Ingrese número de líneas: "))
i = 0
mas = ""

while i <= n:
    mas = mas+str("+")*i+"\n"
    i += 1
print(mas)