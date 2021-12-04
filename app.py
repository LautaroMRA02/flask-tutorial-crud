from flask import Flask
from flask import render_template,request

from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='cac_actividad_empleados'
mysql.init_app(app)




@app.route('/')
def index():
	sql = ""
	conn = mysql.connect()
	cursor = conn.cursor()
	# cursor.execute(sql)
	conn.commit()
	return render_template('empleados/index.html') 

@app.route('/create')
def create():
 return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
	sql = "INSERT INTO `sistema`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Juan Pablo', 'juanpablo@gmail.com', 'juanpablo.jpg');"

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	return render_template('empleados/index.htm')

if __name__ == '__main__':
	app.run(debug=True)
