# This code is setting up a Flask application with a SQLite database.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



basedir = os.path.realpath(os.path.dirname(__file__))


app = Flask (__name__,template_folder='templates')
app.config['SECRET_KEY']  = 'djflkdjflksflk' #crf key to be moved to config file
app.config['SQLALCHEMY_DATABASE_URI' ] =\
'sqlite:///' + os.path.join(basedir, 'task.db')
app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False






db = SQLAlchemy(app) #db instances
app.app_context().push() #for setting up db file via terminal

from routes import *



if __name__ == '__main__':
        app.run(debug=True)
