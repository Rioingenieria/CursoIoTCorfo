from random import randint
clave = ""

while len(clave)<4:
        numero = randint(1,9999)
        menor = 11
        for digito in str(numero):
            if int(digito) <= menor:
                menor = int(digito)
        if menor % 2 == 0:
            clave += digito
print("Su clave aleatoria es: {}".format(clave))
