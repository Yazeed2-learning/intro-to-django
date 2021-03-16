from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(req, *args, **kwargs): 
    my_context = {
        'something':'this is the thing',
        'list': ['something', 3445, 5454 ,545]
    } 
    return render(req, 'home.html', my_context)