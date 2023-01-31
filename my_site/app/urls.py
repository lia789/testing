from django.urls import path
from . import views
# from .views import ExportQuotesView

urlpatterns = [
    path("", views.home_page),
    # path("ok/", views.thank_you_page),
    # path('csv/', ExportQuotesView.as_view(), name='export_quotes'),
    path("csv/", views.export_quotes_view, name='export_quotes'),
    path("ok/", views.run_spider, name="run_spider"),
]
