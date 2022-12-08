from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# index/home page
@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)

# login page
@app.route('/login', methods=['GET', 'POST'])   # allow POST (submitting of data)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash login message
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # return to index
        return redirect(url_for('index'))
    # render login if 1st time loading or validation failed
    return render_template('login.html',  title='Sign In', form=form)
