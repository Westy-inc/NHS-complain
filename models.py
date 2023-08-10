from app import db
from flask_login import UserMixin



#setting up db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
   
    def __repr__(self):
        return f'<Student {self.title} was created {self.date}>'
    
class User(db.Model,UserMixin ):
    __bind_key__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable =False)
    email = db.Column(db.String, nullable=False)