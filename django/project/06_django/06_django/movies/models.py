from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    genre = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()