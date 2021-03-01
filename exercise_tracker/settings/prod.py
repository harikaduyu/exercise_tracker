import django_heroku
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['harikaduyu-exercise-tracker.herokuapp.com']

django_heroku.settings(locals())
