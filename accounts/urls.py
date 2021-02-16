from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('exercises/', views.exercises, name="exercises"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('create_routine/', views.create_routine_view,  name='create_routine'),

]
