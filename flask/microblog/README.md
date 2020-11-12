# Microblog

requirements:

- python 3.9
- pipenv
- flask
- pyenv (optional)

## Getting Started

```bash
pipenv shell
pipenv install

export FLASK_APP=microblog.py
flask run
```

## Setting up the Database

First, we have to install some packages to work with the database and manage
migrations.

```bash
pipenv install flask-sqlalchemy
pipenv install flask-migrate
```

Now we have to add a database url to our configuration and hook up the database
in our initializer.

1. [config.py](./config.py)
2. [app/__init__.py](./app/__init__.py)

Finally, we create a model, initialize our database, generate a migration and
execute our migration.

1. [app/models.py](./app/models.py)
2. `flask db init`
3. `flask db migrate -m "users table"`
4. `flask db upgrade`

> `flask db upgrade` migrates our database. We can run `flask db downgrade` to
> do the opposite.

Now, we can add users manually through the CLI launching the flask shell

```python
# flask shell

user = User(username="john", email="john@email.com")
db.session.add(user)
db.session.commit()
```

## User Login and Registration

When it comes to login in users and registering new users, we can use
`flask-login` and `email_validator`

- `pipenv install flask-login`
- `pipenv install email_validator`

Now we configure our initializer to add the LoginManager and redirect view to
our app.

- [app/__init__py](./app/__init__.py)

Next, we add routes for login and registering in our routes files, create forms,
templates for our routes and configure our User model to hash passwords using
`werkzeug`.

- [app/routes.py](./app/routes.py)
- [app/models.py](./app/models.py)
- [app/forms.py](./app/forms.py)
- [app/templates/login.html](./app/templates/login.html)
- [app/templates/register.html](./app/templates/register.html)
