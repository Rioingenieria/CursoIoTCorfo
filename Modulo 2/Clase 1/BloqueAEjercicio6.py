a = float((input("Ingrese lado a: ")))
b = float((input("Ingrese lado b: ")))
c = float((input("Ingrese lado c: ")))
s = (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print(("El área es de {}").format((round(area,2))))