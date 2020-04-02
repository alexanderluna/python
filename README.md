# Python

> Python is a programming language that lets you work more quickly and
> integrate your systems more effectively. - [Python.org](https://www.python.org)

- [Python](#python)
  - [Why Python](#why-python)
  - [My Goals with Python](#my-goals-with-python)
  - [Learning Python](#learning-python)
  - [Development Setup](#development-setup)
    - [Working with pipenv](#working-with-pipenv)
    - [Working with Docker](#working-with-docker)

## Why Python

Python is one of the most versatile and popular languages. It has a wide range
of application from web developement and data science to GUI applications,
scripts and game development. A lot of big companies use it daily and the
amount of online resources is large and well documented.

## My Goals with Python

Due to the large range of application for Python my main focus with this
language revolves aronud web development and data science:

- Django
- Flask
- Data Science (Pandas, Numpy, Pytorch, etc.)
- Pygame

## [Learning Python](/learning_python)

Resources, steps and notes I take to learn python.

## Development Setup

In the python community it is recommended to use **virtualenv** to manage
packages and project. While **virtualenv** is useful **pipenv** is a better
option because it combines both pip and virtualenv into one tool. Personally,
I find docker with named volumes to be even better and simpler to setup.

### Working with pipenv

``` bash
mkdir something-new
cd something-new

# create new environment with latest python3
pipenv --three

# install package
pipenv install django

# install from requirements.txt
pipenv install -r requirements.txt

# update outdated packages
pipenv update --outdated

# run a shell
pipenv shell

# finally to exit the shell just type 'exit'
exit
```

We can also create scripts similar to how we would using npm/yarn.
For that we create a new section inside the generated Pipfile called sripts
and specify the name followed by the command:

```Pipfile
[scripts]
start = "python manage.py runserver"
```

```bash
pipenv run start
```

### Working with Docker

I prefer docker mainly for the reason that it is easier to get started and
replicate. I use a docker-compose file to install the required modules and start
a development server or run the code:

```docker
version: '3'

services:
  django:
    image: python:3.7-alpine
    volumes:
     - pip37:/usr/local/lib/python3.7/site-packages
     - .:/project
    ports:
      - "8000:8000"
    working_dir: /project
    command: python manage.py runserver 0.0.0.0:8000
    depends_on:
      - requirements

  requirements:
    image: python:3.7-alpine
    volumes:
      - pip37:/usr/local/lib/python3.7/site-packages
      - .:/project
    working_dir: /project
    command: pip install -r requirements.txt

volumes:
  pip37:
    external: true
```

I could run container, attach a named volume and install the packages I need
first and then use the same named volume in my docker compose to reduce the
number of services but this would mean more steps so I opted for the double
service variant which can be executed with a simple:

```bash
docker-compose up
```
