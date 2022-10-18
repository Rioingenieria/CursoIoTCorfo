archivo=open('quijote.txt')
contador=0
contadorPalabra = 0
contadorLineas = 0
for linea in archivo:
   contadorLineas += 1
   contador+=len(linea.strip().replace(' ',''))
   lineas = linea.strip().split(' ')
   for palabra in lineas:
      contadorPalabra += 1
print('El archivo tiene '+str(contador)+' letras')
print('El archivo tiene '+str(contadorPalabra)+' palabras')
print('El archivo tiene '+str(contadorLineas)+' lineas.')