from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise, Account, Routine

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
