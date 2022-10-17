artistas = {
    # nombre: codigo, origen, duracion en minutos de la presentacion)
    'Marco Antonio Solis': (1, 'Estados Unidos', 74),
    'Daddy Yankee': (2, 'Puerto Rico', 70),
    'Myriam Hernandez': (3, 'Chile', 40),
    'Los Charros de Lumaco': (4, 'Chile', 25),
    'Metallica': (5, 'Estados Unidos', 45),
    'U2': (6, 'Irlanda', 80),
    'Justin Bieber': (7, 'Canada', 5),
}

artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1, 4, 3, 6, 2, 5),
    "Martes": (2, 5, 1),
    "Miercoles": (3, 6, 2, 4),
    "Jueves": (2, 5),
}

#dia = input('Ingrese dia: ')
def cantidad_de_artistas(dia):
    n=len(artistas_por_dia[dia])
    return n

def nombre_primer_artista(dia):
    n_art=artistas_por_dia[dia][0]
    for i in artistas:
        if artistas[i][0] == n_art:
            return i

def pais_origen_ultimo(dia):
    n_art=artistas_por_dia[dia][-1]
    for i in artistas:
        if artistas[i][0] == n_art:
            return artistas[i][1]    

def tiempo_total(dia):
    list=[]
    for n in artistas_por_dia:
        list.append(int(artistas_por_dia[dia][n]))
        return list
'''
suma=0
for d, artistas in artistas_por_dia.items():
    if d == dia:
        list_artistas=list(artistas)
        n_artistas=len(list_artistas)
        for artistas, datos in artistas.items():
            print(int(datos[0])) 

            #for i in list_artistas:
                #if i == int(datos[0]):
                    #suma+=int(datos[2])

'''
for artistas, datos in artistas.items():
    print(int(datos[0]))     

'''

#print(artistas_por_dia["Lunes"][1])
#print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
#print('El primer artista del dia sera', nombre_primer_artista(dia))
#print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
#print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')