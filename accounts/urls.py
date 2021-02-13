from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('exercises/', views.exercises, name="exercises"),
    # path('routines/', views.routines, name="routines"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
]
