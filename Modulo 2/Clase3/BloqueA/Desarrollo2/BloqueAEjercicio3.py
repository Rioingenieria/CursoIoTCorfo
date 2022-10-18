'''
Cree un módulo llamado "mimodulo.py" y agregue la función invertir_digitos(n)
que reciba un número entero n, y entregue como resultado el número n, con
los dígitos en orden inverso.

Luego desarrolle un programa principal que use la función de dicho módulo.
'''

from mimodulo import invertir_digitos

n = int(input("Ingrese el número a invertir: "))
invertido = invertir_digitos(n)
print("El número invertido es: ", invertido)