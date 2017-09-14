import random
import time
#lista_datos=[]

while 1:
	time.sleep(1) #Frecuencia de Muestreo Fija, 1seg.
	temp=random.randint(10,30)
	hum=random.randint(0,100)
	pres=random.randint(4000,5000)
	viento=random.randint(10,100)
	#lista_datos.append(random.uniform(0.1,0.9))

	with open('datos.txt','a') as file:
		file.write("{0}/{1}/{2}/{3}\n".format(temp,hum,pres,viento))
	print("Se escribio una linea")
	#datos.close()


