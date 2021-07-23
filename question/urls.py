from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    
    path('question', views.question, name='question'),
    path('result', views.result, name='result'),
    
]