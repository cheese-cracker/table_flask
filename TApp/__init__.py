from flask import Flask
from config import Config

appv = Flask(__name__)
appv.config.from_object(Config)

from TApp import routes
