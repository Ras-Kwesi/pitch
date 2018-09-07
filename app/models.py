from . import db



# Class for the table that manages users,
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True
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


class Comments(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String)
