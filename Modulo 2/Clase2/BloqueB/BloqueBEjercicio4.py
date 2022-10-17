i = int(1)
n = int(input('ingrese el puntaje: '))
count=0
while i <= 6:
    

    j=int(1)
    while j <= 6:
        #print(i,j)
        total = i+j
        if total == n:
            #print(i,j)
            count+=1
        j+=1
    i+=1
print("Existen {} combinaciones".format(count))