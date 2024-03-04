celery:
	DJANGO_SETTINGS_MODULE='config.settings.local' celery -A config worker -lINFO -Q blitzpay_members -E --concurrency=1

check:
	pre-commit run --all-files

lint:
	pre-commit run --all-files

test:
	pytest

make:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser

runserver:
	python3 manage.py runserver localhost:9003
