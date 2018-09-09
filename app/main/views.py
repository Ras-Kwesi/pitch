from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments,Category,Pitches
from .. import db,photos
from .forms import UpdateProfile ,NewPitch, NewComment
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



@main.route('/pitch/add', methods = ['GET','POST'])
def new_pitch():
    '''
    View function to create a new pitch
    '''
    form = NewPitch()
    if form.validate_on_submit():
        new_pitch = (Pitches(title = form.title.data,
                             pitch = form.pitch.data,), 'Category(category = form.category.data)')
        # new_category =
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title = "I have a Pitch"

    return render_template('new_pitch.html', title = title, pitch_form = form)


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

    comment_form = NewComment()
    if comment_form.validate_on_submit():
        new_comment = Comments(comment=comment_form.comment.data)



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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))