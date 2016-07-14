
from app import app
import datetime
from flask import jsonify

@app.route("/", methods=["GET"])
def index():
    data = {
        "status": "OK",
        "utc-time": str(datetime.datetime.utcnow()),
        "time": str(datetime.datetime.now()),
    }
    return jsonify(data)

def before_request():
    conn = mysql.connect() #Connect a DB

def after_request():
    conn.close() #Closes DB connection

def not_found():
    return flask_json.json_response.jsonify(code = 404, msg = "not found")
