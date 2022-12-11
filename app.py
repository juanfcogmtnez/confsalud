from flask import Flask, jsonify, render_template, request, url_for, redirect, session, send_file
from html.parser import HTMLParser
from werkzeug.utils import secure_filename
import os, os.path
from datetime import datetime
import crea
import json
import pandas as pd
import bk
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'despl-ofertas'
app.secret_key = 'esto-es-una-clave-muy-secreta'
#app.register_blueprint(base,url_prefix='-base',template_folder='templates',static_folder='static')
#app.register_blueprint(proyectos,url_prefix='-proyectos',template_folder='templates',static_folder='static')
#app.register_blueprint(unidades,url_prefix='-unidades',template_folder='templates',static_folder='static')
#app.register_blueprint(rooms,url_prefix='-rooms',template_folder='templates',static_folder='static')
#app.register_blueprint(despl,url_prefix='-despl',template_folder='templates',static_folder='static')

@app.route("/")
def hello_world():
	return redirect(url_for('login'))


@app.route("/login", methods=["POST", "GET"])
def login(message=None):
    if message == None:
        message = 'Por favor introduce tus datos'
    if request.method == 'POST':
        print("post")
        email = request.form['email']
        pwd = request.form['password']
        result = crea.checkpwd(email,pwd)
        print("result:",result)
        print(result)
        if result[0] != 'Error':
            session['nombre'] = result[0]
            session['role'] = result[1]
            return redirect(url_for('proyectos',proy='cnd',cons='blanco'))
        else:
            message='Contraseña incorrecta'
    return render_template('login.html', message=message)

@app.route("/todos/<proy>/<cons>", methods=["POST", "GET"])
def proyectos(proy,cons):
    if session['nombre'] != None:
        username = session['nombre']
        return render_template('todos.html',proy=proy,cons=cons,username=username)
    else:
        return render_template('login.html')

@app.route("/titulo", methods=["POST", "GET"])
def titulo():
    titulos = bk.titulos()
    return titulos

@app.route("/cons", methods=["POST", "GET"])
def builds():
    titulos = bk.builds()
    return titulos

@app.route("/template/<id>", methods=["POST", "GET"])
def templateid(id):
    titulos = bk.titulosid(id)
    return titulos

@app.route("/guardatemp", methods=["POST", "GET"])
def guardatemp():
    nombre = request.json["nombre"]
    arc = request.json['file']
    list = []
    for a in arc:
        texto = a['texto']
        texto = texto.replace('"',"'")
        #print(texto)
        a['text'] = texto
        list.append(a)
    #print("list2",list)
    with open('static/json/temp/'+nombre+'.json', 'w') as outfile:    
        outfile.write(json.dumps(arc))
    return  'ok'

@app.route("/guardadef", methods=["POST", "GET"])
def guardadef():
    nombre = request.json["nombre"]
    arc = request.json['file']
    list = []
    for a in arc:
        texto = a['texto']
        texto = texto.replace('"',"'")
        print(texto)
        a['text'] = texto
        list.append(a)
    print("list2",list)
    with open('static/json/'+nombre+'.json', 'w') as outfile:    
        outfile.write(json.dumps(arc))
    return 'ok'

@app.route("/lista", methods=["POST", "GET"])
def lista():
    return send_file('static/datatemp/temp.xlsx')

@app.route("/planeb/<id>", methods=["POST", "GET"])
def planeb(id):
    test = bk.planeb(id)
    print(test)
    if test == 'ok':
        return 'ok'

@app.route("/planabc/<id>", methods=["POST", "GET"])
def planabc(id):
    test = bk.planabc(id)
    print(test)
    if test == 'ok':
        return 'ok'

@app.route("/datatemp/plane/<id>", methods=["POST", "GET"])
def datatempplane(id):
    cont = os.listdir('static/datatemp/')
    print(cont)
    if id+'.xlsx' in cont:
        return 'ok'
    else:
        return 'no'
        

if __name__=='__main__':
    app.run(debug=False,host="0.0.0.0", port=80)
