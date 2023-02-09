# Django Cheat Sheet

**Command-Line Utilities**

    $ python -m pip install Django
    $ python -m django --version
    $ django-admin startproject project_name
    $ python manage.py startapp app_name
    $ python manage.py runserver
    $ mkdir -p templates/ && touch $_/base.html $_/404.html && mkdir -p static/css && touch $_/main.css && mkdir -p static/img
    $ touch urls.py && mkdir -p templates/APP_NAME && touch $_/home_page.html && mkdir -p static/APP_NAME/css && touch $_/APP_NAME.css && mkdir -p static/APP_NAME/img
    $ python mange.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py reset_db --noinput
    $ python manage.py admin_generator app_name


**Managing the settings.py File**

    #setings.py
    "DIRS": [BASE_DIR/ "templates"],
    STATICFILES_DIRS = [BASE_DIR/ "static"]
    "django_extensions",
    "debug_toolbar"

**Handling Django Models**

    class Album(models.Model):
        artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        num_stars = models.IntegerField()



