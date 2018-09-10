from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo

from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,RadioField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class NewPitch(FlaskForm):
    title = StringField('Title :',validators=[Required()])
    pitch = TextAreaField('New Pitch',validators=[Required()])
    category = StringField('Category :',validators=[Required()])    #RadioField('Pick Category',choices=[('Pick-Up Lines', 'Pick-Up Lines'),('Interview Pitch', 'Interview Pitch'),('Product Pitch', 'Product Pitch'),('Promotion Pitch','Promotion Pitch')],validators=[Required()])
    submit = SubmitField('Submit', validators=[Required()])


class NewComment(FlaskForm):
    name = StringField('Name :',validators=[Required()])
    comment = TextAreaField('Comment.',validators = [Required()])
    submit = SubmitField('Submit', validators=[Required()])