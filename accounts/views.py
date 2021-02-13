from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime

from .models import Exercise, Account, Routine
from .utils import Calendar

# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'accounts/exercises.html', {'exercises': exercises})


def account(request, pk):
    account_instance = Account.objects.get(id=pk)
    routines = account_instance.routine_set.all()
    routines_count = routines.count()
    context = {
        'routines': routines,
        'account': account_instance,
    }
    return render(request, 'accounts/account.html', context)


class CalendarView(generic.ListView):
    model = Routine
    template_name = "accounts/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        today = _get_date(self.request.GET.get('day', None))

        calendar_instance = Calendar(today.year, today.month)
        html_calendar = calendar_instance.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_calendar)
        return context


def _get_date(request_day):

    if request_day:
        year, month, day = (int(x) for x in request_day.split('-'))
        return date(year, month, day)

    return datetime.today()
