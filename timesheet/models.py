from django.db import models
from datetime import datetime


class Week(models.Model):
    created_at = models.DateTimeField(atuo_now_add=True)
    day = datetime.today().strftime('%A')
    total_made = models.FloatField(default=0)
    comments = models.TextField()
    order = models.IntegerField(default=0)
    total = sum(range(0, 6))

    def __str__(self):
        return self.title




# 2 seperate models that will corerespond to the same day
class DayInput(models.Model):
    # created_at = models.DateTimeField(atuo_now_add=True)
    # title = models.CharField(max_length=32, unique=True)
    # order = models.IntegerField(default=0)
    monday = datetime.today().strftime('%A')
    tuesday =
    wednesday =
    thursday =
    friday =
    saturday =
    sunday =

class Weekly(models.Model):
    monday = models.FloatField(default=0)
    tuesday = models.FloatField(default=0)
    wednesday = models.FloatField(default=0)
    thursday = models.FloatField(default=0)
    friday = models.FloatField(default=0)
    saturday = models.FloatField(default=0)
    sunday = models.FloatField(default=0)
