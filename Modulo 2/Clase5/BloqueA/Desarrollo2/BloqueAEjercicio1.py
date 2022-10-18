def cantidad_de_artistas(dia):
    for dia in artistas_por_dia.values():
        print(len(dia))
        if dia == 'Lunes':

def tiempo_total(dia):
    suma = 0
    codigos = artistas_por_dia[dia]
    for c in codigos:
        for nombre in artistas:
            codigo, _, duracion = artistas[nombre]
            if c == codigo:
                suma += duracion
    return suma

def pais_origen_ultimo(dia):
    codigo = artistas_por_dia[dia][-1]

    for nombre in artistas:
        codigo_a = artistas[nombre][0]
        pais = artistas[nombre][1]
        if codigo == codigo_a:
            return pais


def nombre_primer_artista(dia):
    codigo = artistas_por_dia[dia][0]

    for nombre in artistas:
        codigo_a = artistas[nombre][0]
        if codigo == codigo_a:
            return nombre


artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1, 4, 3, 6, 2, 5),
    "Martes": (2, 5, 1),
    "Miercoles": (3, 6, 2, 4),
    "Jueves": (2, 5),
}

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

dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')