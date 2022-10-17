sueldo=float((input("Ingrese su sueldo: ")))
if sueldo < 1000:
    print(("Usted pagará {} de impuesto").format(sueldo*0))
elif 1000<sueldo<2000:
    print(("Usted pagará {} de impuesto").format(sueldo*0.05))
elif 2000<sueldo<4000:
    print(("Usted pagará {} de impuesto").format(sueldo*0.1))
elif 4000<sueldo:
    print(("Usted pagará {} de impuesto").format(sueldo*0.12))
else:
    print("Datos erroneos")
    