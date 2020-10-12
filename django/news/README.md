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
 