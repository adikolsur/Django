from formApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_func, name='forms'),
]