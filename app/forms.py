from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class LoginForm(Form):
    uname = StringField('uname', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()]) 
    remember_me = BooleanField('remember_me', default=False)

class CreateAccountForm(Form):
    uname = StringField('uname', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class CreatePostForm(Form):
    post_title= StringField('post_title', validators=[DataRequired()])
    post_content = StringField('post_content', widget=TextArea(), validators=[DataRequired()])
