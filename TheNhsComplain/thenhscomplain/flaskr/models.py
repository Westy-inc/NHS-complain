from flask_login import UserMixin,LoginManager, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin , AdminIndexView
from flask import redirect,url_for
from app import app , db


login = LoginManager(app)



#setting up db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
    public = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model,UserMixin ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable =False)
    email = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    admin = db.Column(db.Boolean, default=False)

class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    HospitalName =  db.Column(db.String(225), nullable=False)
    HospitalAddress = db.Column(db.String(225), nullable=False)
    trustID = db.Column(db.Integer, db.ForeignKey('trusts.id'))

class Trusts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TrustName = db.Column(db.String(225), nullable=False)
    Region = db.Column(db.String(225), nullable=False)
    HeadquartersAddress = db.Column(db.String(225), nullable=False)
    Hospitals = db.relationship('Hospitals', backref='trust', lazy=True)



    @login.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

class Postview(ModelView):
    can_delete = False
    form_columns = [ 'username', 'email','tasks']
    column_list = [ 'username', 'email','tasks']




class  Adminsec(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class Adminsec2(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

admin = Admin(app ,index_view=Adminsec2())
admin.add_view(Adminsec(Task,db.session))
admin.add_view(Adminsec(User,db.session))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
@login_manager.user_loader   #manager for logining user in 
def load_user(user_id):
    return User.query.get(int(user_id))


