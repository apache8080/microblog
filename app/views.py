from flask import render_template, flash, redirect, url_for, request, g, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, CreateAccountForm, CreatePostForm
from app import app, db, models, lm, bcrypt
import datetime

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = current_user
    posts = models.Post.query.all()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error= None
    if request.method =='POST':
        if form.validate_on_submit():
            user = models.User.query.filter_by(uname=form.uname.data).first()
            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('index'))
            else:
                error = 'Invalid username or password.'
    #print user
    return render_template('login.html', form=form, error=error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('login'))

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        uname = form.uname.data
        password = form.password.data
        email = form.email.data
        u = models.User(uname, email, password)
        db.session.add(u)
        db.session.commit()
        flash('Account Created for %s' % (uname))
        return redirect('/index')
    return render_template('create_account.html', 
                           title='Create Account',
                           form=form)

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    user = current_user
    if form.validate_on_submit():
        post_title = form.post_title.data
        post_content = form.post_content.data
        p = models.Post(post_title, post_content, datetime.datetime.utcnow(), user)
        db.session.add(p)
        db.session.commit()
        flash('Post Created by %s' % (user.uname))
        return redirect('/index')
    return render_template('create_post.html', title='Create Post',
                           form=form)
