# ——————————————————————————
# Virtual Environment:-
# ——————————————————————————
# target a - for activating the default virtual environment
a:
	source bin/activate

# target d - for deactivating the virtual environment
d: 
	deactivate

# ——————————————————————————
# Shell in django:-
# ——————————————————————————

# target sh - for getting the python shell for your project
sh:
	poetry run python -m src.manage shell

# Shell - for getting the python shell
dbsh:
	poetry run python -m src.manage dbshell

# target test - for testing the project
test:
	poetry run python -m src.manage test

# target migrations - for saving migrations
migrations: 
	poetry run python -m src.manage makemigrations

# target migrate - for applying migrations
migrate: migrations
	poetry run python -m src.manage migrate

# target run - for running the development server on 8000 port
run: 
	poetry run python -m src.manage runserver

# target run80 - for running the development server on 80 port
run80:
	poetry run python -m src.manage runserver 80

# target app - for creating new app for project
app:
	poetry run python -m src.manage startapp

# ——————————————————————————
# User Management:-
# ——————————————————————————

# target adduser - for creating a superuser for your project
adduser:
	poetry run python -m src.manage createsuperuser

# target passwd - for changing the password of the superuser
passwd: 
	poetry run python -m src.manage changepassword

# ——————————————————————————
# Container Mangement:-
# ——————————————————————————

# target deploy - for running the django project from docker-compose

# ——————————————————————————
# Git and GitHub:-
# ——————————————————————————
# target add - for adding all the files in git repo
add: 
	git add .

# target commit - for adding all the files in git repo
title=""
des=""
commit: add
	git commit -am $title -m $des