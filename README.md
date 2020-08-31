# recipe-app-api

1. Start project in docker
```
docker-compose run app sh -c "django-admin.py startproject app ."
```

2. Run test
```
docker-compose run app sh -c "python manage.py test && flake8"
```