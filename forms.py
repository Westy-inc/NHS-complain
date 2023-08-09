from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField,PasswordField
from wtforms.validators import DataRequired,InputRequired,ValidationError
from app import User

class AddTaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class deleteTaskForm(FlaskForm):
    submit = SubmitField("delete?")

class NewUserForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()],min_length=3, max_length=20,render_kw={'placeholder': 'username'}) 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists.')

    password = PasswordField('password', validators=[InputRequired()], min_length=8, max_length=20,render_kw={'placeholder': 'password'}) 
    email = StringField('email', validators=[InputRequired()])
    submit = SubmitField('register')