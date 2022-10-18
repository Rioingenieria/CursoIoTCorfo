productos = [
    #(id_producto, nombre, precio, cantidad_bodega)
    (41419, 'Fideos', 450, 210),
    (70717, 'Cuaderno', 900, 119),
    (78714, 'Jabon', 730, 708),
    (30877, 'Desodorante', 2190, 79),
    (47470, 'Yogur', 99, 832),
    (50809, 'Palta', 500, 55),
    (75466, 'Galletas', 235, 0),
    (33692, 'Bebida', 700, 20),
    (89148, 'Arroz', 900, 121),
    (66194, 'Lapiz', 120, 900),
    (15982, 'Vuvuzela', 12990, 40),
    (41235, 'Chocolate', 3099, 48),
]

clientes = [
    #(rut, nombre)
    ('11652624-7', 'Juan Perez'),
    ('8830268-0', 'Sebastian Casanueva'),
    ('7547896-8', 'Victor Gamonal'),
]

ventas = [
    #(num_boleta, fecha_venta, rut_cliente)
    (1, (2010, 9, 12), '8830268-0'),
    (2, (2010, 9, 19), '11652624-7'),
    (3, (2010, 9, 30), '7547896-8'),
    (4, (2010, 10, 1), '8830268-0'),
    (5, (2010, 10, 13), '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    #(num_boleta, id_producto, cantidad)
    (1, 89148, 3),
    (2, 50809, 4),
    (2, 33692, 2),
    (2, 47470, 6),
    (3, 30877, 1),
    (4, 89148, 1),
    (4, 75466, 2),
    (5, 89148, 2),
    (5, 47470, 10),
    (6, 41419, 2),
]

def producto_mas_caro(lista):
    n=len(lista)
    precios=[]
    for i in range(n):
        precios.append(lista[i][2])
    for i in range(n):
        if lista[i][2] == max(precios):
            print(lista[i][1])

def valor_total_bodega(lista):
    n=len(lista)
    suma=0
    for i in range(n):
        suma+=lista[i][2]*lista[i][3]
    print(suma)

def ingreso_total_por_ventas(lista1, lista2): #itemes,productos
    n1=len(lista1)
    n2=len(lista2)
    ventas=0
    for i in range(n1): #itemes
        for j in range(n2): #productos
            if itemes[i][1] == productos[j][0]:
                ventas+=itemes[i][2]*productos[j][2]
                #print(itemes[i][1], productos[j][1], itemes[i][2], productos[j][2])
    print(ventas)

def masvendido(lista):
    n=len(lista)
    


def producto_con_mas_ingresos(lista1,lista2):
    n1=len(lista1)
    n2=len(lista2)
    produ_ventas=0





#producto_mas_caro(productos)
#valor_total_bodega(productos)
#ingreso_total_por_ventas(itemes,productos)
producto_con_mas_ingresos(itemes, productos)