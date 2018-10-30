# Python

> Python is a programming language that lets you work more quickly and
> integrate your systems more effectively. - [Python.org](https://www.python.org)

## Index

- [Why Python](#why-python)
- [My Goals with Python](#my-goals-with-python)
- [Development Setup](#development-setup)
    - [Working with pipenv](#working-with-pipenv)
- [Projects](#)
    - [Django](/django)
    - [Flask](/flask)
    - [Pygame](/games)
    - [Data Science](/Jupyter)
    - [Scripts](/scripts)

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
