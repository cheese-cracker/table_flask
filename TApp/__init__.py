from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

appv = Flask(__name__)
appv.config.from_object(Config)
appv.config['UPLOAD_FOLDER'] = 'TApp/upload_files'
bootstrap = Bootstrap(appv)

from TApp import routes
