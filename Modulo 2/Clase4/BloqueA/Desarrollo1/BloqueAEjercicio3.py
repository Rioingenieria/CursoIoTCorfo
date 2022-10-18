def producto_interno(a,b):
    if len(a) == len(b):
        n=len(a)
        resu=0
        for i in range(n):
            resu+=a[i]*b[i]
        return resu


def son_ortogonales(a,b):
    if(producto_interno(a,b) == 0):
        print(True)
    else:
        print(False)

son_ortogonales([2,1],[-3,6])