import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user,LoginManager, login_required , logout_user, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
basedir = os.path.abspath(os.path.dirname(__file__)) 

app = Flask (__name__)
app.config['SECRET_KEY']  = 'djflkdjflksflk' #crf key to be moved to config file
app.config['SQLALCHEMY_DATABASE_URI' ] =\
        'sqlite:///' + os.path.join(basedir, 'task.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile(os.path.join(basedir, 'config.cfg'))


 
db = SQLAlchemy(app) #db instances
app.app_context().push() #for setting up db file via terminal
mail = Mail(app)


from routes import *



if __name__ == '__main__':
        app.run(debug=True)

"""""
import os:
Imports the os module which provides functions for interacting with the operating system.

from flask import Flask:
    Imports the Flask class from the flask module. Flask is a web application framework written in Python.

from flask_sqlalchemy import SQLAlchemy:
Imports the SQLAlchemy class from the flask_sqlalchemy module. SQLAlchemy is an Object Relational Mapper (ORM) which provides a way to interact with databases.

from flask_login import UserMixin, login_user,LoginManager, login_required , logout_user, current_user:
Imports the UserMixin, login_user, LoginManager, login_required, logout_user, and current_user classes from the flask_login module. These classes provide user authentication and authorization functionality.

from flask_mail import Mail, Message:
Imports the Mail and Message classes from the flask_mail module. These classes provide email functionality.

basedir = os.path.abspath(os.path.dirname(__file__)):
Sets the basedir variable to the absolute
"""