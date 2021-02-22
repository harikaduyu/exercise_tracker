from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    # profile_pic = models.ImageField(
    #     default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    OPTIONS = (
        ('Strength Training', 'Strength Training'),
        ('Cardio', 'Cardio'),
        ('Stretching', 'Stretching'),
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, choices=OPTIONS,  null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Routine(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    duration = models.DurationField(default=timedelta(minutes=25))
    date_created = models.DateTimeField(
        default=timezone.now(),  null=True, blank=True)

    def __str__(self):
        return self.exercise.name
