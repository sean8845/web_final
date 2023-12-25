from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    table = models.IntegerField()
    
    def __str__(self):
        return self.name
