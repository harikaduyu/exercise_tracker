import django_heroku
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['harikaduyu-exercise-tracker.herokuapp.com']

django_heroku.settings(locals())
