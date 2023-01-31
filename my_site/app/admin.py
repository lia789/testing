from django.contrib import admin

from .models import QuotesText


@admin.register(QuotesText)
class QuotesTextAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
