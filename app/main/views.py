from flask import render_template,request,redirect,url_for,abort,flash
from . import main


# Views for our templates
@main.route('/')
def index():
    '''
    View function to render the index html template
    '''

    return render_template('index.html',)
