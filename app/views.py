from app import app

@app.route('/')
@app.route('/index')
def index():
    """ Index function
    management of roting to home and index pages"""
    return "<br>Hello world!"