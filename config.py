import os
# os.environ["FLASK_APP"] = "table_flask"


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cool-uncrackable-****'
