from django.shortcuts import render
from .models import *
def home(request):
    return render(request, 'classroom/home.html')

def a23(request, klass = "NA20MA"):
    students = Student.objects.order_by('?').filter(group = klass)
    context = {
        'students': students
    }
    return render(request, 'classroom/a23.html', context)

def b31(request, klass = "NA20MA"):
    students = Student.objects.order_by('?').filter(group = klass)

    context = {
        'students': students
    }
    return render(request, 'classroom/b31.html', context)

def b12(request, klass = "NA20MA"):
    students = Student.objects.order_by('?').filter(group = klass)
    context = {
        'students': students
    }
    return render(request, 'classroom/b12.html', context)
