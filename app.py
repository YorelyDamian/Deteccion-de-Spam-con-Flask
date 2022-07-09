from distutils.command.config import config
from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import config


app = Flask(__name__)
conexion = MySQL(app)


@app.route('/conexion')
def bd():
    try:
        return "Datos Listos"
    except Exception as ex:
        return "Error"


@app.route('/')
def index():
    cursor = conexion.connection.cursor()
    sql = "SELECT id, duration, protocol_type, service, flag, src_bytes, class FROM prueba WHERE class = 'anomaly' LIMIT 10"
    cursor.execute(sql)
    datos = cursor.fetchall()
    print(datos)
    return render_template('index.php')


@app.route('/grafica')
def grafica():

    return render_template('grafica.py')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
