from myApp import views
from django.urls import path

app_name = 'myApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('random/', views.random, name='random')
]
