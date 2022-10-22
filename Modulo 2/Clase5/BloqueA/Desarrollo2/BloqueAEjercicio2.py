resultados = {
    ('Honduras', 'Chile'): (0, 1),
    ('Espana', 'Suiza'): (0, 1),
    ('Suiza', 'Chile'): (0, 1),
    ('Espana', 'Honduras'): (3, 0),
    ('Suiza', 'Honduras'): (0, 0),
    ('Espana', 'Chile'): (2, 1)
}


def goles_anotados(equipo, resultados):
    suma = 0
    for llave in resultados:
        eq1, eq2 = llave
        g1, g2 = resultados[llave]
        if equipo == eq1:
            suma += g1
        if equipo == eq2:
            suma += g2
    return suma


def posiciones(resultados):
    final = []
    equipos = obtener_lista_equipos(resultados)
    for e in equipos:
        puntos = calcular_puntos(e, resultados)
        dif_goles = calcular_diferencia_de_goles(e, resultados)
        goles = goles_anotados(e, resultados)
        final.append((puntos, dif_goles, goles, e))
    final.sort()
    final.reverse()
    lista = []
    for c in final:
        lista.append(c[-1])
    return lista


def calcular_diferencia_de_goles(equipo, resultados):
    favor = 0
    contra = 0
    for llave in resultados:
        eq1, eq2 = llave
        g1, g2 = resultados[llave]
        if equipo == eq1:
            favor += g1
            contra += g2
        if equipo == eq2:
            favor += g2
            contra += g1
    return favor - contra

def calcular_puntos(equipo, resultados):
    puntos = 0

    for paises in resultados:
        equipos = []
        resultados2 = []
        for pais in paises:
            equipos.append(pais)
        for marcador in resultados[paises]:
            resultados2.append(marcador)
        if equipo in equipos:
            if equipos.index(equipo) == 0:
                if resultados2[0] > resultados2[1]:
                    puntos += 3
                elif resultados2[0] == resultados2[1]:
                    puntos += 1
            if equipos.index(equipo) == 1:
                if resultados2[0] < resultados2[1]:
                    puntos += 3
                elif resultados2[0] == resultados2[1]:
                    puntos += 1
    return puntos

def obtener_lista_equipos(resultados):
    final = []
    for equipos in resultados:
        for equipo in equipos:
            if equipo not in final:
                final.append(equipo)
    return final
