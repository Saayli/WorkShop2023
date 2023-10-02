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


app = Flask(__name__)
CORS(app)


@app.route("/get-water", methods=['GET'])
def water():
    SQL_QUERY = """
    SELECT * from temperatures_eau
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append(r)
    return tab


@app.route("/get-pc", methods=['GET'])
def pc():
    SQL_QUERY = """
    SELECT * from temperatures_server
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append(r)
    return tab


@app.route("/get-air", methods=['GET'])
def air():
    SQL_QUERY = """
    SELECT * from temperatures_air
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()

    tab = []

    for r in records:
        tab.append(r)
    return tab


if __name__ == "__main__":
    app.debug = True
    app.run()
