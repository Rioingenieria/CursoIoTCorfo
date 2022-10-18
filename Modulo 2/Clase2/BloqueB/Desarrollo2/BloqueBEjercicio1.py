#Escriba un programa que permita determinar el número mayor de n números solicitados
#al usuario.

numerosolicitado = float(input("Ingresar número: "))
mayor = -float("inf")
i = 0
indicemayor = 1

while i < numerosolicitado:
    numeroingresado = float(input("Ingresar número "+str(i+1)+": "))
    if numeroingresado > mayor:
        mayor = numeroingresado
        indicemayor = i
    i += 1
print("El mayor es el ", mayor, "que corresponde al número", indicemayor+1)

