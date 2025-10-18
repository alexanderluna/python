# Python

> Python is a programming language that lets you work more quickly and
> integrate your systems more effectively. - [Python.org](https://www.python.org)

Python is one of the most versatile and popular languages. It has a wide range
of application from web development and data science to GUI applications,
scripts and game development.

## Table of Contents

- [setup & installation](#setup--installation)
  - [learning python](/learning_python)
- [algorithms](/algorithms/)
- [command line interface apps](/cli_apps/)
- [django](/django)
- [flask](/flask)
- [data science](/jupyter)
- [pygame](/games)
- [resources](#resources)

## Setup & Installation

In the python community it is recommended to use **virtualenv** to manage
packages and project. While **virtualenv** is useful, **uv** is an even better
option because it combines both pip and virtualenv into one tool. First install
[mise](https://mise.jdx.dev/getting-started.html) a front-end for development
environments which makes it easier to install different versions of python and
**uv**.

``` sh
# on Linux
curl https://mise.run | sh

# on MacOS
brew install mise

# Install python/uv and add them to your $PATH automatically
mise use -g python@latest
mise use -g uv@latest
```

## Resources

- ★★★★★ [Head First Python](https://www.oreilly.com/library/view/head-first-python/9781491919521/)
- ★★★★★ [Python Brain Teasers](https://pragprog.com/titles/d-pybrain/python-brain-teasers/)
- ★★☆☆☆[[Course] Udacity Programming Fundamentals with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036)
