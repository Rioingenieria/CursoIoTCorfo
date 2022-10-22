temp = {
    'Vina del mar': (9, 26),
    'Valparaiso': (10, 24),
    'Quilpue': (7, 30),
    'Quintero': (4, 22)
}

archivo = open("reporte.txt","w")
ciudades = []

for item in temp.items():
    ciudad = item[0]
    temp_min = item[1][0]
    temp_max = item[1][1]
    archivo.write("{}: max {}, min {} \n".format(ciudad,temp_min,temp_max))
archivo.close()
