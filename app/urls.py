from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.index),
    path('randfunc', views.Functions.randfunc, name='randfunc'),
    path('check', views.Functions.check, name='check'),
]
