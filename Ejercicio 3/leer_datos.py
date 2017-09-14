import time

#while 1:
	#time.sleep(3)
def leer_datos():
	with open('datos.txt','r') as file:
		while 1:
		#with open('datos.txt','r') as file:
			linea=file.readline()
			while(linea):
				time.sleep(3)
				datos=linea.split("/")
				temp=datos[0]
				hum=datos[1]
				pres=datos[2]
				viento=datos[3]
				print("temp: {}, hum: {}, pres: {}, viento: {} ".format(temp,hum,pres,viento))
				linea=file.readline()
		
