from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments,Category,Pitches
from .. import db
from .forms import ReviewForm,UpdateProfile
from flask_login import login_user,logout_user,login_required


# Views for our templates
@main.route('/')
def index():
    '''
    View function to render the index html template
    '''



    return render_template('index.html',)


@main.route('/category/')
def categories(category):
    '''
    view function to display the pitches of our specific category
    '''



    return render_template('')


@main.route('/pitch/')
def pitch():
    '''
    View function to view a pitch
    '''

    return render_template('')



@main.route('/pitch/add/')
def new_pitch():
    '''
    View function to create a new pitch
    '''



    return render_template("")


@main.route('/comments/')
def comments():
    '''
    View function to display comments to a pitch
    '''

    return render_template('')

@main.route('/comments/new/')
def new_comments():
    '''
    View function to create a new comment to a pitch
    '''

    return render_template('')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

