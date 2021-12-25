from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'classroom/home.html')

def a23(request):
    return render(request, 'classroom/a23.html')

def b31(request):
    return render(request, 'classroom/b31.html')

def b12(request):
    return render(request, 'classroom/b12.html')