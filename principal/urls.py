from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),

]
    
