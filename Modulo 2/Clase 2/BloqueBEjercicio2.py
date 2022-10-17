i=int(1)
n=int(input('ingrese cantidad datos: '))
mayor=int(0)
menor=int(10000)
while i <= n:
    nro = int(input('ingrese nro: '))
    if nro > mayor:
        mayor = nro
    if nro < menor:
        menor = nro
    i +=1
rango = mayor-menor
print(rango)