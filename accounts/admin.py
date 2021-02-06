from django.contrib import admin
from .models import Account, Exercise, Routine


admin.site.register(Account)
admin.site.register(Exercise)
admin.site.register(Routine)

# Register your models here.
