from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('exercises/', views.exercises, name="exercises"),
    path('register/', views.register, name="register"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),

]
