from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Y121200gm'
app.config['MYSQL_DB'] = 'machineglearning'
conexion = MySQL(app)


@app.route('/')
def index():
    cur = conexion.connection.cursor()
    cur.execute(
        "SELECT id, duration, protocol_type, service, flag, src_bytes, class FROM prueba WHERE class = 'anomaly' LIMIT 10")
    data = cur.fetchall()
    return render_template('index.html', correos=data)


@app.route('/conexion')
def bd():
    #cursor = conexion.connection.cursor()
    #sql = "SELECT id, duration, protocol_type, service, flag, src_bytes, class FROM prueba WHERE class = 'anomaly' LIMIT 10"
    # cursor.execute(sql)
    #datos = cursor.fetchall()
    # print(datos)
    try:
        return "Datos Listos"
    except Exception as ex:
        return "Error"


@app.route('/grafica')
def grafica():

    return render_template('grafica.py')


if __name__ == '__main__':
    app.run()
