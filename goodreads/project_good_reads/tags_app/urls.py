from django.urls import path
from .views import home_page, result_page, spider_status




urlpatterns = [
    path("", home_page, name="home_page"),
    path("result/", result_page, name="result_page"),
    path('spider_status/', spider_status, name='spider_status'),
]