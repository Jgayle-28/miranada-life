from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime

WEEKDAY = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)

class DailyEarning(models.Model):
    user = models.ForeignKey(User, related_name='earnings')
    recorded_at = models.DateTimeField(default=timezone.now, editable=False)
    day = models.IntegerField(choices=WEEKDAY)
    made = models.FloatField(default=0)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d '), self.get_day_display())

    class Meta:
        ordering = ['day']


# class Week(models.Model):
#     created_at = models.DateTimeField(atuo_now_add=True)
#     day = datetime.today().strftime('%A')
#     total_made = models.FloatField(default=0)
#     comments = models.TextField()
#     order = models.IntegerField(default=0)
#     total = sum(range(0, 6))

#     def __str__(self):
#         return self.title




# # 2 seperate models that will corerespond to the same day
# class DayInput(models.Model):
#     # created_at = models.DateTimeField(atuo_now_add=True)
#     # title = models.CharField(max_length=32, unique=True)
#     # order = models.IntegerField(default=0)
#     monday = datetime.today().strftime('%A')
#     tuesday =
#     wednesday =
#     thursday =
#     friday =
#     saturday =
#     sunday =

# class Weekly(models.Model):
#     monday = models.FloatField(default=0)
#     tuesday = models.FloatField(default=0)
#     wednesday = models.FloatField(default=0)
#     thursday = models.FloatField(default=0)
#     friday = models.FloatField(default=0)
#     saturday = models.FloatField(default=0)
#     sunday = models.FloatField(default=0)
