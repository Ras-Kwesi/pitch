from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User,Pitches,Category,Comments
# from .forms import
from .. import db
from flask_login import login_user,logout_user,login_required


@auth.route('/login')
def login():
    return render_template('auth/login.html')