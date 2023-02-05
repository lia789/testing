# Django Cheat Sheet

**Simple Guide for Setting up a Django Project**

 - [ ] Project
 - [ ] Application
 - [ ] Creating Project-Level Files
 - [ ] Creating Application-Level Files
 - [ ] Work with settings.py File
			- install apps
			- synchronize 'template' directory and static path
- [ ] Design "base.hml" File
- [ ]  Work with application level html files

```python
#setings.py
"DIRS": [BASE_DIR/ "templates"],
STATICFILES_DIRS = [BASE_DIR/ "static"]

#base.html
{% load static %}
<title>{% block title %}{% endblock %}</title>
<link rel="stylesheet" href="{% static "css/main.css" %}">
{% block content %}{% endblock content%}

#homepage.html
{% extends "base.html" %}
{% load static %}
{% block title %}Home Page{% endblock %}
{% block css_file %}<link rel="stylesheet" href="{% static "APP_NAME/APP_NAME.css" %}" />{% endblock %}>
{% block content %}{% endblock content%}
```


<br>

**Command-Line Utilities**

    $ python -m pip install Django
    $ python -m django --version
    $ django-admin startproject project_name
    $ python manage.py startapp app_name
    $ python manage.py runserver
    $ mkdir -p templates/ && touch $_/base.html $_/404.html && mkdir -p static/css && touch $_/main.css && mkdir -p static/img
    $ touch urls.py && mkdir -p templates/APP_NAME && touch $_/home_page.html && mkdir -p static/APP_NAME/css && touch $_/APP_NAME.css && mkdir -p static/APP_NAME/img




**Django URL Configuration**

    #application level urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [path("", views.home_page),]

	#project level urls.py
	from  django.contrib  import  admin
	from  django.urls  import  path, include
	
	urlpatterns = [
		path("admin/", admin.site.urls),
		path("", path("", include("app_name.urls")))
		]


**Function-based Views in Django**


    from django.shortcuts import render, redirect
    def home_page(request):
        return render(request, 'app_name/index.html', context={"name":"Sakib")
    def my_view(request):
        return redirect("/some/url/")


**Django Application Tools**
Django core
UI Design
Scrapy Integrations
Celery
Deploy on Cloud
Dockerize with Playwright


Hello World How are you all:tw-1f449:
