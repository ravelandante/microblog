from app import app
from app.forms import LoginForm
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# index/home page
@app.route('/')
@app.route('/index')
@login_required     # user has to be logged in to view page
def index():
    # dummy user
    user = {'username': 'Fynn'}
    # dummy posts/content
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Wowowow super cool'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Certified cool moment amirite?'
        }
    ]
    # render 'Home' page
    return render_template('index.html', title='Home', posts=posts)

# login page
@app.route('/login', methods=['GET', 'POST'])   # allow POST (submitting of data)
def login():
    # if user is already logged in and navigates to /login
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash error message
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # get 'next' string value from url
        next_page = request.args.get('next')
        # checks if next doesn't exist and protects from malicious attack (only allows redirection relative to same site)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    # render login if 1st time loading
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
