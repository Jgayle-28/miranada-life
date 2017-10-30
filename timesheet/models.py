from django.db import models
from datetime import datetime

class Week(models.Model):
    created_at = models.DateTimeField(atuo_now_add=True)
    title = models.CharField(max_length=32, unique=True)
    order = models.IntegerField(default=0)

class DayInput(models.Model):
    created_at = models.DateTimeField(atuo_now_add=True)
    day = datetime.now.strftime('%A')
    total_made = models.IntegerField(default=0)
    comments = models.TextField()
    order = models.IntegerField(default=0)
