from flask import render_template,request,redirect,url_for,abort,flash
from . import main


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

@main.route('/profile/')
def profile():
    '''
    View the profile page of a user
    '''

    return render_template('')

