from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

appv = Flask(__name__)
appv.config.from_object(Config)
bootstrap = Bootstrap(appv)

from TApp import routes
