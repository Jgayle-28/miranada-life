import datetime
from django.db.models import Sum

from django import template
from django.utils import timezone

from ..forms import DailyEarningForm
from ..models import DailyEarning

register = template.Library()


@register.inclusion_tag('timesheet/_form.html')
def earnings_form():
    form = DailyEarningForm()
    return {'form': form}

# weekly total
@register.simple_tag(takes_context=True)
def weekly_total(context):
    user = context['user']
    # gathers the last 7 days
    seven_days = timezone.now() - datetime.timedelta(days=7)
    # Gets each days earning filtering by seven_days
    each_day = user.earnings.filter(recorded_at__gte=seven_days).values_list('made', flat=True)
    # Adds the last wee (7 days) logged
    total_for_week = each_day.aggregate(Sum('made')).get('made__sum', 0.00)
    # total = total_for_week['made_sum']
    return 'You made {} this week'.format(total_for_week)
    # returns users email
    # return user.email