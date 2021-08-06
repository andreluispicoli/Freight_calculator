SHELL := /bin/bash

install:
	pipenv install

activate:
	pipenv shell

run:
	python manage.py runserver

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

heroku:
	git push heroku master

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down
