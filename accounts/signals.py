from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import Account


def account_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance, name=instance.username)
        print('Account created!')


post_save.connect(account_profile, sender=User)
