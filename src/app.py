from flask import Flask, render_template
from flask_mysqldb import MySQL
import pandas as pd
import matplotlib.pyplot as plt
import io
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

app = Flask(__name__)

url_datos = 'https://raw.githubusercontent.com/YorelyDamian/DatosCSV/main/prueba.csv'
dataset = pd.read_csv(url_datos)

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


@app.route("/prediccion", methods=['POST'])
def prediccion():

    X = dataset[['duration', 'count']]
    Y = dataset['class']

    correos = dataset.groupby('class').size()

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=0)

    modelo_RL = linear_model.LogisticRegression()

    modelo_RL.fit(X_train, y_train)

    y_pred = modelo_RL.predict(X_test)

    p_s = round(metrics.accuracy_score(y_test, y_pred), 3)
    return render_template('index.html', prediccion=f'La predicción es: {p_s}', num_correos=f'{correos}')


@app.route('/grafica')
def grafica():
    cur = conexion.connection.cursor()
    curs = conexion.connection.cursor()
    cur.execute(
        "SELECT ROUND((((SELECT COUNT(*) FROM prueba WHERE class='anomaly')*100)/count(*)),2)FROM prueba ;")
    curs.execute(
        "SELECT ROUND((((SELECT COUNT(*) FROM prueba WHERE class='normal')*100)/count(*)),2)FROM prueba ;")
    dataA = cur.fetchall()
    dataN = curs.fetchall()
    return render_template('index.html', spam=dataA, normal=dataN)


if __name__ == '__main__':
    app.run()
