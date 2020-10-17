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
