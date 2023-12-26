from django.db import models

class Reservation(models.Model):
    # 模型的字段定義
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return self.name
