def promedio(notas):
    suma = 0
    total = len(notas)
    for nota in notas:
        suma += nota
    return suma/total

lineas = open("notas.txt")
reporte = open("reporte.txt", "w")
for linea in lineas:
    notas = []
    spliteo = linea.strip().split(":")
    for i in spliteo[2:]:
        notas.append(float(i))
    nombre = spliteo[0]
    if promedio(notas) >= 4:
        reporte.write("{} aprobado\n".format(nombre))
    else:
        reporte.write("{} reprobado\n".format(nombre))

lineas.close()
reporte.close()
