def codigo_hora(n):
  suma = 0
  for c in n:
        if c != ':':
            suma += int(c)
        else:
            hora = suma % 24
            suma = 0
  minutos = suma % 60
  print('La hora descifrada es:', str(hora) + ':' + str(minutos))
  return 
