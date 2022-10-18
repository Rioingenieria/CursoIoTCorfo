def ec2grado(a,b,c):
    d=(b ** 2) - 4*a*c
    if d<0:
        print("No tiene solución real")
    if d ==0:
        print("Tiene solución única")
        x = -b/(2*a)
    if d>0:
        print("Tiene 2 soluciones")
        x1=(-b+((b ** 2)-4*a*c) ** 0.5)/2*a
        x2=(-b-((b ** 2)-4*a*c) ** 0.5)/2*a
        print(("Las soluciones son {} y {}").format(x1,x2))
    
ec2grado(2,5,2.5)
    