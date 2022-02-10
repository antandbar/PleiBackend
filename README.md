# PleiBackend

To start the application use:

In development:

```sh
docker-compose build
```

```sh
docker-compose up
```

```sh
docker-compose run web python manage.py makemigrations
```

```sh
docker-compose run web python manage.py migrate
```

```sh
docker-compose run web python manage.py createsuperuser
```

