from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    my_dict={'insert_here':"Whaatsup Pt2?"}
    return render(req,'firstApp/index.html',context=my_dict)

def help(req):
    dict={'myname':'Aditya'}
    return render(req,'firstApp/help.html',context=dict)

def wel(req):
    return HttpResponse("<h2>Welcome Page</h2>")
