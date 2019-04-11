.PHONY: coverage test

start:
	docker-compose up server

daemon:
	docker-compose up -d server

connect:
	docker-compose exec server bash

test:
	docker-compose run --rm testserver

coverage:
	docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

lint:
	docker-compose run --rm server bash -c "python vendor/bin/flake8 ./src ./test"

safety:
	docker-compose run --rm server bash -c "python vendor/bin/safety check"

db/connect:
	docker-compose exec db mysql -uroot my_cellar

db/init:
	docker-compose run --rm server python src/manage.py db init

db/upgrade:
	docker-compose run --rm server python src/manage.py db upgrade

db/migrate:
	docker-compose run --rm server python src/manage.py db migrate

db/downgrade:
	docker-compose run --rm server python src/manage.py db downgrade

.env: .env.example-local
	@if [ -f .env ]; \
	then\
		echo '\033[1;41m/!\ The .env.example-local file has changed. Please check your .env file (this message will not be displayed again).\033[0m';\
		touch .env;\
		exit 1;\
	else\
		echo cp .env.example-local .env;\
		cp .env.example-local .env;\
	fi

install: .env
	docker-compose run --rm server pip install -r requirements/dev.txt --user --upgrade --no-warn-script-location

prettify:
	pipenv run black -l 120 src/ test/ migrations/

prettify/check:
	pipenv run black --check -l 120 src/ test/ migrations/

lint/flake8:
	pipenv run flake8 src/ test/

sort_imports:
	pipenv run isort -rc test/ src/ migrations/
	make prettify

sort_imports/check:
	pipenv run isort -rc test/ src/ migrations/ --check-only
import/fixtures:
	docker-compose run --rm server python src/manage.py import/fixtures
