import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir


app = Flask(__name__)

# Config application
app.config.from_object('config')

# Get a database
db = SQLAlchemy(app)

# Login management
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models

