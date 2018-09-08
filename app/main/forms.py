from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo

from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

