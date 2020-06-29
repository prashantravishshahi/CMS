"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config.from_object(Config)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
app.logger.info('CMS App Starts')


Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
