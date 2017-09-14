from flask import Flask, render_template, request
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

# def post():
# 	print "aca Llegamos"
f=10
@app.route('/', methods=['GET','POST'])
def index():
	global f
	if request.form.get('frecform') is not None:
		f = request.form['frecform']
		print "La frecuencia elegida es {}".format(f)
	#time.sleep(float(f))
	temp=[]
	hum=[]
	pres=[]
	viento=[]
	with open('datos.txt','r') as file:
		totalLineas=file.readlines()
		lineas=totalLineas[-10:]
		for item in lineas:
			#time.sleep(3)
			datos=item.split("/")
			temp.append(datos[0])
			hum.append(datos[1])
			pres.append(datos[2])
			viento.append(datos[3])
			linea=file.readline()
		promedioTemp=calcular_promedio(temp)
		promedioHum=calcular_promedio(hum)
		promedioPres=calcular_promedio(pres)
		promedioViento=calcular_promedio(viento)
	return render_template('index.html',temp=temp[len(temp)-1],hum=hum[len(hum)-1],pres=pres[len(hum)-1],viento=viento[len(viento)-1],frec=f,promedioTemp=promedioTemp,promedioHum=promedioHum,promedioPres=promedioPres,promedioViento=promedioViento)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)