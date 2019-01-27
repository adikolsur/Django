from django.shortcuts import render


# Create your views here.
def index(req):
    dict = {'text': "Hi There!", 'number': 100}
    return render(req, 'myApp/index.html', context=dict)


def relative(req):
    return render(req, 'myApp/relative_urls.html')


def random(req):
    return render(req, 'myApp/random.html')
