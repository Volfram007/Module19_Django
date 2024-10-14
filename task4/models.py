from django.db import models


class GameNews(models.Model):
    objects = None
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
