def desviacion_estandar(valores):
    sigma_2 = 0
    valores_base=[]
    n = len(valores)
    x_prom=sum(valores)/len(valores)
    for i in range(n):
        sigma_2+=((valores[i]-x_prom) ** 2)/(n-1)
        valores_base.append((valores[i]-x_prom) ** 2)
    sigma = sigma_2 ** 0.5
    print(x_prom)
    print(valores_base)
    print(sum(valores_base))
    print(sigma)

desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0])

