from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alexander'}
    posts = [
        {
            'author': {'username': 'Alexander'},
            'body': 'Hello, first post',
        },
        {
            'author': {'username': 'John'},
            'body': 'Hello, second post',
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
