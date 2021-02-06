from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    # profile_pic = models.ImageField(
    #     default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


# class Exercise(models.Model):
