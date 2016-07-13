from flask import Flask
from flask_json import FlaskJSON
import * from views

app = Flask(__name__)
json = FlaskJSON(app)
