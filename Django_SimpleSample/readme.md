# Steps

## Install django
pip3 install django

## Create project and app
django-admin startproject simple_project
python manage.py startapp simple_app

## Add configuration

add app on **settings.py**
```
INSTALLED_APPS = [
    'simple_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

add url on urls.py from project
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("auctions.urls"))
]
```

## Create app files

### Create **urls.py** on app

```
from django.urls import path
from . import  views

urlpatterns = [
    path("", views.index, name="index")
]
```

### Modify **views.py** on app
```
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
```

### Create html file on html folders
create templates/app_name folders within app folder
- create layout.html file

## Create static files
create static/app_name folders within app folder
- add  .js and .css files

