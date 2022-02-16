from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('index/', views.input_number, name='index'),
    path('answer/', views.answer, name='answer'),

]
