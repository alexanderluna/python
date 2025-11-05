# Flask SAAS App

## Setup and Installation

```zsh
# initialize a UV project
uv init .

# create a virtual environment
uv run main.py

# start server either with uv or without
gunicorn -w 4 --reload 'saas.app:create_app()'
uv run gunicorn -w 4 --reload 'saas.app:create_app()'
```

```toml
# configure mise to use the virtual environment
# ~/.config/mise/config.toml
[settings]
python.uv_venv_auto = true
```

Once you have installed everything you can start by creating a
[Flask Application Factory](https://flask.palletsprojects.com/en/stable/patterns/appfactories/).
which allows you to configure and run different instances of Flask. All you need
is to define a `create_app` function with an optional config file as an
argument and return a Flask app object.

```python
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    return app
```

## Blueprints

Blueprints allows you to break up your app in components which allows you to add
namespaces, routes and templates in a maintainable manner. You can create a
blueprint by creating a folder for each blueprint and  importing `Blueprint`
from `flask`:

```python
# saas/blueprints/page
from flask import Blueprint, render_template

page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
def home():
    return render_template("page/home.html")
```

Now you registering your blueprint in the Application Factory:

```python
# saas/app.py
from saas.blueprints.page import page

def create_app():
    # ...
    app.register_blueprint(page)

    return app
```
