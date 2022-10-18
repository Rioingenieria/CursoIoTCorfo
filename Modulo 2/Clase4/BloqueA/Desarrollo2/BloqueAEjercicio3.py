'''
Dos listas de números son ortogonales si su producto interno es cero.
Escriba la función son_ortogonales(a,b) que indique si a y b son
ortogonales.
'''

def son_ortogonales(a,b):
    if producto_interno(a,b) == 0:
        return True
