
install:
	pip install -r requirements.txt

run:
	python manage.py runserver

docker-up:
	docker-compose up --build

createsuperuser:
	python manage.py createsuperuser