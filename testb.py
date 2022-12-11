import pandas as pd
import json

df = pd.read_excel(open('static/data/CND.xlsx', 'rb'),sheet_name='equipos')
print(df)

file = []
grupos = []
items = []
grupo1 = ""
grupo2 = ""
grupo3 = ""
grupo = 0
grupo1id = ""
grupo2id = ""
grupo3id = ""

dict = {'id':0,'parent':"#","text":"<span id='ltitle' style='color:grey'>Proyecto: </span><span id='title' style='color:black;font-weight:bold'>CND</span><span id='lqty' style='color:grey'> &nbsp;| cantidad: </span><span id='qty' style='color:black;font-weight:bold'>1</span><span id='lsup' style='color:grey'>&nbsp;| m2: </span><span id='sup' style='color:black;font-weight:bold'></span>"}
file.append(dict)
for i in range(len(df)):
    if str(df.loc[i][0]) != grupo1:
        grupos.append(str(df.loc[i][0]))
        grupo1 = str(df.loc[i][0])
        grupo = grupo+1
        grupo1id = grupo
        dict = {'id':grupo,'parent':0,"text":"<span id='ltitle' style='color:grey'>Grupo: </span><span id='title' style='color:black;font-weight:bold'>"+str(df.loc[i][0])+"</span><span id='lqty' style='color:grey'> &nbsp;| cantidad: </span><span id='qty' style='color:black;font-weight:bold'>1</span><span id='lsup' style='color:grey'>&nbsp;| m2: </span><span id='sup' style='color:black;font-weight:bold'></span>"}
        file.append(dict)
    if str(df.loc[i][1]) != grupo2:
        grupos.append(str(df.loc[i][1]))
        grupo2 = str(df.loc[i][1])
        grupo = grupo+1
        grupo2id = grupo
        dict = {'id':grupo,'parent':grupo1id,"text":"<span id='ltitle' style='color:grey'>Grupo: </span><span id='title' style='color:black;font-weight:bold'>"+str(df.loc[i][1])+"</span><span id='lqty' style='color:grey'> &nbsp;| cantidad: </span><span id='qty' style='color:black;font-weight:bold'>1</span><span id='lsup' style='color:grey'>&nbsp;| m2: </span><span id='sup' style='color:black;font-weight:bold'></span>"}
        file.append(dict)
    if str(df.loc[i][2]) != grupo3:
        grupos.append(str(df.loc[i][2]))
        grupo3 = str(df.loc[i][2])
        grupo = grupo+1
        grupo3id = grupo
        dict = {'id':grupo,'parent':grupo2id,"text":"<span id='ltitle' style='color:grey'>Grupo: </span><span id='title' style='color:black;font-weight:bold'>"+str(df.loc[i][2])+"</span><span id='lqty' style='color:grey'> &nbsp;| cantidad: </span><span id='qty' style='color:black;font-weight:bold'>1</span><span id='lsup' style='color:grey'>&nbsp;| m2: </span><span id='sup' style='color:black;font-weight:bold'>"+str(df.iloc[i][9])+"</span>"}
        file.append(dict)
    grupo = grupo+1
    dict = {'id':grupo,'parent':grupo3id,"text":"<span id='ltitle' style='color:grey'>Artículo: </span><span id='title' style='color:black;font-weight:bold'>"+str(df.iloc[i][8])+"</span><span id='lqty' style='color:grey'> &nbsp;| cantidad: </span><span id='qty' style='color:black;font-weight:bold'>"+str(df.iloc[i][10])+"</span><span id='lsup' style='color:grey'>&nbsp;| Tipo: </span><span id='sup' style='color:black;font-weight:bold'></span>"}
    file.append(dict)

print(file)

with open("static/json/cndb.json", "w") as outfile:
    json.dump(file, outfile)