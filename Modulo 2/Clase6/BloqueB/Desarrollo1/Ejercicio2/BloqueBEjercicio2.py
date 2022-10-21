pacientes = open("pacientes.csv")
jovenes = open("jovenes.txt","w")
mayores = open("mayores.txt","w")

for linea in pacientes:
    spliteo = linea.strip().split(";")
    edad = int(spliteo[2])
    if edad < 30:
        jovenes.write(linea)
    elif edad > 60:
        mayores.write(linea)

pacientes.close()
jovenes.close()
mayores.close()
