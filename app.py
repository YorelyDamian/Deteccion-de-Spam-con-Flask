from flask import Flask, render_template
from flask_mysqldb import MySQL
import pandas as pd
import matplotlib.pyplot as plt

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


@app.route('/grafica')
def grafica():
    cur = conexion.connection.cursor()
    curs = conexion.connection.cursor()
    cur.execute(
        "SELECT ROUND((((SELECT COUNT(*) FROM prueba WHERE class='anomaly')*100)/count(*)),2)FROM prueba ;")
    curs.execute(
        "SELECT ROUND((((SELECT COUNT(*) FROM prueba WHERE class='normal')*100)/count(*)),2)FROM prueba ;")
    data = cur.fetchall()
    data = curs.fetchall()
    return render_template('index.html', spam=data, normal=data)


if __name__ == '__main__':
    app.run()
