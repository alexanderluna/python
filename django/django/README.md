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

## Generating Models

Each app has its own `models.py` file. We can create our models there. Everytime
we update our models file we have to create a migration with `makemigrations`
and then we run our migration with the `migrate` command.

```bash
python manage.py makemigrations posts
python manage.py migrate
```

## Django Admin

Django comes with a build in CMS that allows us to interact with our data
easily. To being, we have to create a superuser who can login.

```bash
python manage.py createsuperuser
```

## Testing our Apps

In order to make our code robust, we can use the build in testing tools and the
auto generated `test.py` file.

## Working with Forms

In order to work with forms, we have to create a view with a template as we are
used to. In our `views.py` we have to whitelist the database fields we want to
expose.

```python
from django.views.generic.edit import CreateView

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

```

Inside our template, we can render the fields and protect againt XSS attacks as
follows.

```html
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```

After submiting our form, django doesn't know where it should redirect the user
to. Thus we have to specify a url inside our database model class.

```python
class Post(models.Model):
  # ...
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
```

## Working with Static Files

Django doesn't serve static files in production. Instead, we have to compile
all static files into a directory for deployment. For that we configure our
project in `settings.py`

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]

STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
```

Now we can run the `collectstatic` command to compile all static files into one
directory.

```bash
python manage.py collectstatic
```

In order to server our static files directory in production we can use the
`whitenoise` package.

```bash
pipenv install whitenoise==5.1.0
```

We have to make some changes to use whitenoise in our project. In `settings.py`

```python
# 1) add whitenoise before staticfiles
INSTALLED_APPS = [
    ...,
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

# 2) add whitenoise middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

# 3) change the static files storage method
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Finally we have to compile our static files again.

```bash
pipenv install whitenoise==5.1.0
```

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

Now its time to change our default web server for a production web server

```bash
pipenv install gunicorn==19.9.0
```
