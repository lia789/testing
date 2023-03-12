# Django Cheat Sheet


**Django Project Building Steps**

```
List of steps about writing code about Django project:
    1. Django project and application
    2. Setup project file structure
    3. Write settings.py file
    4. Define models with best practice such as normalizing database, using appropriate data types, and field options.
    5. Define admin interface code
    6. Write forms
    7. Create views for the app using best practices such as keeping the views small, reusable, and using django class based views
    8. Define URL patterns application and project level
    9. Create templates for the views and use best practices for template design such as separating presentation from logic and using template inheritance
    10. Work with authentication system
    11. Work with emails and list of other features
    12. Work with Django caching
    13. Do data base migrations
    14. Create super user
    15. Setup Django project for deployment
```


**Command-Line Utilities**

```cmd
$ python -m pip install Django
$ python -m django --version
$ django-admin startproject project_name .
$ python manage.py startapp app_name
$ python manage.py runserver
$ mkdir -p templates/ && touch $_/base.html $_/404.html && mkdir -p static/css && touch $_/main.css && mkdir -p static/img
$ touch urls.py && mkdir -p templates/APP_NAME && touch $_/home_page.html && mkdir -p static/APP_NAME/css && touch $_/APP_NAME.css && mkdir -p static/APP_NAME/img
$ python mange.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```


**Managing the settings.py File**
```python
#settings.py
"DIRS": [BASE_DIR/ "templates"],
STATICFILES_DIRS = [BASE_DIR/ "static"]
```


**Working with Models**

```python

# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'my_custom_table_name'
        ordering = ['colum_name', 'column_name']
        verbose_name_plural = 'My Models'

    def __str__(self):
        return self.column_name

    def save(self, *args, **kwargs):
        # perform some custom validation or processing here
        super(MyModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # perform some custom processing here
        super(MyModel, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.pk})

```


**Working with admin**

```python
# admin.py
from django.contrib import admin
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    list_filter = ('age',)
    search_fields = ('name',)

```


**Django Form**
```python
# forms.py
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('name', 'email', 'message')


# views.py
def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if name == 'John':
                form.add_error(None, 'Sorry, John is not allowed to submit this form.')
            else:
                # Process form data
                return HttpResponse('Form submitted successfully.')
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})


# my_forms.html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```




**Django URL Pattern**
```python
# Application level urls.py
from django.urls import path
from .views import home_page

urlpatterns = [
    path("", home_page, name="home"),
]

# Project level urls.py
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_name.urls")),
]
```


**Django Class based views**

```python
## TemplateView ##
# urls.py
from django.views.generic.base import TemplateView

path("about/", TemplateView.as_view(template_name="app_name/about.html"), name="about"),


# ListView
from django.views.generic.list import ListView
from app_name.models import model_name

class ModelNameListView(ListView):
    model_name = model_name
    template_name = "template_name.html"

# urls.py
from app_name.views import ModelNameListView
path("", ArticleListView.as_view()),

# my_list_view.html
{% for data in object_list %}
    <li>{{ data.key_name}} - {{ data.key_name }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}



# DetailView
from django.views.generic.detail import DetailView
from app_name.models import model_name

class ArticleDetailView(DetailView):
    model = model_name
    template_name = "detail.html"


# urls.py
from app_name.views import ModelNameListView
path("post/<int:pk>/", ArticleListView.as_view()),

# my_list_view.html
{% block content %}
    <h2>{{ object.title }}</h2>
    <p>{{ object.body }}</p>
{% endblock content %}


# CreateView
from django.views.generic.edit import CreateView
from app_name.models import model_name

class ArticleCreateView(CreateView):
    model = model_name
    template_name = "new_post.html"
    fields = ["title", "author", "body"]\
    success_url = reverse_lazy("home")

# urls.py
from app_name.views import ArticleCreateView
path("post/new", ArticleCreateView.as_view()),

# my_list_view.html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>


```



**Django Template**

```python

# Template inheritance
<!-- templates/base.html -->
{% load static %}
<html>
<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400" rel="stylesheet">
<link href="{% static 'css/main.css' %}" rel="stylesheet">

{% extends "base.html" %}
{% block title %}{% endblock title %}
{% block content %}{% endblock content%}
{% include "reusable/reusable.html" %}


# Template tag
{% url 'some-url-name' arg1=v1 arg2=v2 %}

{% if athlete_list %}
    # HTML
{% elif athlete_in_locker_room_list %}
    # HTML
{% else %}
    # HTML
{% endif %}

{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}


# Template filter
{{ value|title }}
{{ value|length }}


# Template variables
{{ first_name }}
{{ my_dict.key }}

```


**Django Scrapy Item Integration**

```
Steps about integrating Django models with Scrapy:
    1. Define models on Django
    2. Store Scrapy project on Django project root director. Should be scrapy.cfg and manage.py are same directory.
    3. Setup environment variable on Scrapy settings.py
    4. Inherit Django model on Scrapy item.py and write Scrapy item code
    5. Write database save save code on pipelines.py file
    7. Enable Item pipeline on Scrapy setting.py
    6. Runspider and test database
```

```python

# Scrapy settings.py file
import os
import sys
import django

# Django Integration
sys.path.append(os.path.abspath("django_project_name"))
os.environ["DJANGO_SETTINGS_MODULE"] = "my_site.settings"
django.setup()


# Scrapy items.py
import scrapy
from scrapy_djangoitem import DjangoItem
from django_app_name.models import ModelName

class ModelNameItem(DjangoItem):
    django_model = ModelName


# Scrapy pipelines.py
from app_name.models import ModelName

class QuotesbotPipeline(object):
    def process_item(self, item, spider):
        data = QuotesText(
            author=item.get("author"),
            title=item.get("title")
            )
        data.save()
        return item


# Scrapy setting.py
ITEM_PIPELINES = {
   'quotesbot.pipelines.QuotesbotPipeline': 300,
   'quotesbot.pipelines.DataCleanerPipeline': 200,
}
```








