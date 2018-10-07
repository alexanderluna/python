# My Python projects

Python projects are seperated into folders:

1. django
2. games
  1. snakeGame.py (retro snake game using pygame)
3. scripts
  1. primeNumber.py (calculate all prime numbers)

## Working with pipenv

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
```

finally to exit the shell just type 'exit'

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
