a = int(input("ingresa longitud A: "))
b = int(input("ingresa longitud B: "))
c = int(input("ingresa longitud C: "))

s = (a + b + c) / 2
area = (s*(s - a) * (s - b) * (s - c)) ** 0.5
print("el area de un triangulo es:", round(area,2))