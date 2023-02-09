from django.urls import path
from .views import channels_meta_data, data_preview


urlpatterns = [
    path("", channels_meta_data, name='home'),
    path("data/", data_preview, name='data_preview_url'),
]