from firstApp import views
from django.urls import path

urlpatterns = [
    path('help/', views.help, name='help'),
    path('welcome/',views.wel,name='wel'),
    path('image/',views.img,name='img'),
]