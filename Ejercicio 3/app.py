from flask import Flask,render_template
import time
import linecache

app = Flask(__name__)

def calcular_promedio(collection):
	total=0
	col=collection[-10:]
	for item in col:
		total = total + int(item)
	prom=total/len(col)
	return prom

@app.route('/')
def index():
	temp=[]
	hum=[]
	pres=[]
	viento=[]
	with open('datos.txt','r') as file:
		#tamLinea=sizeof(file.readline)
		totalLineas=file.readlines()
		lineas=totalLineas[-10:]
		#print "La cantidad de lineas es {}".format(cantidadLineas)
		# if (cantidadLineas <= 10):
		# 	file.seek(0,0)
		# else:
		# 	linecache.getline(file, 33)
		#while 1:
		#with open('datos.txt','r') as file:
		#linea=file.readline()
		for item in lineas:
			time.sleep(3)
			datos=item.split("/")
			temp.append(datos[0])
			hum.append(datos[1])
			pres.append(datos[2])
			viento.append(datos[3])
			linea=file.readline()
		print temp
		print hum
		print pres
		promedioTemp=calcular_promedio(temp)
		promedioHum=calcular_promedio(hum)
		promedioPres=calcular_promedio(pres)
		promedioViento=calcular_promedio(viento)
	return render_template('index.html',temp=temp[len(temp)-1],hum=hum[len(hum)-1],pres=pres[len(hum)-1],viento=viento[len(viento)-1],frec=3,promedioTemp=promedioTemp,promedioHum=promedioHum,promedioPres=promedioPres,promedioViento=promedioViento)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')