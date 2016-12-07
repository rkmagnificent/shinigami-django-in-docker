#### Create new Django project

```shell
$ docker build -t shinigami .
$ docker run --rm -it -v $(pwd):/code shinigami django-admin startproject shinigami .
```

#### Create new app ryuk

```shell
$ docker run --rm -it -v $(pwd):/code shinigami python manage.py startapp ryuk
```

#### Create view for ryuk

use of name argument of url https://docs.djangoproject.com/en/1.10/topics/http/urls/#naming-url-patterns

#### Migrate database

```shell
$ docker run --rm -it -v $(pwd):/code shinigami python manage.py migrate
```

#### Create models for ryuk

Steps:

1. First add model classes in ryuk/models.py
2. Add RyukConfig to shinigami/settings.py INSTALLED_APPS

```shell
echo "create a file for migration"
$ docker run --rm -it -v $(pwd):/code shinigami python manage.py makemigrations ryuk
echo "to view how migration happens"
$ docker run --rm -it -v $(pwd):/code shinigami python manage.py sqlmigrate ryuk 0001
echo "run migration in db"
$ docker run --rm -it -v $(pwd):/code shinigami python manage.py migrate
```

