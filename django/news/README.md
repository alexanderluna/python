# News

requirements:

- python 3.9
- pipenv
- django 3.1+
- pyenv (optional)

While we can use the build user model it is highly advised to use custom user
models in our application because the build in one is hard to modify and
extend. In order to create our custom user model, we have to tell django that
we will use our own model. Our custom model has to inherit from either
`AbstractBaseUser` or `AbstractBase`. The first, allows us to completely rewrite
django's behavior if we want and the later allows us to make more changes to
the user model. Thus, we will use the `AbstractBase` class.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
```

## Sending Email

Using SendGrid we can add email sending capabilities to our project. For that
we have to go to [SendGrid](https://sendgrid.com/) and create an API key for
SMTP Relay. Now that we got our key and credentials we can setup SMTP on our
django app.

```python
# config/settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'your_custom_email_account'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'YOUR_API_KEY'
EMAIL_HOST_PASSWORD = 'YOUR_SENDGRID_PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

At first it might not work because SendGrid has to verify our identity. We can
go back to the SendGrid console and start the verification process but once this
is done we are set to send emails.

## Deployment

Part of our deployment requires us to protect sensitive data and configure our
app base on development or production. We can use `environs` to add environment
variables to our project. We can install it and create a `.env` file to store
our variables.

```bash
pipenv install 'environs[django]==8.0.0'
```

Now we have to add it to our `settings.py` and while we are at it, turn Debug to
false. We also want to specify which hosts are allowed for our project by
whitelisting them and finally we want to dynamically change the database for
our production environment.

```python
# config/settings.py
from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']

DATABASES = {
    'default': env.dj_db_url("DATABASE_URL")
}
```

In production we will use postgresql and for that we need a database adapter.
We will use `psycopg`.

```bash
pipenv install psycopg2-binary==2.8.5
```

Now we can configure our static files as well. We add the `whitenoise` package
, compile our static files and configure it.

```bash
pipenv install whitenoise==5.1.0

python manage.py collectstatic
```

```python
# config/settings.py
STATIC_URL = '/static/'

STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]

STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Finally, we add a production grade web server to our project: `gunicorn`.

```bash
pipenv install gunicorn==19.9.0
touch Procfile
```

```Procfile
web: gunicorn config.wsgi --log-file -
```

Once we push to production all we have to do is to set a secret key, migrate
our database and create a super user.

```bash
heroku config:set SECRET_KEY='somesecret'
heroku run python manage.py migrate
heroku run python manage.py createsuperuser

# check deployment check list
heroku run python manage.py check --deploy
```