from django.db import models

class Quote(models.Model):
    author_name = models.CharField(max_length=255)
    number_of_likes = models.IntegerField()
    quotes_text = models.TextField()

    def __str__(self):
        return f"{self.author_name}: {self.quotes_text}"

