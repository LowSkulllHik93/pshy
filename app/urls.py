from django.urls import path
from . import views
from .views import Main

urlpatterns = [
    path('', Main.index),
    path('start/', Main.start, name='start'),
    #path('randfunc', views.Functions.randfunc, name='randfunc'),
    #path('check', views.Functions.check, name='check'),

]
