from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    # Fake user definition
    user = {'nickname': 'Fabio'} #Fake user management
    # Fake data for user
    terraces = [
        {
            'mgtuser': {'nickname': 'Fabio'},
            'terrace': 'Upper terrace'
        },
        {
            'mgtuser': {'nickname': 'Fabio'},
            'terrace': 'Ground terrace'
        },
        {
            'mgtuser': {'nickname': 'Silvia'},
            'terrace': 'Ground terrace'
        }
    ]
    # Return rendered template
    return render_template( 'index.html',
                title='Home',
                user=user,
                terraces=terraces
                )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for openid=%s , remeber_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template( 'login.html',
                title='Sign in',
                form=form,
                providers=app.config['OPENID_PROVIDERS'])

