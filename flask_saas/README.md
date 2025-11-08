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
# saas/app.py
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    return app
```

## [Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/)

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

## [Testing and Coverage](https://flask.palletsprojects.com/en/stable/tutorial/tests/)

For testing you can use `pytest` and for coverage you can use `coverage.py` or
`pytest-cov`.

```zsh
uv add pytest pytest-cov  
```

Now you can start configuring your tests by creating a `tests/conftest.py` file.
You want to use the previously created App Factory and configure your `pytest`
by creating creating a custom test app, a context for the test environment and
push that context to the current context.

```python
import pytest

from saas.app import create_app


@pytest.yield_fixture(scope="session")
def app():
    params = {"DEBUG": False, "TESTING": True}
    _app = create_app(settings_override=params)
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.yield_fixture(scope="function")
def client(app):
    yield app.test_client()
```

Now you can run your tests using UV or configuring your test in the
`pyproject.toml` file.

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

```zsh
uv run py.test tests 

# if you configured your tests in pyproject.toml
pytest --cov=saas tests
```
