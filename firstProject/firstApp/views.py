from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic,WebPage,AccessRecord,User
# Create your views here.

def index(req):
    page_list=AccessRecord.objects.order_by('date')
    my_dict={'access_record':page_list}
    return render(req,'firstApp/index.html',context=my_dict)

def help(req):
    dict={'myname':'Aditya'}
    return render(req,'firstApp/help.html',context=dict)

def wel(req):
    return HttpResponse("<h2>Welcome Page</h2>")

def img(req):
    return render(req,'firstApp/image.html')

def user(req):
    data=User.objects.order_by('first_name')
    dict={'user_info':data}
    return render(req,'firstApp/user.html',context=dict)