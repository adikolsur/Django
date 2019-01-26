from django.shortcuts import render
from . import forms


# Create your views here.

def index(req):
    return render(req, 'formApp/index.html')


def form_model(req):
    form = forms.FormModel()

    if (req.method == 'POST'):
        form = forms.FormModel(req.POST)

        if (form.is_valid()):
            form.save(commit=True)
            return index(req)
        else:
            print("Invalid Form")
    dict = {'form': form}
    return render(req, 'formApp/form.html', context=dict)


def form_func(req):
    form = forms.FormName()

    if (req.method == 'POST'):
        form = forms.FormName(req.POST)

        if (form.is_valid()):
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
    dict = {'form': form}
    return render(req, 'formApp/form.html', context=dict)
