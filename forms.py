from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,InputRequired,ValidationError,Length
from models import User

class AddTaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    submit = SubmitField('Submit')
    public = BooleanField('public?')

class deleteTaskForm(FlaskForm):
    submit = SubmitField("delete?")

class NewUserForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)],render_kw={'placeholder': 'username'}) 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists. try again')
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)],render_kw={'placeholder': 'password'})
    email = StringField('email', validators=[InputRequired()],render_kw={'placeholder': 'email'})
    submit = SubmitField('register')

class LoginUserForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)],render_kw={'placeholder': 'username'}) 
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)],render_kw={'placeholder': 'password'}) 
    submit = SubmitField('login')