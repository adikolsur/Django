from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'myApp/index.html')

def relative(req):
    return render(req,'myApp/relative_urls.html')

def random(req):
    return render(req,'myApp/random.html')