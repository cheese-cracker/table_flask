import os
# os.environ["FLASK_APP"] = "table_flask"
os.environ["FLASK_DEBUG"] = "1"


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cool-uncrackable-****'
