# Web Applications

Python comes with various modules that allow us to create web apps from scratch
but usually we do ourselves a favor by using pre-existing framework such as
Flask.

```bash
pip3 install flask
```

Flask is a micro framework. To use it, we can import it and create a simple
app.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str
  return "Hello"

app.run()
```

When we run our web app we get a web server and a loopback address to access our
app in a browser. We have also seen our first decorator. A decorator allows us
to take existing code and augment its functionality without having to change
functions/classes.

If rendering simple text is too boring, we can use Jinja which a templating
engine that comes with Flask. Jinja allows us to dynamically render HTML.

## Sessions and Cookies

When working with state in web apps we can't use global variables and the likes
to save state. Instead, we have to use a session with a cookie. In flask we can
import the session module for that.

```python
from flask import Flask, session

app.secret_key = 'our super secret key to encrypt our cookies'

@app.route('/user/<user>')
def setUser(user: str):
  session['user'] = user
```

The secret is set to encrypt the cookie before sending it to the browser. We can
check if a user is logged in with a function or a decorator.
