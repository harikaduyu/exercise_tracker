from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Exercise, Account, Routine
from .exercise_calendar import Calendar
from .forms import RegisterForm, RoutineForm
# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='login')
def exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'accounts/exercises.html', {'exercises': exercises})


@login_required(login_url='login')
def account(request, pk):
    account_instance = Account.objects.get(id=pk)
    routines = account_instance.routine_set.all()
    routines_count = routines.count()
    context = {
        'routines': routines,
        'account': account_instance,
    }
    return render(request, 'accounts/account.html', context)


@login_required(login_url='login')
def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Account was created for {user.username}")
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is wrong.")

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

# todo: form not saving properly


@login_required(login_url='login')
def create_routine_view(request):
    account = request.user.account
    if request.method == "POST":
        form = RoutineForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = RoutineForm(instance=account)
    context = {'form': form}
    return render(request, 'accounts/routine_form.html', context)


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
