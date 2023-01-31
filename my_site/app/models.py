from django.db import models



class QuotesText(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=250)




class UserInput(models.Model):
    quotes_keyword = models.CharField(max_length=50)