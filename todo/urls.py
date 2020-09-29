from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('log-in', views.log_in, name='log-in'),
    path('log-out', views.log_out, name='log-out'),
    path('add', views.add, name='add'),
    path('<int:id>', views.delete, name='delete'),
]
