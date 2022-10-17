tem_f = float((input("Temp. En Farenheit: ")))
tem_c = (tem_f-32)*(5/9) 
print(("Los {} F en grados Celsius son {} C").format((round(tem_f,1)),round(tem_c,1)))