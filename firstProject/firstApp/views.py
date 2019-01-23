from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse("<h1> Hello World </h1>")

def wel(req):
    return HttpResponse("<h2>Welcome to First Page</h2>")