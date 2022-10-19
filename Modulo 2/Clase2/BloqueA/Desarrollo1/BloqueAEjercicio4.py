suma = 0
while True:
    tiempo = int(input("cuanto demoraste en el tramo: "))
    if tiempo == 0:
        break
    else:
        suma += tiempo

h = suma // 60
m = suma % 60
print("el tiempo total:", str(h) + ":" + str(m))
