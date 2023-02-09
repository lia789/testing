from django.contrib import admin

from .models import ChannelSearchKeyword


@admin.register(ChannelSearchKeyword)
class ChannelSearchKeywordAdmin(admin.ModelAdmin):
    list_display = ('channel_keyword',)



