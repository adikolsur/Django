from django.shortcuts import render
from myApp.forms import UserForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(req):
    return render(req, 'myApp/index.html')


def register(req):
    registered = False
    if req.method == "POST":
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileForm(data=req.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(req, 'myApp/registration.html',
                  {'registered': registered, 'user_form': user_form, 'profile_form': profile_form})


def user_login(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username, password=password)
