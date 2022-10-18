palabra1 = input("ingrese palabra 1: ")
palabra2 = input("ingrese palabra 2: ")
a = len(palabra1)
b = len(palabra2)
if a > b:
    print("palabra 1 es mayor a palabra 2")
elif a == b:
    print("ambas palabras tienen el mismo largo")
else:
    print("palabra 2 es mayor a palabra 1")