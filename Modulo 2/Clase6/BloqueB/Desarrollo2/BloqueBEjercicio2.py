archivoPacientes=open('pacientes.csv')
archivoJovenes=open('jovenes.txt','w')
archivoMayores=open('mayores.txt','w')
for linea in archivoPacientes:
    valores = linea.strip().split(';')
    edad=int(valores[2])
    if edad<30:
        archivoJovenes.write('{};{};{}\n'.format(valores[0],valores[1],valores[2]))
    elif edad>60:
        archivoMayores.write('{};{};{}\n'.format(valores[0], valores[1], valores[2]))
archivoJovenes.close()
archivoMayores.close()
archivoPacientes.close()