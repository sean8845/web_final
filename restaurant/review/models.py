# models.py
from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.username
