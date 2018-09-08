from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


# Class for the table that manages users,
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    pass_key = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))






class Category(db.Model):
    __tablename__= 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    pitch_cat = db.Column(db.Integer, db.ForeignKey('pitches.id'))



class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    user_id = db.relationship('User', backref='pitch', lazy="dynamic")
    category_id = db.relationship('Category', backref='pitch', lazy="dynamic")



    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitchs(cls, id):
        pitches = Pitches.query.filter_by(movie_id=id).all()
        return pitches


class Comments(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String)


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comments.query.filter_by(movie_id=id).all()
        return comments

