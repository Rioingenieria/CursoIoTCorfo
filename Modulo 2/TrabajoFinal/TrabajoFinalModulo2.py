from random import randrange, random,uniform
from time import sleep

tiempo_total=int(input('Ingrese tiempo total en segundos: '))
tiempo_medicion=int(input('Ingrese tiempo medicion en segundos: '))
temperatura_calefactor=int(input('Ingrese temperatura en grados celsius: '))
temperatura_inicial=0
estado_calefactor=False

i=0

while i<tiempo_total:
    temperatura_inicial = randrange(0, 35, 1)
    if i==0:
        archivo_log = open(
            'log-tempinicial-{}-tempcalefactor_{}-tiempototal_{}-tiempomedicion_{}.csv'.format(temperatura_inicial,
                                                                                               temperatura_calefactor,
                                                                                               tiempo_total,
                                                                                               tiempo_medicion), 'a')
    numero_aleatorio=uniform(0,2)
    temperatura_actual=temperatura_inicial
    if temperatura_inicial<=temperatura_calefactor:
        estado_calefactor=True
        temperatura_actual-=numero_aleatorio
    else:
        temperatura_actual += numero_aleatorio
        estado_calefactor=False
    sleep(tiempo_medicion)
    i+=tiempo_medicion
    temperatura_actual=round(temperatura_actual, 2)

    archivo_log.write(str(temperatura_actual)+';'+str(estado_calefactor)+'\n')
    print('La temperatura actual es '+str(temperatura_actual)+' y el estado es '+str(estado_calefactor))