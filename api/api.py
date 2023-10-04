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
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/get-water", methods=['GET'])
def water():

    firstDate = request.args.get('firstDate')
    endDate = request.args.get('endDate')

    where = ""
    if firstDate and endDate:
        where = f"where t.date between '{firstDate}' and '{endDate} 23:59:59.999'"

    print(firstDate, endDate)

    SQL_QUERY = f"""
    SELECT * from temperatures_eau as t
    {where}
    order by date ASC
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

    firstDate = request.args.get('firstDate')
    endDate = request.args.get('endDate')

    where = ""
    if firstDate and endDate:
        where = f"where t.date between '{firstDate}' and '{endDate} 23:59:59.999'"

    print(firstDate, endDate)

    SQL_QUERY = f"""
    SELECT * from temperatures_server as t
    {where}
    order by date ASC
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append({"temp_cpu_max": r[0],
                    "date": r[1],
                    "temp_cpu_avg": r[2],
                    "temp_gpu": r[3],
                    "cons_cpu_total": r[4],
                    "cons_cpu_memory": r[5],
                    "cons_cpu_core": r[6],
                    "cons_total": r[7],
                    "cons_gpu": r[8],
                    "cons_cpu_package": r[9],
                    }
                   )

    return tab


@app.route("/get-air", methods=['GET'])
def air():

    firstDate = request.args.get('firstDate')
    endDate = request.args.get('endDate')

    where = ""
    if firstDate and endDate:
        where = f"where t.date between '{firstDate}' and '{endDate} 23:59:59.999'"

    print(firstDate, endDate)

    SQL_QUERY = f"""
    SELECT * from temperatures_air as t
    {where}
    order by date ASC
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
    temp_cpu_max = request.form['temp_cpu_max']
    temp_cpu_avg = request.form['temp_cpu_avg']
    temp_gpu = request.form['temp_gpu']
    cons_cpu_total = request.form['cons_cpu_total']
    cons_cpu_memory = request.form['cons_cpu_memory']
    cons_cpu_core = request.form['cons_cpu_core']
    cons_total = request.form['cons_total']
    cons_gpu = request.form['const_gpu']
    cons_cpu_package = request.form['cons_cpu_package']
    SQL_QUERY = f"""
    USE [workshop2023]
    INSERT INTO temperatures_server
        ([temp_cpu_max]
           ,[date]
           ,[temp_cpu_avg]
           ,[temp_gpu]
           ,[cons_cpu_total]
           ,[cons_cpu_memory]
           ,[cons_cpu_core]
           ,[cons_total]
           ,[cons_gpu]
           ,[cons_cpu_package])
     VALUES
           ({temp_cpu_max}
           ,GETDATE()
           ,{temp_cpu_avg}
           ,{temp_gpu}
           ,{cons_cpu_total}
           ,{cons_cpu_memory}
           ,{cons_cpu_core}
           ,{cons_total}
           ,{cons_gpu}
           ,{cons_cpu_package}
           )        
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
