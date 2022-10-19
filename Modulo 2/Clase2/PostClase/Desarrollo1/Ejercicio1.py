benefactores = int(input("Ingrese numero total de benefactores: "))
meta = int(input("Ingrese el monto total a recaudar: "))
acumulado = 0
donador_maximo = ""
maximo = -1
for i in range(benefactores):
    benefactor = input("Ingrese nombre de benefactor {}: ".format(i+1))
    monto = int(input("Ingrese monto de donacion: "))

    if monto >= maximo:
        donador_maximo = benefactor
        maximo = monto

    acumulado += monto
    if acumulado >= meta:
        break
print("El monto mayor donado fue de {} y lo donó {}".format(maximo,donador_maximo))
