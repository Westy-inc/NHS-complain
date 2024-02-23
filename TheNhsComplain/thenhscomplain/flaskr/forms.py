# The code defines several FlaskForm classes for different purposes such as adding tasks, deleting
# tasks, creating new users, logging in users, and collecting user details.
from flask_wtf import FlaskForm 
from wtforms import StringField , SubmitField,PasswordField,BooleanField,TextAreaField,IntegerField,RadioField
from wtforms.validators import DataRequired,InputRequired,ValidationError,Length,Email
from models import User
from wtforms.fields import EmailField


# The `AddTaskForm` class is a form used to add a task with a title, body.
class AddTaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=4, max=20)])
    body = TextAreaField('body', validators=[DataRequired()],render_kw={"rows": 30, "cols": 11,'placeholder': 'put you complaint here please put the name of the hospital,Pharmacy,GP or any other nhs health provider \nplease give as much detail of your complaint here'},)
    submit = SubmitField('Su')

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

class NextForm(FlaskForm):
    submit = SubmitField('next')

class Userdetails(FlaskForm):
    name = StringField('name', validators=[InputRequired("input required"), Length(min=4, max=20)]) 
    surname = StringField('surname', validators=[InputRequired("input required"), Length(min=4, max=20)]) 
    day = IntegerField ('day', validators=[InputRequired("input required")])
    month = IntegerField ('month',  validators=[InputRequired("input required")])
    year = IntegerField ('year', validators=[InputRequired("input required")])
    email =  EmailField('email',validators=[InputRequired("input required")])
    phone = StringField('phone')
    submit = SubmitField('next')