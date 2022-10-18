sueldo = int(input("ingresa su suedo:"))

if sueldo < 1000:
    impuesto = 0
    print("usted pagara", impuesto, "de impuest")
else:
    if sueldo >= 1000 and sueldo < 2000:
        impuesto = (sueldo * 5) / 100
        print(impuesto)
    elif sueldo >= 2000 and sueldo < 4000:
        impuesto = (sueldo * 10) / 100
        print(impuesto)
    else:
        impuesto = (sueldo * 12) / 100
        print(impuesto)

