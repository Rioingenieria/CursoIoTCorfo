estatura = float(input("ingrese tu estatura: "))
peso = float(input("ingrese tu peso: "))
edad = int(input("ingrese tu edad: "))
imc = peso / (estatura ** 2)
print(imc)
if edad < 45 and imc < 22.0:
    print("Bajo")
elif edad >= 45 and imc < 22.0:
    print("Medio")
elif edad < 45 and imc >= 22.0:
    print("medio")
elif edad >= 45 and imc >= 22.0:
    print("Alto")