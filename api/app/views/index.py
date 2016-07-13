from flask import Flask, request, jsonify
from datetime import datetime
from flask_json import json_response
from flask.ext.mysql import MySQL

app = Flask(__name__)
@app.route('/')
def index():
    if request.method == 'GET': #If the request is GET, return the parameters as a hash
        return flask_json.json_response.jsonify(status = "OK", utc_time = datetime.utcnow(), time = datetime.now())

def before_request():
    conn = mysql.connect() #Connect a DB

def after_request():
    conn.close() #Closes DB connection

def not_found():
    return flask_json.json_response.jsonify(code = 404, msg = "not found")
