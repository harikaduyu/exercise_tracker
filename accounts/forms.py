from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account, Routine, Exercise


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'
        exclude = ['account']


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
