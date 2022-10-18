def producto_interno(a,b):
    if len(a) == len(b):
        n=len(a)
        resu=0
        for i in range(n):
            resu+=a[i]*b[i]
        print(resu)

producto_interno([7,1,4,9,8],range(5))