i=int(1)
n=int(input('ingrese n: '))
mayor=int(0)
while i <= n:
    nro = int(input('ingrese nro: '))
    if nro > mayor:
        mayor = nro
    i +=1
print(mayor)


