from django.db import models


class ChannelSearchKeyword(models.Model):
    channel_keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.channel_keyword


class DataToCSV(models.Model):
    pass






