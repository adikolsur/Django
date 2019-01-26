from django.shortcuts import render
from . import forms
# Create your views here.

def index(req):
    return render(req,'formApp/index.html')

def form_func(req):
    form=forms.FormName()
    dict={'form':form}
    return render(req,'formApp/form.html',context=dict)