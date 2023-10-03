# TO INSTALL pip install pypyodbc
# TO INSTALL pip install flask
# TO INSTALL pip install flask_cors

from flask import Flask, render_template, request
from flask_cors import CORS
import pypyodbc as pyodbc

SERVER = 'PORTABLE_MATTHI'
DATABASE = 'workshop2023'
USERNAME = 'python'
PASSWORD = 'python'

connectionString = f'DRIVER=SQL SERVER;SERVER={SERVER};DATABASE={DATABASE};Trust_Connection=yes;'

conn = pyodbc.connect(connectionString)


app = Flask(__name__)
CORS(app)


@app.route("/get-water", methods=['GET'])
def water():
    SQL_QUERY = """
    SELECT * from temperatures_eau order by date ASC
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append({"temp": r[0], "date": r[1] })

    return tab


@app.route("/get-server", methods=['GET'])
def pc():
    SQL_QUERY = """
    SELECT * from temperatures_server order by date ASC
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append({"temp": r[0], "date": r[1], "consomation": r[2] })

    return tab


@app.route("/get-air", methods=['GET'])
def air():
    SQL_QUERY = """
    SELECT * from temperatures_air order by date ASC
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append({"temp": r[0], "date": r[1] })

    return tab

@app.route("/set-water", methods=['POST'])
def postWater():
    temp = request.form['temp']
    SQL_QUERY = f"""
    USE [workshop2023]
    INSERT INTO temperatures_eau
           ([temp]
           ,[date])
     VALUES
           ({temp}
           ,GETDATE())
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    cursor.commit()

    return "Ok"

@app.route("/set-server", methods=['POST'])
def postServer():
    temp = request.form['temp']
    SQL_QUERY = f"""
    USE [workshop2023]
    INSERT INTO temperatures_server
           ([temp]
           ,[date])
     VALUES
           ({temp}
           ,GETDATE())        
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    cursor.commit()

    return "Ok"

@app.route("/set-air", methods=['POST'])
def postAir():
    temp = request.form['temp']
    SQL_QUERY = f"""
    USE [workshop2023]
    INSERT INTO temperatures_air
           ([temp]
           ,[date])
     VALUES
           ({temp}
           ,GETDATE())
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    cursor.commit()

    return "Ok"


if __name__ == "__main__":
    app.debug = True
    app.run()
