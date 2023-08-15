from flask_bcrypt import Bcrypt
from datetime import datetime
from app import app, db
from flask import Flask, render_template ,redirect,url_for,flash
from models import Task 
from models import User
from flask_login import login_user, login_required , logout_user, current_user

import forms

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)



@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t =Task(title=form.title.data, date=datetime.utcnow(),user_id=current_user.id)
        db.session.add(t)
        db.session.commit()
        flash('task added')
        print('Submitted title', form.title.data)
        return redirect(url_for('index'))
    return render_template('add.html',form=form)


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
    return render_template('login.html',form=form)


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
    return render_template('register.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    task = Task.query.filter_by(user_id=current_user.id)
    return render_template('dashboard.html',task=task)
