from crypt import methods
from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = " "

app.config('MYSQL_HOST') == "localhost"
app.config('MYSQL_USER') == "root"
app.config('MYSQL_PASSWORD') == "edureka123"
app.config('MYSQL_DB') == "data"

db = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/app/api/data/all', methods=['GET'])
def show():
    cursor = db.connection.cursor(MySQLdb.cursor.DictCursor)
    cursor.execute("SELECT * FROM dataa")
    info = cursor.fetchall()

    return jsonify(info)
