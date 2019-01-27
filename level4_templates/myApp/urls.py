from myApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('random/', views.random, name='random')
]
