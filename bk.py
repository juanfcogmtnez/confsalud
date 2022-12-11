from stat import FILE_ATTRIBUTE_READONLY
import pandas as pd
import json
import os
import datetime
from datetime import datetime

import pandas as pd
import json
import sqlite3

def titulos():
    cont = os.listdir('static/json/')
    list = []
    for c in cont:
        if '.json' in c:
            list.append(c[0:-5])
    print(list)
    return json.dumps(list)

def builds():
    cont = os.listdir('static/json/temp/')
    list = []
    for c in cont:
        if '.json' in c:
            list.append(c[0:-5])
    print(list)
    return json.dumps(list)

def guardatemp(nombre,file):
    print(nombre)
    text = json.loads(file)
    print(text)
    return 'ok'

def padre(df,ref):
    filtro = df['id'] == ref
    filtrado = df[filtro]
    return filtrado.iloc[0][1]

def ident(df,ref):
    print("busco",ref,"en")
    print(df)
    filtro = df['id'] == ref
    filtrado = df[filtro]
    print("filtrado",filtrado)
    return filtrado.iloc[0][2]


def planeb(id):
    print("estamos en planeb -------------------------------------------------------------------------------------------------------------------")
    print('static/json/temp/'+id+'.json')
    df = pd.read_json('static/json/temp/'+id+'.json',convert_dates=True)
    print("df",df)
    for i in range(len(df)):
        obj = df.iloc[i][2]
        obj = obj.replace('<span id="ltitle" style="color:grey">','')
        obj = obj.replace('</span><span id="title" style="color:black;font-weight:bold">','')
        obj = obj.replace('</span><span id="lqty" style="color:grey">',':')
        obj = obj.replace('&nbsp;|','')
        obj = obj.replace('</span><span id="qty" style="color:black;font-weight:bold">','')
        obj = obj.replace('</span><span id="lsup" style="color:grey">',':')
        obj = obj.replace('</span><span id="sup" style="color:black;font-weight:bold">','')
        obj = obj.replace('</span>','')
        df.iloc[i][2] = obj
    max = 0
    for i in range(len(df)):
        if "Artículo" in str(df.iloc[i][2]):
            print("contiene articulo",str(df.iloc[i][2]))
            lista = []
            valor = str(df.iloc[i][0])
            while "#" not in lista:
                valor = padre(df,valor)
                lista.append(valor)
            if len(lista) > max:
                max = len(lista)
    cols = []
    print("max",max)
    for i in range(max-2):
        print(i)
        cols.append("nivel_"+str(i))
        cols.append("cant_"+str(i))
        cols.append("m2_"+str(i))
    cols.append("articulo")
    cols.append("cantidad")
    cols.append("tipo")
    ndf = pd.DataFrame()
    for i in range(len(df)):
        if "Artículo" in str(df.iloc[i][2]):
            print("contiene articulo")
            lista = []
            valor = str(df.iloc[i][0])
            while "#" not in lista:
                valor = padre(df,valor)
                lista.append(valor)
            lista.pop()
            lista.reverse()
            print("lista",lista)
            
            dict = {}
            columns = 0
            nuevalinea = []
            for x in range(1,len(lista)):
                esto = ident(df,lista[x])
                esto = esto.split(":")
                print("esto",esto)
                nuevalinea.append(esto[1])
                nuevalinea.append(esto[3])
                nuevalinea.append(esto[5])
            articulo = df.iloc[i][2]
            articulo = articulo.split(":")
            nuevalinea.append(articulo[1])
            nuevalinea.append(articulo[3])
            nuevalinea.append(articulo[5])
            print("articulo",articulo)
            print("nuevalinea",nuevalinea)
            test = pd.DataFrame([nuevalinea],columns=cols)
            ndf = pd.concat([ndf, test], ignore_index=True)
            print(ndf)
    ndf.to_excel('static/datatemp/temp.xlsx',sheet_name='Hoja 1',index=False)  
    return 'ok'

def planabc(id):
    print("estamos en planabc -------------------------------------------------------------------------------------------------------------------")
    print('static/json/temp/'+id+'.json')
    df = pd.read_json('static/json/temp/'+id+'.json',convert_dates=True)
    print("df",df)
    for i in range(len(df)):
        obj = df.iloc[i][2]
        obj = obj.replace('<span id="ltitle" style="color:grey">','')
        obj = obj.replace('</span><span id="title" style="color:black;font-weight:bold">','')
        obj = obj.replace('</span><span id="lqty" style="color:grey">',':')
        obj = obj.replace('&nbsp;|','')
        obj = obj.replace('</span><span id="qty" style="color:black;font-weight:bold">','')
        obj = obj.replace('</span><span id="lsup" style="color:grey">',':')
        obj = obj.replace('</span><span id="sup" style="color:black;font-weight:bold">','')
        obj = obj.replace('</span>','')
        df.iloc[i][2] = obj
    max = 0
    for i in range(len(df)):
        if "Artículo" in str(df.iloc[i][2]):
            print("contiene articulo",str(df.iloc[i][2]))
            lista = []
            valor = str(df.iloc[i][0])
            while "#" not in lista:
                valor = padre(df,valor)
                lista.append(valor)
            if len(lista) > max:
                max = len(lista)
    cols = []
    cols.append("articulo")
    cols.append("tipo")
    cols.append("cantidad")
    ndf = pd.DataFrame()
    for i in range(len(df)):
        if "Artículo" in str(df.iloc[i][2]):
            print("contiene articulo")
            nuevalinea = []
            articulo = df.iloc[i][2]
            articulo = articulo.split(":")
            nuevalinea.append(articulo[1])
            nuevalinea.append(articulo[5])
            try:
                cantidad = int(articulo[3])
            except:
                cantidad = 1
            nuevalinea.append(cantidad)
            print("articulo",articulo)
            print("nuevalinea",nuevalinea)
            test = pd.DataFrame([nuevalinea],columns=cols)
            ndf = pd.concat([ndf, test], ignore_index=True)
            print(ndf)
    ndf = ndf.groupby(by=['articulo','tipo']).sum()
    ndf = ndf.sort_values(by='articulo')
    print(ndf)
    ndf.to_excel('static/databc/temp.xlsx',sheet_name='Hoja 1')  
    return 'ok'