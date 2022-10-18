temp = {
	'Vina del mar': (9, 26), 
	'Valparaiso': (10, 24), 
	'Quilpue': (7, 30), 
	'Quintero': (4, 22)
}

archivo = open("reporte.txt","w")
for i in temp:
	text = ("{} : max {}, min {} \n").format(i,temp[i][1],temp[i][0])
	#print(("{} : max {}, min {}").format(i,temp[i][1],temp[i][0]))
	archivo.write(text)
archivo.close()
