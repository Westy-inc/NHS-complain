"""
    This is a Flask application with routes for user registration, login, logout, adding, editing, and
    deleting tasks, and displaying user details.
    :return: The code is returning the Flask application routes and their corresponding HTML templates.
"""
from flask_bcrypt import Bcrypt
from datetime import datetime
from app import app, db
from flask import render_template ,redirect,url_for,flash,request
from models import Task , User , Hospitals
from flask_login import login_user, login_required , logout_user, current_user
import forms 

@app.route('/index', methods=['GET', 'POST'])
def index():
        return redirect(url_for('start'))



def add_user_task(name, surname, email, body):
    t = Task(body=body, date=datetime.utcnow(), name=name, surname=surname, email=email)
    db.session.add(t)
    db.session.commit(t)

def gettask(body):
    body=body

def getinfo(name, surname, email):
    name=name, 
    surname=surname
    email=email

def gethospital(hospital):
    hospital=hospital
    Hospid = db.session.query(Hospitals).filter(Hospitals.HospitalName==hospital).first()
    hospital = Hospid.id
    print (hospital)



@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.is_submitted():
        gettask(body=form.body.data)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>',  methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("task has been updated")
            return redirect(url_for('index'))
        form.title.data=task.title
        return render_template('edit.html' , form=form, task_id=task_id)
    print (task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>',  methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.deleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("task has been deleted")
            return redirect(url_for('index'))
        return render_template('delete.html' , form=form, task_id=task_id,task=task.title)
    return redirect(url_for('index'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginUserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and Bcrypt().check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('/auth/login.html',form=form)


@app.route("/register",  methods=['GET', 'POST'])
def register():
    form = forms.NewUserForm()
    if form.validate_on_submit():
        hashed_password = Bcrypt().generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password
                        , email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('/auth/register.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('/auth/login'))


@app.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
        task = Task.query.filter_by(user_id=current_user.id)
        return render_template('dashboard.html',task=task)


@app.route('/details',methods=['GET', 'POST'])
def details():
    form = forms.Userdetails()
    if form.is_submitted():
        getinfo(name=form.name.data, surname=form.surname.data, email=form.email.data)
        return redirect(url_for('ContactInformation'))
    return render_template('details.html', form=form)


@app.route('/dateofbirth',methods=['GET', 'POST'])
def dateofbirth():
        form = forms.Userdetails()
        next = forms.NextForm()
        if form.validate_on_submit():
            return redirect(url_for('ContactInformation'))

@app.route('/ContactInformation', methods=['GET', 'POST'])
def ContactInformation():
    form = forms.Userdetails()
    next = forms.NextForm()
    if next.validate_on_submit():
        print('Before redirect')
        return redirect(url_for('add'))
    return render_template('ContactInformation.html', form=form , next=form)

@app.route('/start',methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def start():
    form = forms.NextForm()
    if form.validate_on_submit():
        print('Before redirect')
        return redirect(url_for('details'))
    return render_template('start.html', form=form)


@app.route('/service-lookup',methods=['GET', 'POST'])
def Servicelookup():
    return render_template('service-lookup.html')



@app.route('/search',methods=['GET', 'POST'])
def search():
    form = forms.AddTaskForm()
    q = request.args.get("q")
    print (q)
    if q:
        results = Hospitals.query.filter(Hospitals.HospitalName.icontains(q))\
            .order_by(Hospitals.HospitalName.asc()).limit(5)
    else:
        results= []
    if request.method == 'POST':
        form.hospital.data = request.form["hosp"] #gets the name of the hospital for the add form (might need to change method later)
        print (form.hospital.data)
        gethospital(hospital=form.hospital.data)
        return redirect(url_for('add'))
    return render_template('search_results.html', results=results,form=form)