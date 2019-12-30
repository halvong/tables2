docker-compose run --rm database psql -U hal -h database


docker-compose exec web python manage.py makemigrations tutorial
docker-compose exec web python manage.py migrate tutorial

docker-compose exec web python manage.py createsuperuser