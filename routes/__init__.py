__author__ = 'karnikamit'
from flask import Flask
import os
app_route = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
app = Flask(__name__, template_folder=app_route+'/templates')
from routes import baseroutes

