estatura=float((input("Ingrese estatura ")))
peso=float((input("Ingrese peso ")))
edad=float((input("Ingrese edad ")))

IMC=peso/(estatura ** 2)

if IMC<22.0 and 2 < edad < 45:
    print("Indice Bajo")
elif IMC>=22.0 and 2 < edad < 45:
    print("Indice Medio")
elif IMC<22.0 and 2 < edad >= 45:
    print("Indice Medio")
elif IMC>= 22.0 and 2 < edad>=45:
    print("Indice Alto")
else:
    print("Datos incorrectos")
