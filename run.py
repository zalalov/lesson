
import os

from app import create_app, db

config_name = os.getenv('FLASK_CONFIG') or 'development'
app = create_app(config_name)

from views import *


if __name__ == '__main__':
    app.run()