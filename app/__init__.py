# Init package
from flask import Flask

app = Flask(__name__)
from app import views

def version():
    """Return version number"""
    return '0.0.1'