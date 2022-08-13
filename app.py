import os
from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import matplotlib.pyplot as plt

app=Flask(__name__)
app.secret_key="xd"
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='stylver2802X'
app.config['MYSQL_DATABASE_DB']='maquinarias'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/picaroca/save', methods=['POST'])
def picaroca_save():
    _ch01 = request.form['ch01']
    _ch02 = request.form['ch02']
    _ch03 = request.form['ch03']
    _ch04 = request.form['ch04']
    _ch05 = request.form['ch05']
    _ch06 = request.form['ch06']
    _ch07 = request.form['ch07']

    _cd01 = request.form['cd01']
    _cd02 = request.form['cd02']
    _cd03 = request.form['cd03']
    _cd04 = request.form['cd04']
    _cd05 = request.form['cd05']
    _cd06 = request.form['cd06']
    _cd07 = request.form['cd07']

    _ct01 = request.form['ct01']
    _ct02 = request.form['ct02']
    _ct03 = request.form['ct03']
    _ct04 = request.form['ct04']
    _ct05 = request.form['ct05']
    _ct06 = request.form['ct06']
    _ct07 = request.form['ct07']

    _ecph = request.form['ecph']
    _ecpd = request.form['ecpd']
    _ecbi = request.form['ecbi']
    _ecbo = request.form['ecbo']
    _obph = request.form['obph']
    _obpd = request.form['obpd']
    _obbi = request.form['obbi']
    _obbo = request.form['obbo']

    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%m%d')
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT idpicaroca FROM `maquinarias`.`picaroca` WHERE idpicaroca = %s",(horaActual))
    conexion.commit()

    

    sql="INSERT INTO `maquinarias`.`picaroca` (`idpicaroca`, `ch01`, `ch02`, `ch03`, `ch04`, `ch05`, `ch06`, `ch07`, `cd01`, `cd02`, `cd03`, `cd04`, `cd05`, `cd06`, `cd07`, `ct01`, `ct02`, `ct03`, `ct04`, `ct05`, `ct06`, `ct07`, `ecph`, `ecpd`, `ecbi`, `ecbo`, `obph`, `obpd`, `obbi`, `obbo`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    datos=(horaActual, _ch01, _ch02, _ch03, _ch04, _ch05, _ch06, _ch07, _cd01, _cd02, _cd03, _cd04, _cd05, _cd06, _cd07, _ct01, _ct02, _ct03, _ct04, _ct05, _ct06, _ct07, _ecph, _ecpd, _ecbi, _ecbo, _obph, _obpd, _obbi, _obbo)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    return redirect('/')



@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')


@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    _usuario = request.form['User']
    _password = request.form['Password']

    if _usuario=="123" and _password =="456":
        session["login"]=True
        session["usuario"]="Administrador"
        return redirect('/admin/maquinas')


@app.route('/admin/cerrar', methods=['POST'])
def admin_login_cerrar():
    session.clear()
    return redirect('/admin/login')


@app.route('/admin/maquinas')
def admin_maquinas():
    if not 'login' in session:
        return redirect('/admin/login')
    conexion1 = mysql.connect()
    cursor1 = conexion1.cursor()
    cursor1.execute("SELECT idpicaroca FROM `maquinarias`.`picaroca`")
    maquinas = cursor1.fetchall()
    conexion1.commit()
    return render_template('admin/maquinas.html', maquinas=maquinas)


@app.route('/admin/picaroca', methods=['POST'])
def admin_picarocas():
    if not 'login' in session:
        return redirect('/admin/login')
    conexion1 = mysql.connect()
    cursor1 = conexion1.cursor()
    cursor1.execute("SELECT idpicaroca FROM `maquinarias`.`picaroca`")
    maquinas = cursor1.fetchall()
    conexion1.commit()
    
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `maquinarias`.`picaroca` WHERE idpicaroca = %s",(request.form['inputid']))
    picarocas = cursor.fetchall()
    conexion.commit()
    return render_template('admin/picaroca.html', picarocas=picarocas, maquinas=maquinas)




if __name__ == '__main__':
    app.run(debug=True)