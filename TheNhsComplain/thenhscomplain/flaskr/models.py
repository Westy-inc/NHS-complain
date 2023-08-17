from app import app, db
from flask_login import UserMixin,LoginManager


#setting up db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
    public = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<Student {self.title} was created {self.date}>'
    
class User(db.Model,UserMixin ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable =False)
    email = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
@login_manager.user_loader   #manager for logining user in 
def load_user(user_id):
    return User.query.get(int(user_id))