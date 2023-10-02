# TO INSTALL pip install pyodbc
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

SQL_QUERY = """
SELECT * from temperatures_eau
"""


app = Flask(__name__)
CORS(app)


@app.route("/get-water", methods=['GET'])
def water():
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append(r)
    return tab


@app.route("/get-pc", methods=['GET'])
def pc():
    return "dqhsbdhu"


@app.route("/get-air", methods=['GET'])
def air():
    return "dqhsbdhu"


if __name__ == "__main__":
    app.debug = True
    app.run()
