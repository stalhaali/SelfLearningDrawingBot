from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '71d66b04ce031b343ebcd5879bb7eceb'

from drawingbot import routes
