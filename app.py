import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__)) 

app = Flask (__name__)
app.config['SECRET_KEY']  = 'djflkdjflksflk' #crf key
app.config['SQLALCHEMY_DATABASE_URI' ] =\
        'sqlite:///' + os.path.join(basedir, 'task.db')
app.config ['SQLALCHEMY_BINDS'] = {'auth' : 'sqlite:///' + os.path.join(basedir, 'users.db')}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




db = SQLAlchemy(app) #db instance
app.app_context().push() #for setting up db file via terminal



from routes import *



if __name__ == '__main__':
    app.run(debug=True)
