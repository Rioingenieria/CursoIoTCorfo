'''
El diccionario de paises asocia cada persona con el país que ha visitado

Escriba una función cuantos_en_comun(a,b), que indique cuántos países en
común han visitado la persona a y la persona b.

'''

def cuantos_en_comun(a, b):
    interseccion = paises[a] & paises[b]
    return interseccion

paises = {'Juan': {'Chile', 'Argentina'},
          'Pedro': {'Francia', 'Suiza', 'Chile'},
          'Diego': {'Chile', 'Italia', 'Francia', 'Peru'}}

a = input("Ingrese nombre 1: ")
b = input("Ingrese nombre 2: ")
print (len(cuantos_en_comun(a, b)))