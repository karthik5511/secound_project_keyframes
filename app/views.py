from django.shortcuts import render
from django.http import *

# Create your views here.

def animations(request):
    return render(request,'animations.html')

def karthik(request):
    return HttpResponse('<h1><i>karthik</i></h1>')

