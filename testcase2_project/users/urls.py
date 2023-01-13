from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('add_user/', views.add_user, name='add_user'),
]