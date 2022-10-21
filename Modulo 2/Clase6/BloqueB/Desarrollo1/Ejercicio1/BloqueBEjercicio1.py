def promedio(notas):
    suma = 0
    total = len(notas)
    for nota in notas:
        suma += nota
    return suma/total

lineas = open("notas.txt")
reporte = open("reporte.txt","w")
for linea in lineas:
    spliteo = linea.strip().split(":")
    notas_lista = list(map(float,spliteo[2:]))
    nombre = spliteo[0]
    if promedio(notas_lista) >= 4:
        reporte.write("{} aprobado\n".format(nombre))
    else:
        reporte.write("{} reprobado\n".format(nombre))

lineas.close()
reporte.close()
