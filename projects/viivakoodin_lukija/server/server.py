import mysql.connector as mariadb
from flask import Flask,request
import json

mariadb_connection = mariadb.connect(user="USERNAME", password="PASSWORD", database="viivakoodit")
mariadb_connection.autocommit=True
cursor = mariadb_connection.cursor()
app = Flask(__name__)


@app.route("/")
def index():
    lhtml=""
    cursor.execute("SELECT * FROM tuotteet")
    l=list(cursor)
    print(l)
    l=sorted(l,key=lambda x:x[1].lower())
    for i in l:
        print(i)
        #if i[3]!=0:
        lhtml+="<li>"+i[1]+"</li>"
        #else:
         #   lhtml+="<li><font color=red>"+i[1]+": "+str(i[3])+"</font></li>"
    page="""<html>
    <body>
        <center>
            <h1>Tuotteet:</h1>
            <ul>
            """+lhtml+"""
            </ul>
        </center>
    </body>

    </html>
    """
    return page
@app.route("/add")
def add():
    try:
        koodi=request.args.get("koodi")
        nimi=request.args.get("nimi")
        hinta=request.args.get("hinta")
        print(koodi,nimi,hinta)

        cursor.execute("INSERT INTO tuotteet VALUES (%s,%s,%s,%s);",(koodi,nimi,hinta,1))
        
        mariadb_connection.commit()
        return json.dumps({"status":"ok"})
    except Exception as e:
        print(e)
        return json.dumps({"status":"error","exception":str(e)})
@app.route("/get")
def get():
    try:
        koodi=request.args.get("koodi")

        cursor.execute("SELECT * FROM tuotteet WHERE koodi=%s",(koodi,))
        res=list(cursor)
        assert len(res)==1
        res=res[0]
        return json.dumps({"status":"ok","found":"true","koodi":res[0],"nimi":res[1],"hinta":res[2],"lkm":res[3]})
    except AssertionError as e:
        return json.dumps({"status":"error","found":"false"})
@app.route("/take")
def take():
    try:
        koodi=request.args.get("koodi")

        cursor.execute("SELECT * FROM tuotteet WHERE koodi=%s",(koodi,))
        res=list(cursor)
        assert len(res)==1
        res=res[0]
        lkm=res[3]
        cursor.execute("UPDATE tuotteet SET ostettu=%s WHERE koodi=%s",(lkm-1,koodi,))
        mariadb_connection.commit()
        return json.dumps({"status":"ok","found":"true"})
    except Exception as e:
        print(e)
        return json.dumps({"status":"error","found":"false"})

app.run("0.0.0.0",port=80)
