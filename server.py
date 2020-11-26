from flask import Flask,render_template, request, session, Response, redirect
#from database import connector
#from model import entities
import json
import time
from query import query

#db = connector.Manager()
#engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/search/<content>', methods = ['GET'])
def search(content):
    data = query(content)
    print(content)
    return Response(data, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
