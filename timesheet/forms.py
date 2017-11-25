from django import forms

from . import models

class DailyEarningForm(forms.ModelForm):
    class Meta:
        fields = ('day', 'notes', 'made')
        model = models.DailyEarning
