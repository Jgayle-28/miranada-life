from django import template

from ..forms import DailyEarningForm

register = template.Library()


@register.inclusion_tag('timesheet/_form.html')
def earnings_form():
    form = DailyEarningForm()
    return {'form': form}