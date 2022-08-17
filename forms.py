from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, TextAreaField #validators to be used in form
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import IMAGES

#register form
class RegisterForm(FlaskForm):
    name = StringField('Full name', validators=[InputRequired('A full name is required.'), Length(max=100, message='Your name can\'t be more than 100 characters.')])
    username = StringField('Username', validators=[InputRequired('Username is required.'), Length(max=30, message='Your username is too many characters.')])
    password = PasswordField('Password', validators=[InputRequired('A password is required.')])
    image = FileField(validators=[FileAllowed(IMAGES, 'Only images are accepted.')]) #validators --> for only unsupported file

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Username is required.'), Length(max=30, message='Your username is too many characters.')])
    password = PasswordField('Password', validators=[InputRequired('A password is required.')])
    remember = BooleanField('Remember me')

# add the tweet in the post
class TweetForm(FlaskForm):
    text = TextAreaField('Message', validators=[InputRequired('Message is required.')])