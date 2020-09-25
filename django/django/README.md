# Django App

requirements:

- python 3.9
- pipenv
- django 3.1+
- pyenv (optional)

## Getting Started

```bash
# navigate to the project and run a pipenv shell
cd django
pipenv shell

# now run all pending migrations
python manage.py migrate

# start the server
python manage.py runserver
```

## Creating an App

At first, we only have an empty project with a configuration file. In django you
create a project first, hence `django startproject`, and add functionality
through apps.

> Creating an app is subjective but each app should have a clear function

```bash
# create an app called "pages"
python manage.py startapp pages
```

This generates severals files within the pages folder.

- admin.py (build in admin app)
- apps.py (app configuration)
- migrations/ (tracks models.py)
- models.py (database models)
- tests.py
- views.py (request/response logic)

Since we created an app, we have to add it to the project in
`config/settings.py`.

```python
INSTALLED_APPS = [
  ...,
  'pages',
]
```

## Django Fundamentals

At its core, django rquires a `urls.py`, `views.py`, `models.py` and an
`index.html` template. A request is first matched by the `urls.py` file through
a regular expression which specifies a view. The view in turn, accesses the
database through the model and sends a styled template to the user. Each app has
its own `urls.py` file with urls matching routes within the app. We include the
app specific `urls.py` file into the project's `urls.py` file.

We define an `urls.py` file for each app and within our `views.py` we add the
logic required to render the correct templates.

```python
# views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
```

```python
# pages/urls.py
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

## Testing our Apps

In order to make our code robust, we can use the build in testing tools and the
auto generated `test.py` file.

## Deploy on Heroku

We have to tell heroku to ignore static files given that django optimizes them
for us.

```bash
cd django

heroku create

heroku config:set DISABLE_COLLECTSTATIC=1

git push heroku master

heroku ps:scale web=1

heroku open
```
