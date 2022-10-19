numero = int(input("ingresa un numero: "))
while numero != 1:
    if numero % 2 == 0:
        numero = (numero // 2)
    elif numero % 2 != 0:
        numero = (numero * 3) + 1
    print(numero)
