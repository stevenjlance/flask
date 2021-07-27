# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return "hello is this working?"


@app.route('/steven')
def steven():
    return "this is steven's code"
  
@app.route('/about')
def about():
    return "working on this rn"

